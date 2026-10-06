# -*- coding: utf-8 -*-
"""Copy prototype 10/10-v2/11 vao demo-github-pages (khong gan banner top — tranh cat layout h-screen)."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLAN = HERE.parent
SRC = {
    "console.html": PLAN / "10-prototype-bdsc-console.html",
    "console-v2.html": PLAN / "10-prototype-bdsc-console-v2.html",
    "mobile.html": PLAN / "11-prototype-mobile-ktv.html",
    "mobile-v2.html": PLAN / "11-prototype-mobile-ktv-v2.html",
}


def strip_docs_backbar(t: str) -> str:
    t = re.sub(r'<div class="docs-backbar"[^>]*>.*?</div>\s*', "", t, count=1, flags=re.S)
    t = re.sub(
        r'<div style="position:sticky;top:0;z-index:9999;background:#0b1f17[^"]*"[^>]*>.*?</div>\s*',
        "",
        t,
        count=1,
        flags=re.S,
    )
    return t


def main():
    for dest_name, src in SRC.items():
        if not src.exists():
            print("Skip missing", src.name)
            continue
        t = strip_docs_backbar(src.read_text(encoding="utf-8"))
        out = HERE / dest_name
        out.write_text(t, encoding="utf-8")
        print("Wrote", out.name, "from", src.name, "·", len(t), "chars")


if __name__ == "__main__":
    main()
