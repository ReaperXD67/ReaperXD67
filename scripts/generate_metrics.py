#!/usr/bin/env python3
"""Generate a self-hosted GitHub activity card from public GraphQL data.

The script uses only the Python standard library and GitHub's API. The rolling
window is pinned to whole UTC days so the generated SVG changes only when the
underlying public activity changes.
"""

from __future__ import annotations

import html
import json
import os
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://api.github.com/graphql"
LOGIN = os.environ.get("GH_LOGIN", "ReaperXD67")
OUTPUT = Path(os.environ.get("OUT_FILE", "metrics.svg"))

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      nodes {
        isArchived
        languages(first: 8, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def fetch() -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required")
    today = datetime.now(timezone.utc).date()
    start = today - timedelta(days=364)
    variables = {
        "login": LOGIN,
        "from": f"{start.isoformat()}T00:00:00Z",
        "to": f"{today.isoformat()}T23:59:59Z",
    }
    body = json.dumps({"query": QUERY, "variables": variables}).encode()
    request = urllib.request.Request(
        API,
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": f"{LOGIN}-profile-metrics",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise SystemExit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]["user"]


def streaks(days: list[dict]) -> tuple[int, int]:
    current = longest = run = 0
    for day in days:
        if day["contributionCount"]:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    tail = days[:-1] if days and days[-1]["contributionCount"] == 0 else days
    for day in reversed(tail):
        if not day["contributionCount"]:
            break
        current += 1
    return current, longest


def summarise(user: dict) -> dict:
    calendar = user["contributionsCollection"]["contributionCalendar"]
    weeks = [week["contributionDays"] for week in calendar["weeks"]]
    days = [day for week in weeks for day in week]
    weekly = [sum(day["contributionCount"] for day in week) for week in weeks]
    current, longest = streaks(days)
    language_bytes: Counter[str] = Counter()
    language_colors: dict[str, str] = {}
    active_repositories = 0
    for repository in user["repositories"]["nodes"]:
        if repository["isArchived"]:
            continue
        active_repositories += 1
        for edge in repository["languages"]["edges"]:
            name = edge["node"]["name"]
            language_bytes[name] += edge["size"]
            language_colors[name] = edge["node"].get("color") or "#4d8dff"
    return {
        "total": calendar["totalContributions"],
        "active_days": sum(bool(day["contributionCount"]) for day in days),
        "current": current,
        "longest": longest,
        "repositories": active_repositories,
        "weekly": weekly,
        "languages": [(name, size, language_colors[name]) for name, size in language_bytes.most_common(5)],
    }


def generate(stats: dict) -> str:
    width, height = 900, 250
    weekly = stats["weekly"] or [0]
    peak = max(weekly) or 1
    chart_x, chart_y, chart_w, chart_h = 450, 56, 398, 84
    step = chart_w / max(1, len(weekly) - 1)
    points = " ".join(
        f"{chart_x + index * step:.1f},{chart_y + chart_h - (value / peak) * chart_h:.1f}"
        for index, value in enumerate(weekly)
    )
    total_language_bytes = sum(item[1] for item in stats["languages"]) or 1
    language_x = 450.0
    language_segments = []
    language_labels = []
    palette = ["#ff5f38", "#d8ff4f", "#7ea8ff", "#f4f1e8", "#8b7cff"]
    for index, (name, size, _) in enumerate(stats["languages"]):
        segment_width = 398 * size / total_language_bytes
        color = palette[index % len(palette)]
        language_segments.append(
            f'<rect x="{language_x:.1f}" y="176" width="{segment_width:.1f}" height="8" fill="{color}"/>'
        )
        if index < 3:
            language_labels.append(
                f'<circle cx="{450 + index * 132}" cy="211" r="4" fill="{color}"/>'
                f'<text x="{460 + index * 132}" y="215" class="small">{html.escape(name)}</text>'
            )
        language_x += segment_width
    cards = [
        ("ROLLING 365D", stats["total"], "public contributions"),
        ("ACTIVE DAYS", stats["active_days"], "days with a signal"),
        ("CURRENT RUN", stats["current"], "consecutive days"),
        ("LONGEST RUN", stats["longest"], "consecutive days"),
    ]
    card_markup = []
    for index, (label, value, detail) in enumerate(cards):
        x = 34 + (index % 2) * 190
        y = 48 + (index // 2) * 91
        card_markup.append(
            f'<text x="{x}" y="{y}" class="label">{label}</text>'
            f'<text x="{x}" y="{y + 35}" class="number">{value}</text>'
            f'<text x="{x}" y="{y + 55}" class="small">{detail}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Aman's rolling public GitHub activity</title><desc id="desc">Daily generated contribution, streak, repository, and language summary.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#030405"/><stop offset="1" stop-color="#111318"/></linearGradient><linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#ff5f38"/><stop offset=".5" stop-color="#d8ff4f"/><stop offset="1" stop-color="#7ea8ff"/></linearGradient><clipPath id="chart"><rect x="450" y="52" width="398" height="94"/></clipPath></defs>
<style>.mono{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}.label{{font:600 10px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;letter-spacing:1.5px;fill:#97999f}}.number{{font:700 28px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#f4f1e8}}.small{{font:11px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#b2b3b6}}.grid{{stroke:#f4f1e8;stroke-opacity:.09}}</style>
<rect x="1" y="1" width="898" height="248" rx="10" fill="url(#bg)" stroke="#5b5d61"/>
<path d="M420 26V224" stroke="#f4f1e8" stroke-opacity=".18"/>
{''.join(card_markup)}
<g clip-path="url(#chart)"><path d="M450 76H848M450 104H848M450 132H848" class="grid"/><polyline points="{points}" fill="none" stroke="url(#line)" stroke-width="2.3" stroke-linejoin="round"><animate attributeName="stroke-dasharray" values="0 1200;1200 0" dur="1.7s" fill="freeze"/></polyline></g>
<text x="450" y="34" class="label">WEEKLY PUBLIC CONTRIBUTIONS · PEAK {peak}</text><text x="848" y="34" text-anchor="end" class="small">{stats['repositories']} source repositories</text>
<g>{''.join(language_segments)}</g><rect x="450" y="176" width="398" height="8" fill="none" stroke="#f4f1e8" stroke-opacity=".24"/>
<text x="450" y="166" class="label">LANGUAGE FOOTPRINT · BY PUBLIC BYTES</text>{''.join(language_labels)}
</svg>'''


def main() -> None:
    OUTPUT.write_text(generate(summarise(fetch())), encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
