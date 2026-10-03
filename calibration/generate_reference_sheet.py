#!/usr/bin/env python3
"""Generate a printable SVG reference/calibration sheet with a fine grid.

SVG is used (not a raster PNG) because it encodes real physical units (mm),
so the sheet prints at its exact physical size regardless of viewer/printer
DPI assumptions -- as long as it's printed at 100% / "actual size".
"""

import argparse


def generate_svg(size_mm: float, grid_mm: float, stroke_mm: float) -> str:
    lines = []
    n = round(size_mm / grid_mm)
    for i in range(n + 1):
        pos = i * grid_mm
        lines.append(f'<line x1="{pos}" y1="0" x2="{pos}" y2="{size_mm}" />')
        lines.append(f'<line x1="0" y1="{pos}" x2="{size_mm}" y2="{pos}" />')

    return f'''<svg xmlns="http://www.w3.org/2000/svg"
     width="{size_mm}mm" height="{size_mm}mm"
     viewBox="0 0 {size_mm} {size_mm}">
  <rect x="0" y="0" width="{size_mm}" height="{size_mm}" fill="white" />
  <g stroke="black" stroke-width="{stroke_mm}">
    {"".join(lines)}
  </g>
</svg>
'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size-mm", type=float, default=50.0, help="sheet width/height in mm")
    parser.add_argument("--grid-mm", type=float, default=1.0, help="grid cell size in mm")
    parser.add_argument("--stroke-mm", type=float, default=0.1, help="line stroke width in mm")
    parser.add_argument("--out", default="reference-sheet-5cm-1mm.svg", help="output file path")
    args = parser.parse_args()

    svg = generate_svg(args.size_mm, args.grid_mm, args.stroke_mm)
    with open(args.out, "w") as f:
        f.write(svg)


if __name__ == "__main__":
    main()
