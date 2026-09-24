"""Compose responsive profile headers around the approved, unaltered portrait.

Usage: python scripts/render_identity.py --portrait /path/to/approved-square.png
Requires Pillow and fontTools (with Brotli). The portrait is not retouched here.
The only photo transformations are proportional display resizing and a finite
entrance mask. Both compositions have explicit static/reduced-motion fallbacks.
"""

from argparse import ArgumentParser
from io import BytesIO
from pathlib import Path
from random import Random

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"
BG, FG, MUTED, LINE, ACID = "#0b0d0e", "#f5f5f1", "#b8bcb9", "#363b39", "#d8ff4f"


def font(size, weight=400):
    # Store the open-source original; convert to a Pillow-readable font in memory.
    source = TTFont(FONTS / "space-grotesk-latin-wght-normal.woff2")
    source.flavor = None
    buffer = BytesIO()
    source.save(buffer)
    buffer.seek(0)
    result = ImageFont.truetype(buffer, size)
    result.set_variation_by_axes([weight])
    return result


def text(draw, xy, content, size=24, color=FG, weight=400):
    draw.text(xy, content, font=font(size, weight), fill=color)


def base(mobile=False):
    width, height = (700, 890) if mobile else (1280, 480)
    canvas = Image.new("RGB", (width, height), BG)
    d = ImageDraw.Draw(canvas)
    d.rectangle((0, 0, width - 1, height - 1), outline=LINE)
    if mobile:
        text(d, (44, 485), "Aman Kumar", 66, weight=600)
        text(d, (46, 578), "AI Engineer &", 35)
        text(d, (46, 625), "Full-Stack Developer", 35)
        d.line((46, 709, 654, 709), fill=LINE)
        text(d, (46, 742), "Intelligence, engineered.", 31, ACID, 500)
        text(d, (46, 814), "Agents · Retrieval · Reliable systems", 22, MUTED)
        return canvas, (140, 32, 420)
    text(d, (46, 45), "Aman Kumar", 78, weight=600)
    text(d, (48, 164), "AI Engineer &", 42)
    text(d, (48, 219), "Full-Stack Developer", 42)
    text(d, (48, 310), "Intelligence, engineered.", 31, ACID, 500)
    d.line((48, 388, 752, 388), fill=LINE)
    text(d, (48, 412), "Agents · Retrieval · Reliable systems", 22, MUTED)
    return canvas, (800, 16, 448)


def render_variant(portrait, mobile=False, review=False):
    composition, (px, py, size) = base(mobile)
    photo = portrait.resize((size, size), Image.Resampling.LANCZOS)
    coarse = photo.resize((16, 16), Image.Resampling.BOX).resize(photo.size, Image.Resampling.NEAREST)
    tile = 28
    count = (size + tile - 1) // tile
    rng = Random(67)
    offsets = {(x, y): rng.uniform(-0.05, 0.05) for y in range(count) for x in range(count)}
    frames = []
    for index in range(34):
        progress = min(1.0, index / 30)
        frame = composition.copy()
        reveal = coarse.copy()
        if progress >= 1:
            reveal = photo.copy()
        else:
            mask = ImageDraw.Draw(reveal)
            for y in range(count):
                for x in range(count):
                    threshold = (y + 0.5) / count + offsets[x, y]
                    box = (x * tile, y * tile, min(size, (x + 1) * tile), min(size, (y + 1) * tile))
                    if threshold < progress:
                        reveal.paste(photo.crop(box), box)
            scan_y = min(size - 1, round(progress * size))
            mask.line((0, scan_y, size - 1, scan_y), fill=ACID, width=1)
        frame.paste(reveal, (px, py))
        frames.append(frame)
    prefix = "identity-mobile" if mobile else "identity"
    final = frames[-1]
    final.save(ASSETS / f"{prefix}-still.png", optimize=True)
    palette = final.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    quantized = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    # No NETSCAPE loop extension: the 1.7s reveal ends on the recognizable portrait.
    quantized[0].save(ASSETS / f"{prefix}-scan.gif", save_all=True, append_images=quantized[1:],
                      duration=[50] * len(frames), disposal=1, optimize=True)
    if review:
        (ROOT / "output").mkdir(exist_ok=True)
        frames[14].save(ROOT / "output" / f"{prefix}-mid-reveal.png", optimize=True)
    print(f"{prefix}: {final.width}x{final.height}; finite 1700ms reveal; "
          f"{(ASSETS / f'{prefix}-scan.gif').stat().st_size:,} bytes")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--portrait", required=True, type=Path)
    parser.add_argument("--review", action="store_true")
    args = parser.parse_args()
    ASSETS.mkdir(exist_ok=True)
    original = Image.open(args.portrait).convert("RGB")
    if original.width != original.height:
        raise ValueError("Use the approved square portrait; this compositor will not crop it.")
    original.resize((800, 800), Image.Resampling.LANCZOS).save(
        ASSETS / "aman-kumar-avatar.jpg", quality=95, subsampling=0, optimize=True
    )
    render_variant(original, review=args.review)
    render_variant(original, mobile=True, review=args.review)
