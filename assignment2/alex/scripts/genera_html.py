#!/usr/bin/env python3
"""Genera le sei schede HTML dai sorgenti Markdown della cartella alex."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "html"

COMMON_CSS = r"""
:root {
  color-scheme: light;
  --ink: #111820;
  --muted: #4d5c67;
  --line: #d9d9d9;
  --panel: #e8f0f6;
  --accent: #0b4f6c;
  --paper: #ffffff;
}
* { box-sizing: border-box; }
html { background: #eef1f3; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: Calibri, "Segoe UI", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.35;
}
.sheet {
  width: min(1120px, calc(100% - 32px));
  margin: 24px auto;
  padding: 44px 50px;
  background: #fff;
  box-shadow: 0 6px 26px rgba(20, 32, 40, .12);
}
h1 { margin: 0 0 4px; font-size: 25pt; line-height: 1.12; font-weight: 500; }
.course { margin: 0 0 14px; }
.meta { display: flex; flex-wrap: wrap; gap: 3px 18px; margin-bottom: 4px; }
.meta p { margin: 0; }
.instructions { margin: 10px 0 14px; color: var(--muted); font-size: 9pt; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid var(--line); padding: 9px; vertical-align: top; text-align: left; }
th { font-weight: 700; }
.field h2, .notes h2 {
  margin: 0 0 8px;
  color: var(--ink);
  font-size: 10.5pt;
  line-height: 1.25;
}
.field p, .field blockquote, .notes p { margin: 0; }
ul { margin: 0; padding-left: 19px; }
li + li { margin-top: 2px; }
blockquote { font-style: italic; }
.persona-grid { table-layout: fixed; }
.persona-grid td { width: 50%; min-height: 88px; }
.full-field { margin-top: 16px; border: 1px solid var(--line); padding: 12px; }
.page-break { break-before: page; margin-top: 18px; }
.journey-wrap { overflow-x: auto; }
.journey { min-width: 1120px; table-layout: fixed; font-size: 8.4pt; line-height: 1.24; }
.journey thead th, .journey tbody th { background: var(--panel); }
.journey thead th:first-child, .journey tbody th { width: 132px; }
.journey td, .journey th { padding: 7px; }
.journey .notes-row td { background: #fbfcfd; }
.journey .notes-row h2 { margin: 0 0 6px; font-size: 9pt; }
.template-note { margin: 8px 0 0; font-size: 8.5pt; color: var(--muted); }
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;
}
@media (max-width: 760px) {
  .sheet { width: 100%; margin: 0; padding: 24px 18px; box-shadow: none; }
  .persona-grid, .persona-grid tbody, .persona-grid tr, .persona-grid td { display: block; width: 100%; }
  .persona-grid td + td { border-top: 0; }
  h1 { font-size: 22pt; }
}
@media print {
  @page { size: Letter portrait; margin: 12mm; }
  html, body { background: #fff; }
  .sheet { width: 100%; margin: 0; padding: 0; box-shadow: none; }
  .persona-grid tr, .full-field { break-inside: avoid; }
  .journey-sheet { width: 100%; }
  .journey { min-width: 0; font-size: 6.6pt; }
  .journey td, .journey th { padding: 4px; }
}
"""

JOURNEY_PRINT_CSS = r"""
@media print {
  @page { size: Letter landscape; margin: 9mm; }
  h1 { font-size: 20pt; }
  .course { margin-bottom: 7px; }
  .meta { font-size: 8pt; }
  .instructions { margin: 6px 0 8px; }
}
"""


def read_sections(path: Path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    sections = {}
    for match in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
        sections[match.group(1).strip()] = match.group(2).strip()
    return text, sections


def inline(value: str) -> str:
    safe = html.escape(value.strip(), quote=False)
    safe = safe.replace("&lt;br&gt;", "<br>")
    safe = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", safe)
    return safe


def block(value: str) -> str:
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    output = []
    list_open = False
    for line in lines:
        if line.startswith("- "):
            if not list_open:
                output.append("<ul>")
                list_open = True
            output.append(f"<li>{inline(line[2:])}</li>")
            continue
        if list_open:
            output.append("</ul>")
            list_open = False
        if line.startswith("> "):
            output.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        else:
            output.append(f"<p>{inline(line)}</p>")
    if list_open:
        output.append("</ul>")
    return "\n".join(output)


def field(title: str, value: str) -> str:
    return f'<div class="field"><h2>{html.escape(title)}</h2>{block(value)}</div>'


def document(title: str, body: str, extra_css: str = "") -> str:
    return f"""<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>{COMMON_CSS}{extra_css}</style>
</head>
<body>
{body}
</body>
</html>
"""


def persona_header(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return (
        next(line for line in lines if line.startswith("Gruppo:")),
        next(line for line in lines if line.startswith("Servizio o progetto:")),
        next(line for line in lines if line.startswith("Tipo:")),
    )


def build_persona(path: Path, output: Path):
    text, sections = read_sections(path)
    group, service, kind = persona_header(text)
    pairs = [
        ("Nome convenzionale e descrizione del profilo", "Scenario e obiettivo principale"),
        ("Attività e comportamenti", "Bisogni e aspettative"),
        ("Obiettivi e motivazioni", "Difficoltà e frustrazioni"),
        ("Contesto e vincoli di utilizzo", "Competenze e strumenti digitali"),
        ("Esigenze di accessibilità", "Frase rappresentativa e provenienza"),
    ]
    rows = "\n".join(
        f"<tr><td>{field(left, sections[left])}</td><td>{field(right, sections[right])}</td></tr>"
        for left, right in pairs
    )
    name = path.stem.split("_", 1)[1].replace("_", " ").title()
    body = f"""<main class="sheet">
  <header>
    <h1>Scheda persona</h1>
    <p class="course">Cristina Gena · Human-Computer Interaction</p>
    <div class="meta">
      <p>{inline(group)}</p>
      <p>{inline(service)}</p>
      <p>{inline(kind)}</p>
    </div>
    <p class="instructions">Scheda compilata secondo il template ufficiale. Le ipotesi da validare sono indicate esplicitamente.</p>
  </header>
  <table class="persona-grid">
    <caption class="sr-only">Campi della scheda persona di {html.escape(name)}</caption>
    <tbody>{rows}</tbody>
  </table>
  <section class="full-field">{field("Fonti ed evidenze disponibili", sections["Fonti ed evidenze disponibili"])}</section>
  <section class="full-field page-break">{field("Ipotesi da verificare e informazioni mancanti", sections["Ipotesi da verificare e informazioni mancanti"])}</section>
</main>"""
    output.write_text(document(f"Scheda persona · {name}", body), encoding="utf-8")


def parse_markdown_table(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    rows = []
    for index, line in enumerate(lines):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if index == 1 and all(re.fullmatch(r"-+", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def journey_header(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    start = next(i for i, line in enumerate(lines) if line.startswith("Gruppo:"))
    return lines[start : start + 4]


def build_journey(path: Path, output: Path):
    text, sections = read_sections(path)
    headers = journey_header(text)
    rows = parse_markdown_table(text)
    head = "".join(f'<th scope="col">{inline(cell.replace("**", ""))}</th>' for cell in rows[0])
    body_rows = []
    for row in rows[1:]:
        label = inline(row[0].replace("**", ""))
        cells = "".join(f"<td>{inline(cell)}</td>" for cell in row[1:])
        body_rows.append(f'<tr><th scope="row">{label}</th>{cells}</tr>')
    notes = block(sections["Fonti e ipotesi"])
    body_rows.append(
        '<tr class="notes-row"><th scope="row">Fonti e ipotesi</th>'
        f'<td colspan="6"><div class="notes">{notes}</div></td></tr>'
    )
    person = path.stem.split("_", 1)[1].replace("_", " ").title()
    meta = "\n".join(f"<p>{inline(line)}</p>" for line in headers)
    content = f"""<main class="sheet journey-sheet">
  <header>
    <h1>Scheda user journey</h1>
    <p class="course">Cristina Gena · Human-Computer Interaction</p>
    <div class="meta">{meta}</div>
    <p class="instructions">Le fasi sono colonne; le dimensioni del percorso sono righe. La sesta fase è stata aggiunta come previsto dal template.</p>
  </header>
  <div class="journey-wrap" role="region" aria-label="User journey di {html.escape(person)}" tabindex="0">
    <table class="journey">
      <caption class="sr-only">Mappa del percorso di {html.escape(person)}</caption>
      <thead><tr>{head}</tr></thead>
      <tbody>{''.join(body_rows)}</tbody>
    </table>
  </div>
  <p class="template-note">Emozioni: punteggio da -2 a +2 e base ipotizzata. Fonti: proto-persona non basata su ricerca diretta.</p>
</main>"""
    output.write_text(document(f"User journey · {person}", content, JOURNEY_PRINT_CSS), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for source in sorted((ROOT / "personas").glob("P*.md")):
        build_persona(source, OUT / f"{source.stem}.html")
    for source in sorted((ROOT / "journeys").glob("J*.md")):
        build_journey(source, OUT / f"{source.stem}.html")
    produced = sorted(OUT.glob("*.html"))
    if len(produced) != 6:
        raise RuntimeError(f"Attesi 6 file HTML, prodotti {len(produced)}")
    for artifact in produced:
        print(artifact)


if __name__ == "__main__":
    main()
