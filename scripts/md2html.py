#!/usr/bin/env python3
"""Zet lesmateriaal in Markdown om naar een standalone HTML-pagina.

Gebruik:
    python tools/md2html.py course/ai-enterprise/lessons/lesson-001-ai-business-vs-saas.md
    python tools/md2html.py course/ai-enterprise/lessons -o docs/
    python tools/md2html.py les.md --stdout

Alleen standaardbibliotheek. Ondersteunt de Markdown-subset die in dit
lesmateriaal voorkomt: koppen, alinea's, vet/cursief/code, links, opsommingen,
genummerde lijsten, citaten, codeblokken en horizontale lijnen.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- vormgeving

CSS = """\
  :root {
    --bg: #fbfaf8;
    --surface: #ffffff;
    --text: #1f1d1a;
    --muted: #61605c;
    --line: #e2ded7;
    --accent: #8a5a2b;
    --accent-soft: #f4ede3;
    --quote-bg: #f6f2ec;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #171614;
      --surface: #201e1b;
      --text: #ece8e1;
      --muted: #a39f97;
      --line: #35322d;
      --accent: #d2a06a;
      --accent-soft: #2a2520;
      --quote-bg: #262220;
    }
  }
  :root[data-theme="dark"] {
    --bg: #171614;
    --surface: #201e1b;
    --text: #ece8e1;
    --muted: #a39f97;
    --line: #35322d;
    --accent: #d2a06a;
    --accent-soft: #2a2520;
    --quote-bg: #262220;
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size: 17px;
    line-height: 1.65;
  }
  .wrap { max-width: 44rem; margin: 0 auto; padding: 3rem 16px 5rem; }

  h1 {
    font-size: 1.75rem; line-height: 1.25; font-weight: 600;
    margin: 0 0 .6rem;
  }
  .meta {
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-size: .82rem; color: var(--muted); letter-spacing: .02em;
    margin: 0 0 2rem; padding-bottom: 1.25rem;
    border-bottom: 2px solid var(--line);
  }
  h2 {
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-size: 1.05rem; font-weight: 600; letter-spacing: .01em;
    margin: 2.5rem 0 .9rem; padding-bottom: .4rem;
    border-bottom: 1px solid var(--line);
  }
  h3 {
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-size: .95rem; font-weight: 600; margin: 1.8rem 0 .6rem;
  }
  h4, h5, h6 { font-size: .9rem; margin: 1.5rem 0 .5rem; }

  p { margin: 0 0 1rem; }
  ol, ul { margin: 0 0 1rem; padding-left: 1.4rem; }
  li { margin-bottom: .5rem; }
  a { color: var(--accent); }

  hr { border: 0; border-top: 1px solid var(--line); margin: 2.5rem 0; }

  blockquote {
    margin: 1.2rem 0;
    padding: 1rem 1.25rem;
    background: var(--quote-bg);
    border-left: 3px solid var(--accent);
    border-radius: 0 6px 6px 0;
    font-style: italic;
  }
  blockquote p:last-child { margin-bottom: 0; }

  code {
    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;
    font-size: .88em;
    background: var(--accent-soft);
    border-radius: 4px;
    padding: .1em .35em;
  }
  pre {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 1rem 1.25rem;
    overflow-x: auto;
  }
  pre code { background: none; padding: 0; font-size: .85rem; }

  table {
    width: 100%;
    margin: 1.5rem 0;
    border-collapse: collapse;
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-size: .85rem;
  }
  th, td {
    text-align: left;
    padding: .55rem .7rem;
    border-bottom: 1px solid var(--line);
    vertical-align: top;
  }
  thead th {
    background: var(--accent-soft);
    font-weight: 600;
    border-bottom: 2px solid var(--line);
  }
  tbody tr:last-child td { border-bottom: 0; }
  .tabel-scroll { overflow-x: auto; }

  .keten {
    margin: 1.4rem 0;
    padding: .85rem 1.1rem;
    background: var(--accent-soft);
    border: 1px solid var(--line);
    border-radius: 8px;
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-size: .88rem;
    line-height: 1.7;
    text-align: center;
  }
  .keten strong { color: var(--accent); }

  .label {
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-size: .78rem; letter-spacing: .06em; text-transform: uppercase;
    color: var(--muted); margin: 1.6rem 0 .4rem;
  }
  .label strong { font-weight: 600; }
  blockquote .keten {
    margin: 0 0 1rem; padding: 0; background: none; border: 0;
    font-family: inherit; font-size: inherit; text-align: left;
  }

  .opties {
    list-style: none;
    margin: 0 0 1rem;
    padding: .9rem 1.1rem;
    background: var(--accent-soft);
    border: 1px solid var(--line);
    border-radius: 8px;
  }
  .opties li { margin-bottom: .45rem; }
  .opties li:last-child { margin-bottom: 0; }
  .opties .letter {
    font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
    font-weight: 600; color: var(--accent); margin-right: .4rem;
  }
"""

PAGE = """\
<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}</style>
</head>
<body>
<div class="wrap">
{body}
</div>
</body>
</html>
"""

# ------------------------------------------------------------------- inline

RE_CODE = re.compile(r"`([^`]+)`")
RE_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
RE_BOLD = re.compile(r"\*\*(.+?)\*\*", re.S)
RE_ITALIC = re.compile(r"(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)", re.S)
RE_STRIKE = re.compile(r"~~(.+?)~~", re.S)


def inline(text: str) -> str:
    """Zet inline-Markdown om. Code-spans worden eerst geparkeerd zodat de
    inhoud ervan niet alsnog als vet of cursief wordt gelezen."""
    spans: list[str] = []

    def park(match: re.Match[str]) -> str:
        spans.append(html.escape(match.group(1), quote=False))
        return f"\x00{len(spans) - 1}\x00"

    text = RE_CODE.sub(park, text)
    text = html.escape(text, quote=False)
    text = RE_LINK.sub(
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', text
    )
    text = RE_BOLD.sub(r"<strong>\1</strong>", text)
    text = RE_ITALIC.sub(r"<em>\1</em>", text)
    text = RE_STRIKE.sub(r"<s>\1</s>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{spans[int(m.group(1))]}</code>", text)


# -------------------------------------------------------------------- blocks

RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RE_HR = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
RE_UL = re.compile(r"^\s*[-*+]\s+(.*)$")
RE_OL = re.compile(r"^\s*\d+[.)]\s+(.*)$")
RE_QUOTE = re.compile(r"^\s*>\s?(.*)$")
RE_FENCE = re.compile(r"^\s*(```|~~~)(.*)$")
RE_OPTION = re.compile(r"^([A-Z])\.\s+(.*)$")
RE_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
RE_TABLE_SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
RE_KETEN = re.compile(r"^(\*\*.+\*\*|[↓→].*)$")
RE_LABEL = re.compile(r"^\*\*([^*]+)\*\*$")


def is_block_start(line: str) -> bool:
    return bool(
        not line.strip()
        or RE_HEADING.match(line)
        or RE_HR.match(line)
        or RE_UL.match(line)
        or RE_OL.match(line)
        or RE_QUOTE.match(line)
        or RE_FENCE.match(line)
        or RE_TABLE_ROW.match(line)
    )


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def render_table(rows: list[str]) -> str:
    """Een pipe-tabel: eerste regel is de kop, tweede de scheidingsregel."""
    header, body = split_row(rows[0]), rows[2:]
    out = ['<div class="tabel-scroll">', "<table>", "<thead>", "  <tr>"]
    out += [f"    <th>{inline(cell)}</th>" for cell in header]
    out += ["  </tr>", "</thead>", "<tbody>"]
    for row in body:
        cells = split_row(row)
        cells += [""] * (len(header) - len(cells))
        out.append("  <tr>")
        out += [f"    <td>{inline(cell)}</td>" for cell in cells[: len(header)]]
        out.append("  </tr>")
    out += ["</tbody>", "</table>", "</div>"]
    return "\n".join(out)


def render_paragraph(lines: list[str]) -> str:
    """Een alinea. Regels die met 'A. ', 'B. ' beginnen worden als
    antwoordopties opgemaakt; overige regelovergangen worden <br>."""
    if len(lines) >= 2 and all(RE_OPTION.match(line) for line in lines):
        items = []
        for line in lines:
            letter, rest = RE_OPTION.match(line).groups()
            items.append(f'  <li><span class="letter">{letter}.</span>{inline(rest)}</li>')
        return '<ul class="opties">\n' + "\n".join(items) + "\n</ul>"
    # afleidingsketens: **A → B → C**, of meerdere regels met pijlen ertussen
    if any(arrow in line for line in lines for arrow in "→↓") and all(
        RE_KETEN.match(line.strip()) for line in lines
    ):
        return '<p class="keten">' + "<br>\n".join(inline(l.strip()) for l in lines) + "</p>"
    # een enkele, volledig vette regel is een label boven het blok dat volgt
    if len(lines) == 1 and RE_LABEL.match(lines[0].strip()):
        return '<p class="label">' + inline(lines[0].strip()) + "</p>"
    return "<p>" + "<br>\n".join(inline(line.strip()) for line in lines) + "</p>"


def render(lines: list[str], *, first_para_is_meta: bool = False) -> str:
    out: list[str] = []
    i = 0
    seen_h1 = False
    meta_pending = first_para_is_meta

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        fence = RE_FENCE.match(line)
        if fence:
            marker, info = fence.group(1), fence.group(2).strip()
            i += 1
            code: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith(marker):
                code.append(lines[i])
                i += 1
            i += 1  # sluitende fence
            cls = f' class="language-{html.escape(info, quote=True)}"' if info else ""
            body = html.escape("\n".join(code), quote=False)
            out.append(f"<pre><code{cls}>{body}</code></pre>")
            continue

        heading = RE_HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            text = inline(heading.group(2).strip())
            out.append(f"<h{level}>{text}</h{level}>")
            seen_h1 = seen_h1 or level == 1
            i += 1
            continue

        if RE_HR.match(line):
            out.append("<hr>")
            i += 1
            continue

        if RE_QUOTE.match(line):
            quoted: list[str] = []
            while i < len(lines) and (RE_QUOTE.match(lines[i]) or lines[i].strip()):
                match = RE_QUOTE.match(lines[i])
                quoted.append(match.group(1) if match else lines[i].strip())
                i += 1
            out.append("<blockquote>\n" + render(quoted) + "\n</blockquote>")
            continue

        if (
            RE_TABLE_ROW.match(line)
            and i + 1 < len(lines)
            and RE_TABLE_SEP.match(lines[i + 1])
        ):
            rows: list[str] = []
            while i < len(lines) and RE_TABLE_ROW.match(lines[i]):
                rows.append(lines[i])
                i += 1
            out.append(render_table(rows))
            continue

        if RE_UL.match(line) or RE_OL.match(line):
            ordered = bool(RE_OL.match(line))
            pattern = RE_OL if ordered else RE_UL
            items: list[str] = []
            while i < len(lines) and pattern.match(lines[i]):
                item = [pattern.match(lines[i]).group(1)]
                i += 1
                # doorlopende regels binnen hetzelfde item
                while i < len(lines) and lines[i].strip() and not is_block_start(lines[i]):
                    item.append(lines[i].strip())
                    i += 1
                items.append("  <li>" + inline(" ".join(item)) + "</li>")
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>\n" + "\n".join(items) + f"\n</{tag}>")
            continue

        para: list[str] = []
        while i < len(lines) and lines[i].strip() and not is_block_start(lines[i]):
            para.append(lines[i])
            i += 1
        if meta_pending and seen_h1:
            out.append('<p class="meta">' + "<br>\n".join(inline(p.strip()) for p in para) + "</p>")
            meta_pending = False
        else:
            out.append(render_paragraph(para))

    return "\n\n".join(out)


# ---------------------------------------------------------------- conversion


def convert(markdown: str, *, title: str | None = None, meta: bool = True) -> str:
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    # YAML-frontmatter overslaan als die er is
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                lines = lines[index + 1 :]
                break

    body = render(lines, first_para_is_meta=meta)

    if title is None:
        heading = next((RE_HEADING.match(l) for l in lines if RE_HEADING.match(l)), None)
        raw = heading.group(2).strip() if heading else "Lesmateriaal"
        title = html.escape(re.sub(r"[*`_]", "", raw), quote=False)

    return PAGE.format(title=title, css=CSS, body=body)


def convert_file(source: Path, destination: Path, *, meta: bool = True) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        convert(source.read_text(encoding="utf-8"), meta=meta), encoding="utf-8"
    )
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Zet Markdown-lesmateriaal om naar HTML.")
    parser.add_argument("input", type=Path, help="Een .md-bestand of een map met .md-bestanden")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Doelbestand, of doelmap wanneer de invoer een map is "
        "(standaard: naast het bronbestand)",
    )
    parser.add_argument("--stdout", action="store_true", help="Schrijf naar stdout in plaats van een bestand")
    parser.add_argument("--title", help="Overschrijf de paginatitel (alleen bij één bestand)")
    parser.add_argument(
        "--no-meta",
        action="store_true",
        help="Behandel de eerste alinea na de titel als gewone tekst in plaats van metadata",
    )
    args = parser.parse_args(argv)

    if not args.input.exists():
        parser.error(f"bestaat niet: {args.input}")

    if args.input.is_dir():
        sources = sorted(args.input.rglob("*.md"))
        if not sources:
            parser.error(f"geen .md-bestanden gevonden in {args.input}")
        if args.stdout:
            parser.error("--stdout werkt alleen met één bestand")
        out_dir = args.output or args.input
        for source in sources:
            target = out_dir / source.relative_to(args.input).with_suffix(".html")
            print(convert_file(source, target, meta=not args.no_meta))
        return 0

    markdown = args.input.read_text(encoding="utf-8")
    if args.stdout:
        # Windows-consoles staan standaard op cp1252; de lessen bevatten — en →.
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(convert(markdown, title=args.title, meta=not args.no_meta))
        return 0

    target = args.output or args.input.with_suffix(".html")
    if target.is_dir():
        target = target / args.input.with_suffix(".html").name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        convert(markdown, title=args.title, meta=not args.no_meta), encoding="utf-8"
    )
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
