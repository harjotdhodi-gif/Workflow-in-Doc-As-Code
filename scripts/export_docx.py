import os
import pathlib
import subprocess

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
SITE_DIR = REPO_ROOT / "site"
OUT_DIR = SITE_DIR / "downloads" / "docx"

EXCLUDE = {"downloads.md"}

def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for md in DOCS_DIR.rglob("*.md"):
        if md.name in EXCLUDE:
            continue

        rel = md.relative_to(DOCS_DIR)
        out = OUT_DIR / rel.with_suffix(".docx")
        out.parent.mkdir(parents=True, exist_ok=True)

        # Pandoc: Markdown -> DOCX
        run(["pandoc", str(md), "-o", str(out)])

    print(f"DOCX exported to: {OUT_DIR}")

if __name__ == "__main__":
    main()

