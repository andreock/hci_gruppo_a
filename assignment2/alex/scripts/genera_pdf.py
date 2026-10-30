#!/usr/bin/env python3
"""Genera i sei PDF dalle schede Markdown presenti nella cartella alex."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"

FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("DejaVu", FONT_REGULAR))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FONT_BOLD))

BLUE = colors.HexColor("#0B4F6C")
PALE_BLUE = colors.HexColor("#EAF3F7")
LINE = colors.HexColor("#B8C6CC")
INK = colors.HexColor("#172126")
MUTED = colors.HexColor("#4E6068")

styles = getSampleStyleSheet()
TITLE = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    fontName="DejaVu-Bold",
    fontSize=19,
    leading=22,
    textColor=INK,
    alignment=TA_LEFT,
    spaceAfter=3 * mm,
)
SECTION_TITLE = ParagraphStyle(
    "SectionTitleCustom",
    parent=TITLE,
    fontSize=16,
    leading=19,
    spaceAfter=5 * mm,
)
SUBTITLE = ParagraphStyle(
    "SubtitleCustom",
    parent=styles["Normal"],
    fontName="DejaVu",
    fontSize=8.5,
    leading=10,
    textColor=MUTED,
)
META = ParagraphStyle(
    "MetaCustom",
    parent=styles["Normal"],
    fontName="DejaVu",
    fontSize=7.8,
    leading=10.2,
    textColor=INK,
)
BOX_TITLE = ParagraphStyle(
    "BoxTitle",
    parent=styles["Normal"],
    fontName="DejaVu-Bold",
    fontSize=8,
    leading=9.5,
    textColor=BLUE,
    spaceAfter=2.2 * mm,
)
BOX_BODY = ParagraphStyle(
    "BoxBody",
    parent=styles["Normal"],
    fontName="DejaVu",
    fontSize=7.25,
    leading=9.2,
    textColor=INK,
)
J_HEAD = ParagraphStyle(
    "JourneyHead",
    parent=styles["Normal"],
    fontName="DejaVu-Bold",
    fontSize=7.25,
    leading=8.4,
    textColor=INK,
)
J_BODY = ParagraphStyle(
    "JourneyBody",
    parent=styles["Normal"],
    fontName="DejaVu",
    fontSize=6.35,
    leading=7.8,
    textColor=INK,
)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 13 * mm, doc.pagesize[0] - doc.rightMargin, 13 * mm)
    canvas.setFont("DejaVu", 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 8.5 * mm, "Gruppo A · Assignment 2 · proto-persona ipotetica")
    canvas.drawRightString(doc.pagesize[0] - doc.rightMargin, 8.5 * mm, f"Pagina {doc.page}")
    canvas.restoreState()


def read_sections(path: Path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    sections = {}
    for match in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
        sections[match.group(1).strip()] = match.group(2).strip()
    return text, sections


def inline_markup(value: str) -> str:
    value = html.escape(value, quote=False)
    value = value.replace("&lt;br&gt;", "<br/>")
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    return value


def body_markup(value: str) -> str:
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    converted = []
    for line in lines:
        if line.startswith("- "):
            converted.append("• " + inline_markup(line[2:]))
        elif line.startswith("> "):
            converted.append("<i>" + inline_markup(line[2:]) + "</i>")
        else:
            converted.append(inline_markup(line))
    return "<br/>".join(converted)


def box(title: str, content: str):
    return [Paragraph(inline_markup(title), BOX_TITLE), Paragraph(body_markup(content), BOX_BODY)]


def persona_header(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    group = next(line for line in lines if line.startswith("Gruppo:"))
    service = next(line for line in lines if line.startswith("Servizio o progetto:"))
    kind = next(line for line in lines if line.startswith("Tipo:"))
    return group, service, kind


def build_persona(path: Path, output: Path):
    text, sec = read_sections(path)
    group, service, kind = persona_header(text)
    doc = SimpleDocTemplate(
        str(output),
        pagesize=letter,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=14 * mm,
        bottomMargin=18 * mm,
        title=f"Scheda persona - {path.stem}",
        author="Gruppo A",
    )
    story = [
        Paragraph("Scheda persona", TITLE),
        Paragraph("Cristina Gena · Human-Computer Interaction", SUBTITLE),
        Spacer(1, 2.5 * mm),
        Paragraph(inline_markup(group), META),
        Paragraph(inline_markup(service), META),
        Paragraph(inline_markup(kind), META),
        Spacer(1, 4 * mm),
    ]
    pairs = [
        ("Nome convenzionale e descrizione del profilo", "Scenario e obiettivo principale"),
        ("Attività e comportamenti", "Bisogni e aspettative"),
        ("Obiettivi e motivazioni", "Difficoltà e frustrazioni"),
        ("Contesto e vincoli di utilizzo", "Competenze e strumenti digitali"),
        ("Esigenze di accessibilità", "Frase rappresentativa e provenienza"),
    ]
    data = []
    for left, right in pairs:
        data.append([box(left, sec[left]), box(right, sec[right])])
    table = Table(data, colWidths=[90.5 * mm, 90.5 * mm], hAlign="LEFT", splitByRow=1)
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.55, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.45, LINE),
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)
    story.extend(
        [
            Spacer(1, 4 * mm),
            Table(
                [[box("Fonti ed evidenze disponibili", sec["Fonti ed evidenze disponibili"])]],
                colWidths=[181 * mm],
                style=TableStyle(
                    [
                        ("BOX", (0, 0), (-1, -1), 0.55, LINE),
                        ("LEFTPADDING", (0, 0), (-1, -1), 7),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                        ("TOPPADDING", (0, 0), (-1, -1), 7),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ]
                ),
            ),
            PageBreak(),
            Paragraph("Ipotesi da verificare e informazioni mancanti", SECTION_TITLE),
            Paragraph(
                "Le seguenti ipotesi orientano la ricerca successiva e non costituiscono evidenze raccolte con utenti.",
                SUBTITLE,
            ),
            Spacer(1, 5 * mm),
            Table(
                [[box("Domande aperte", sec["Ipotesi da verificare e informazioni mancanti"])]],
                colWidths=[181 * mm],
                style=TableStyle(
                    [
                        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FBFC")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                        ("TOPPADDING", (0, 0), (-1, -1), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                    ]
                ),
            ),
        ]
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def journey_header(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    start = next(i for i, line in enumerate(lines) if line.startswith("Gruppo:"))
    return lines[start : start + 4]


def parse_markdown_table(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    rows = []
    for index, line in enumerate(lines):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if index == 1 and all(re.fullmatch(r"-+", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def table_para(value: str, style):
    value = value.replace("**", "")
    return Paragraph(inline_markup(value), style)


def build_journey(path: Path, output: Path):
    text, sec = read_sections(path)
    header_lines = journey_header(text)
    rows = parse_markdown_table(text)
    formatted = []
    for r_index, row in enumerate(rows):
        formatted.append(
            [table_para(cell, J_HEAD if r_index == 0 or c_index == 0 else J_BODY) for c_index, cell in enumerate(row)]
        )
    page_w, page_h = landscape(letter)
    usable_w = page_w - 24 * mm
    first = 31 * mm
    col_widths = [first] + [(usable_w - first) / 6] * 6
    doc = SimpleDocTemplate(
        str(output),
        pagesize=landscape(letter),
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=10 * mm,
        bottomMargin=17 * mm,
        title=f"Scheda user journey - {path.stem}",
        author="Gruppo A",
    )
    story = [
        Paragraph("Scheda user journey", TITLE),
        Paragraph("Cristina Gena · Human-Computer Interaction", SUBTITLE),
        Spacer(1, 2 * mm),
    ]
    for line in header_lines:
        story.append(Paragraph(inline_markup(line), META))
    story.append(Spacer(1, 3 * mm))
    journey_table = Table(formatted, colWidths=col_widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    journey_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (-1, 0), PALE_BLUE),
                ("BACKGROUND", (0, 1), (0, -1), colors.HexColor("#F1F6F8")),
                ("GRID", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.extend(
        [
            journey_table,
            PageBreak(),
            Paragraph("Fonti e ipotesi", TITLE),
            Paragraph(
                "La mappa è una ricostruzione as-is ipotetica: i comportamenti e le emozioni devono essere validati con utenti.",
                SUBTITLE,
            ),
            Spacer(1, 5 * mm),
            Table(
                [[box("Note di metodo, momenti critici e continuità", sec["Fonti e ipotesi"])]],
                colWidths=[usable_w],
                style=TableStyle(
                    [
                        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FBFC")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                        ("TOPPADDING", (0, 0), (-1, -1), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                    ]
                ),
            ),
        ]
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for source in sorted((ROOT / "personas").glob("P*.md")):
        build_persona(source, OUT / f"{source.stem}.pdf")
    for source in sorted((ROOT / "journeys").glob("J*.md")):
        build_journey(source, OUT / f"{source.stem}.pdf")
    produced = sorted(OUT.glob("*.pdf"))
    if len(produced) != 6:
        raise RuntimeError(f"Attesi 6 PDF, prodotti {len(produced)}")
    for pdf in produced:
        print(pdf)


if __name__ == "__main__":
    main()
