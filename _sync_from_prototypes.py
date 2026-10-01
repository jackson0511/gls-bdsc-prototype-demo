# -*- coding: utf-8 -*-
"""Copy prototype 10/11 vao demo-github-pages va gan banner demo."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLAN = HERE.parent
SRC = {
    "console.html": PLAN / "10-prototype-bdsc-console.html",
    "mobile.html": PLAN / "11-prototype-mobile-ktv.html",
}
BANNER = (
    '<div style="position:sticky;top:0;z-index:9999;background:#0b1f17;color:#dcece5;'
    'font:13px/1.4 system-ui,sans-serif;padding:8px 14px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;'
    'border-bottom:1px solid rgba(255,255,255,.08)">'
    '<a href="index.html" style="color:#fff;font-weight:700;text-decoration:none">← Demo BD/SC</a>'
    '<span style="opacity:.75">Prototype · dữ liệu mẫu trên trình duyệt</span>'
    '<span style="flex:1"></span>'
    '<a href="console.html" style="color:#cfe3da;text-decoration:none">Console</a>'
    '<a href="mobile.html" style="color:#cfe3da;text-decoration:none">Mobile</a>'
    "</div>\n"
)


def main():
    for dest_name, src in SRC.items():
        t = src.read_text(encoding="utf-8")
        t = re.sub(r'<div class="docs-backbar"[^>]*>.*?</div>\s*', "", t, count=1, flags=re.S)
        t = re.sub(
            r'<div style="position:sticky;top:0;z-index:9999;background:#0b1f17[^"]*"[^>]*>.*?</div>\s*',
            "",
            t,
            count=1,
            flags=re.S,
        )
        t = re.sub(r"(<body[^>]*>)", r"\1\n" + BANNER, t, count=1, flags=re.I)
        out = HERE / dest_name
        out.write_text(t, encoding="utf-8")
        print("Wrote", out.name, "from", src.name)


if __name__ == "__main__":
    main()
