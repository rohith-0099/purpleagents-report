## Diagram Rules

**Default tool**
- For ANY diagram (architecture, flowchart, sequence, data flow, workflow, lifecycle, system design), ALWAYS use the **archify** skill.
- Do not hand-write Mermaid, ASCII, or raw SVG unless explicitly asked.
- If archify isn't installed, tell me to run: `npx skills add tt-a1i/archify -g`

**Fallback**
- For chart/business diagrams (quadrant, timeline, gantt, venn, pyramid, org chart, kanban), use the **diagram-design** skill if installed.
- Install: `npx skills add cathrynlavery/diagram-design`

**Style (Miro-like)**
- Light theme. Clean, colorful, card-style nodes with rounded corners.
- Group related components in labelled zones (e.g. Safe Environment, Reasoning Engine, Memory).
- Readable: 8–12 core components max; extra detail in node cards, not more arrows.
- One clear primary flow; label arrows with short verbs ("sends", "checks", "stores").

**Output**
- Save diagrams to `docs/diagrams/<descriptive-name>.html`.
- After generating, tell me the file path. I export PNG from the Export menu.
- For change requests, edit the existing diagram source — don't regenerate from scratch.