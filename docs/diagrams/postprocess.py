"""Turn an archify light-theme SVG export into a report figure.

Removes the dotted grid, grey canvas and node icons; swaps selected node
rectangles for standard flowchart shapes (diamond, cylinder, stadium);
freezes animation. Usage: postprocess.py in.svg out.svg shape:node-id ...
"""
import re
import sys

src, dst, *specs = sys.argv[1:]
shapes = dict(s.split(":")[::-1] for s in specs)  # node-id -> shape
svg = open(src, encoding="utf-8").read()

# Plain white canvas, no dotted grid.
svg = re.sub(r'(<rect x="0" y="0" width="[\d.]+" height="[\d.]+" fill=")#f4f5f7"', r'\1#ffffff"', svg, count=1)
svg = re.sub(r'<rect[^>]*fill="url\(#grid\)"[^>]*/>', "", svg)
# No icons/glyphs inside nodes.
svg = re.sub(r'<g[^>]*class="semantic-sigil[^"]*"[^>]*>.*?</g>', "", svg, flags=re.S)


def num(attr, tag):
    return float(re.search(attr + r'="([\d.]+)"', tag).group(1))


def shape_path(kind, x, y, w, h):
    cx, cy = x + w / 2, y + h / 2
    if kind == "diamond":
        return f"M{cx},{y} L{x + w},{cy} L{cx},{y + h} L{x},{cy} Z", ""
    if kind == "cylinder":
        ry = min(9, h / 6)
        body = (f"M{x},{y + ry} A{w / 2},{ry} 0 0 1 {x + w},{y + ry} V{y + h - ry} "
                f"A{w / 2},{ry} 0 0 1 {x},{y + h - ry} Z")
        lip = f"M{x},{y + ry} A{w / 2},{ry} 0 0 0 {x + w},{y + ry}"
        return body, lip
    if kind == "stadium":
        r = h / 2
        outer = (f"M{x + r},{y} H{x + w - r} A{r},{r} 0 0 1 {x + w - r},{y + h} "
                 f"H{x + r} A{r},{r} 0 0 1 {x + r},{y} Z")
        i, ri = 4, r - 4
        inner = (f"M{x + r},{y + i} H{x + w - r} A{ri},{ri} 0 0 1 {x + w - r},{y + h - i} "
                 f"H{x + r} A{ri},{ri} 0 0 1 {x + r},{y + i} Z")
        return outer, inner
    raise SystemExit(f"unknown shape {kind}")


def reshape(match):
    group = match.group(0)
    node = re.search(r'data-node-id="([^"]+)"', group).group(1)
    kind = shapes.get(node)
    if not kind:
        return group

    def swap(rect):
        tag = rect.group(0)
        x, y, w, h = (num(a, tag) for a in ("x", "y", "width", "height"))
        d, extra = shape_path(kind, x, y, w, h)
        attrs = re.sub(r'\s(x|y|width|height|rx)="[^"]*"', "", tag[len("<rect"):-2])
        out = f'<path d="{d}"{attrs}/>'
        if extra and "c-mask" not in tag:
            stroke_class = re.search(r'class="([^"]+)"', tag).group(1)
            out += f'<path d="{extra}" class="{stroke_class}" fill="none" stroke-width="1.25"/>'
        return out

    return re.sub(r'<rect[^>]*/>', swap, group)


svg = re.sub(r'<g id="node-[^"]+"[^>]*data-node-id="[^"]+".*?</g>', reshape, svg, flags=re.S)

override = ("<style>.c-mask{fill:#ffffff !important}"
            "*{animation:none !important;transition:none !important}"
            "[data-node-id]>path:not(.c-mask){stroke-width:1.25px}</style>")
svg = svg.replace("</svg>", override + "</svg>")
open(dst, "w", encoding="utf-8").write(svg)
