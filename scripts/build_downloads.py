import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"

EXCLUDE = {"downloads.md", "index.md"}

def md_title(path: pathlib.Path) -> str:
    # Use filename as title fallback
    return path.stem.replace("-", " ").replace("_", " ").title()

def main():
    items = []
    for md in sorted(DOCS_DIR.rglob("*.md")):
        if md.name in EXCLUDE:
            continue
        rel = md.relative_to(DOCS_DIR)
        name = md_title(md)
        # Where files will end up in GitHub Pages:
        # PDFs: /pdf/<same-path>.pdf (from mkdocs-pdf-export-plugin)
        # DOCX: /downloads/docx/<same-path>.docx (from our pandoc export)
        pdf_link = f"/pdf/{rel.with_suffix('.pdf')}".replace("\\", "/")
        docx_link = f"/downloads/docx/{rel.with_suffix('.docx')}".replace("\\", "/")
        html_link = f"/{rel.with_suffix('')}".replace("\\", "/")

        items.append((name, html_link, pdf_link, docx_link))

    out = DOCS_DIR / "downloads.md"
    lines = [
        "# Downloads",
        "",
        "Download the documentation in multiple formats:",
        "",
        "| Page | HTML | PDF | DOCX |",
        "|---|---|---|---|",
    ]
    for name, html_link, pdf_link, docx_link in items:
        lines.append(f"| {name} | [View]({html_link}) | [PDF]({pdf_link}) | [DOCX]({docx_link}) |")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote: {out}")

if __name__ == "__main__":
    main()
