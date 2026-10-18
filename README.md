# PurpleAgents — B.Tech Project Report

LaTeX source for the Phase-1 project report of **PurpleAgents: A Dual-Reasoning
Agentic Framework for Intelligent Purple Team Cyber Defense**.

The PDF starts at the Table of Contents. The title page, certificate,
declaration, abstract and acknowledgement are prepared separately and attached
in front.

## Layout

- `report/main.tex` — document setup and front matter (Contents, List of Figures, List of Symbols)
- `report/chapters/` — Chapters 1–8 and References
- `report/figures/` — `fig-5-1.png`, `fig-5-2.png`, `fig-5-3.png`, `fig-6-1.png` (placeholders render until these exist)
- `docs/diagrams/` — diagram sources (HTML); `postprocess.py` turns their light SVG export into the clean report figures (white background, no icons, flowchart shapes)
- `PurpleAgents_Report_Spec.md` — content spec

## Build

```sh
cd report
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

## License

This project report is licensed under CC BY-NC 4.0.
