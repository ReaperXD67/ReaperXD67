"""Render Aman's finite profile introduction from his approved, unaltered portrait.

Usage: python scripts/render_identity.py --portrait /path/to/approved-portrait.png
Requires Pillow. Composition changes only: resize, pixel sampling, and reveal masks.
No retouching, facial alteration, or AI reconstruction is performed here.
"""

from argparse import ArgumentParser
from pathlib import Path
from random import Random

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
W, H = 1000, 408
PHOTO_X, PHOTO_Y, PHOTO_SIZE = 648, 26, 324
BG = "#0b0d0e"
FG = "#f3f1e9"
MUTED = "#a5aaa9"
LINE = "#343a38"
ACID = "#d8ff4f"
ORANGE = "#ff6840"


def font(size, bold=False, mono=False):
    filename = "consola.ttf" if mono else ("segoeuib.ttf" if bold else "segoeui.ttf")
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / filename), size)


def text(draw, xy, content, size=16, color=FG, bold=False, mono=False):
    draw.text(xy, content, font=font(size, bold, mono), fill=color)


def base():
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    for x in range(0, W, 32):
        d.line((x, 0, x, H), fill="#121615")
    for y in range(0, H, 32):
        d.line((0, y, W, y), fill="#121615")
    d.rectangle((0, 0, W - 1, H - 1), outline=LINE)
    d.rectangle((0, 0, 212, 3), fill=ORANGE)
    d.line((624, 26, 624, 378), fill=LINE)
    d.rectangle((32, 35, 38, 41), fill=ACID)
    text(d, (48, 26), "BENGALURU, INDIA", 13, MUTED, mono=True)
    text(d, (32, 70), "AMAN KUMAR", 55, bold=True)
    text(d, (35, 147), "AI ENGINEER", 27, ACID, bold=True)
    text(d, (35, 183), "& FULL-STACK DEVELOPER", 23, FG, bold=True)
    text(d, (35, 238), "Accountable intelligence.", 23)
    text(d, (35, 269), "Reliable systems. Visible proof.", 23)
    d.line((35, 324, 588, 324), fill=LINE)
    text(d, (35, 340), "LLM APPLICATIONS  /  AGENTS  /  RAG", 13, MUTED, mono=True)
    text(d, (35, 366), "BUILD  →  MEASURE  →  VERIFY  →  SHIP", 13, FG, mono=True)
    d.rectangle((PHOTO_X - 1, PHOTO_Y - 1, PHOTO_X + PHOTO_SIZE, PHOTO_Y + PHOTO_SIZE), outline=LINE)
    for x, y, dx, dy in [(PHOTO_X, PHOTO_Y, 1, 1), (PHOTO_X + PHOTO_SIZE - 1, PHOTO_Y, -1, 1),
                          (PHOTO_X, PHOTO_Y + PHOTO_SIZE - 1, 1, -1),
                          (PHOTO_X + PHOTO_SIZE - 1, PHOTO_Y + PHOTO_SIZE - 1, -1, -1)]:
        d.line((x, y, x + dx * 15, y), fill=MUTED, width=2)
        d.line((x, y, x, y + dy * 15), fill=MUTED, width=2)
    return canvas


def render(source, review=False):
    ASSETS.mkdir(exist_ok=True)
    portrait = Image.open(source).convert("RGB")
    # The approved source is square: preserve its entire framing and appearance.
    if portrait.width != portrait.height:
        raise ValueError("Use the approved square portrait to avoid an unintended crop.")
    portrait.resize((800, 800), Image.Resampling.LANCZOS).save(
        ASSETS / "aman-kumar-avatar.jpg", quality=95, subsampling=0, optimize=True
    )
    portrait = portrait.resize((PHOTO_SIZE, PHOTO_SIZE), Image.Resampling.LANCZOS)
    mosaic = portrait.resize((18, 18), Image.Resampling.BOX).resize(portrait.size, Image.Resampling.NEAREST)
    rng = Random(67)
    tile = 18
    columns = PHOTO_SIZE // tile
    offsets = {(x, y): rng.uniform(-0.08, 0.08) for y in range(columns) for x in range(columns)}
    frames = []
    for index in range(44):
        progress = min(1.0, index / 39)
        canvas = base()
        image = mosaic.copy()
        if progress >= 1:
            image = portrait.copy()
        else:
            d = ImageDraw.Draw(image)
            for y in range(columns):
                for x in range(columns):
                    threshold = (y + 0.5) / columns + offsets[x, y]
                    box = (x * tile, y * tile, (x + 1) * tile, (y + 1) * tile)
                    if threshold < progress:
                        image.paste(portrait.crop(box), box)
                    elif threshold < progress + 0.10:
                        d.rectangle((box[0], box[1], box[2] - 1, box[3] - 1), outline="#a0ad72")
            scan_y = min(PHOTO_SIZE - 1, round(progress * PHOTO_SIZE))
            d.line((0, scan_y, PHOTO_SIZE, scan_y), fill=ACID, width=1)
        canvas.paste(image, (PHOTO_X, PHOTO_Y))
        d = ImageDraw.Draw(canvas)
        text(d, (PHOTO_X, 365), "THE PERSON BEHIND THE SYSTEMS", 12, MUTED, mono=True)
        text(d, (PHOTO_X + 278, 365), f"{round(progress * 100):03}", 12, ACID, mono=True)
        frames.append(canvas)

    final = frames[-1]
    final.save(ASSETS / "identity-still.png", optimize=True)
    # Keep the same palette across frames to prevent color shimmer on the face.
    palette = final.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    quantized = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    # Intentionally omit the loop extension: a single <2.5s pass settles to a still.
    quantized[0].save(ASSETS / "identity-scan.gif", save_all=True, append_images=quantized[1:],
                      duration=[50] * 43 + [100], disposal=1, optimize=True)
    if review:
        for index in (0, 16, 31):
            frames[index].save(ASSETS / f"identity-review-{index:02}.png", optimize=True)
    print(f"Rendered {len(frames)} frames; finite 2250ms reveal; {W}x{H}.")
    print(f"GIF: {(ASSETS / 'identity-scan.gif').stat().st_size:,} bytes")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--portrait", required=True, type=Path)
    parser.add_argument("--review", action="store_true", help="Also emit three intermediate review frames.")
    args = parser.parse_args()
    render(args.portrait, args.review)
