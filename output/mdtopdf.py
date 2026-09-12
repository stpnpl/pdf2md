#!/usr/bin/env python3
"""
Markdown to PDF Converter - GitHub Style
Converts all Markdown files in the current directory to PDF format
with GitHub-flavored styling for maximum readability.

Uses Playwright (headless Chromium) for accurate HTML/CSS rendering.
"""

import base64
import mimetypes
import os
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Error: markdown library not found.")
    print("Please install it using: pip install markdown")
    sys.exit(1)

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: playwright library not found.")
    print("Please install it using: pip install playwright && playwright install chromium")
    sys.exit(1)


# GitHub-inspired CSS for PDF rendering
GITHUB_CSS = """
@page {
    size: A4;
    margin: 1.2cm 1.5cm;
}

@page :first {
    margin-top: 1.2cm;
}

@page :left {
    margin-left: 1.5cm;
    margin-right: 1.2cm;
}

@page :right {
    margin-left: 1.2cm;
    margin-right: 1.5cm;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial,
                 sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 13px;
    line-height: 1.45;
    color: #1f2328;
    max-width: 100%;
    word-wrap: break-word;
}

/* Headings */
h1 {
    font-size: 1.6em;
    font-weight: 600;
    padding-bottom: 0.2em;
    border-bottom: 1px solid #d1d9e0;
    margin-top: 10px;
    margin-bottom: 6px;
    page-break-after: avoid;
    color: #1f2328;
}

h2 {
    font-size: 1.3em;
    font-weight: 600;
    padding-bottom: 0.2em;
    border-bottom: 1px solid #d1d9e0;
    margin-top: 10px;
    margin-bottom: 6px;
    page-break-after: avoid;
    color: #1f2328;
}

h3 {
    font-size: 1.1em;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 6px;
    page-break-after: avoid;
    color: #1f2328;
}

h4 {
    font-size: 1em;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 6px;
    page-break-after: avoid;
    color: #1f2328;
}

h5 {
    font-size: 0.875em;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 6px;
    page-break-after: avoid;
    color: #1f2328;
}

h6 {
    font-size: 0.85em;
    font-weight: 600;
    color: #656d76;
    margin-top: 10px;
    margin-bottom: 6px;
    page-break-after: avoid;
}

/* Paragraphs */
p {
    margin-top: 0;
    margin-bottom: 6px;
}

/* Links */
a {
    color: #0969da;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Strong and emphasis */
strong {
    font-weight: 600;
}

em {
    font-style: italic;
}

/* Horizontal rules */
hr {
    height: 0.25em;
    padding: 0;
    margin: 10px 0;
    background-color: #d1d9e0;
    border: 0;
}

/* Lists */
ul, ol {
    padding-left: 2em;
    margin-top: 0;
    margin-bottom: 6px;
}

ul ul, ol ul, ul ol, ol ol {
    margin-top: 0;
    margin-bottom: 0;
}

li {
    margin-bottom: 2px;
    word-wrap: break-word;
}

li + li {
    margin-top: 0.1em;
}

li > p {
    margin-top: 6px;
}

/* Task lists */
li input[type="checkbox"] {
    margin: 0 0.2em 0.25em -1.6em;
    vertical-align: middle;
}

/* Blockquotes */
blockquote {
    padding: 0 1em;
    color: #656d76;
    border-left: 0.25em solid #d1d9e0;
    margin: 0 0 6px 0;
}

blockquote > :first-child {
    margin-top: 0;
}

blockquote > :last-child {
    margin-bottom: 0;
}

/* Code - inline */
code {
    padding: 0.2em 0.4em;
    margin: 0;
    font-size: 85%;
    background-color: rgba(175, 184, 193, 0.2);
    border-radius: 6px;
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas,
                 "Liberation Mono", monospace;
    word-wrap: break-word;
}

/* Code - blocks */
pre {
    padding: 10px;
    overflow: auto;
    font-size: 85%;
    line-height: 1.4;
    background-color: #f6f8fa;
    border-radius: 6px;
    margin-top: 0;
    margin-bottom: 6px;
    word-wrap: normal;
    page-break-inside: avoid;
}

pre code {
    display: inline;
    padding: 0;
    margin: 0;
    overflow: visible;
    line-height: inherit;
    word-wrap: normal;
    background-color: transparent;
    border: 0;
    font-size: 100%;
}

/* Tables - GitHub style */
table {
    border-spacing: 0;
    border-collapse: collapse;
    margin-top: 0;
    margin-bottom: 6px;
    width: 100%;
    font-size: 12px;
    page-break-inside: avoid;
}

table th,
table td {
    padding: 4px 10px;
    border: 1px solid #d1d9e0;
    text-align: left;
}

table th {
    font-weight: 600;
    background-color: #f6f8fa;
}

table tr {
    background-color: #ffffff;
    border-top: 1px solid #d1d9e0;
}

table tr:nth-child(2n) {
    background-color: #f6f8fa;
}

/* Empty table cells */
table td:empty::after {
    content: "\\00a0";
}

/* Images */
img {
    max-width: 100%;
    box-sizing: border-box;
    border-radius: 6px;
}

/* Syntax highlighting - GitHub dark-ish theme for code blocks */
.highlight pre {
    background-color: #f6f8fa;
}

/* Pygments syntax highlighting - GitHub theme */
.highlight .hll { background-color: #f6f8fa }
.highlight .c { color: #6a737d; font-style: italic }
.highlight .err { color: #cf222e }
.highlight .k { color: #8250df; font-weight: bold }
.highlight .o { color: #8250df; font-weight: bold }
.highlight .cm { color: #6a737d; font-style: italic }
.highlight .cp { color: #8250df; font-weight: bold }
.highlight .c1 { color: #6a737d; font-style: italic }
.highlight .cs { color: #8250df; font-weight: bold }
.highlight .gd { color: #cf222e; background-color: #ffebe9 }
.highlight .ge { font-style: italic }
.highlight .gi { color: #116329; background-color: #dafbe1 }
.highlight .gs { font-weight: bold }
.highlight .gu { color: #8250df; font-weight: bold }
.highlight .kc { color: #0550ae; font-weight: bold }
.highlight .kd { color: #0550ae; font-weight: bold }
.highlight .kn { color: #8250df; font-weight: bold }
.highlight .kp { color: #0550ae; font-weight: bold }
.highlight .kr { color: #0550ae; font-weight: bold }
.highlight .kt { color: #953800; font-weight: bold }
.highlight .m { color: #0550ae }
.highlight .s { color: #0a3069 }
.highlight .na { color: #0550ae }
.highlight .nb { color: #0550ae }
.highlight .nc { color: #953800; font-weight: bold }
.highlight .no { color: #0550ae }
.highlight .nd { color: #8250df; font-weight: bold }
.highlight .ni { color: #24292f; font-weight: bold }
.highlight .ne { color: #953800; font-weight: bold }
.highlight .nf { color: #8250df; font-weight: bold }
.highlight .nl { color: "#0550ae"; font-weight: bold }
.highlight .nn { color: #953800; font-weight: bold }
.highlight .nt { color: #116329; font-weight: bold }
.highlight .nv { color: #953800 }
.highlight .ow { color: #8250df; font-weight: bold }
.highlight .w { color: #eaeef2 }
.highlight .mb { color: #0550ae }
.highlight .mf { color: #0550ae }
.highlight .mh { color: #0550ae }
.highlight .mi { color: #0550ae }
.highlight .mo { color: #0550ae }
.highlight .sa { color: #0a3069 }
.highlight .sb { color: #0a3069 }
.highlight .sc { color: #0a3069 }
.highlight .dl { color: #0a3069 }
.highlight .sd { color: #0a3069 }
.highlight .s2 { color: #0a3069 }
.highlight .se { color: #0a3069 }
.highlight .sh { color: #0a3069 }
.highlight .si { color: #0a3069 }
.highlight .sx { color: #0a3069 }
.highlight .sr { color: #0a3069 }
.highlight .s1 { color: #0a3069 }
.highlight .ss { color: #0550ae }
.highlight .bp { color: #0550ae }
.highlight .fm { color: #8250df; font-weight: bold }
.highlight .vc { color: #953800 }
.highlight .vg { color: #953800 }
.highlight .vi { color: #953800 }
.highlight .vm { color: #953800; font-weight: bold }
.highlight .il { color: #0550ae }

/* Special formatting for document headers */
h1:first-of-type {
    font-size: 1.6em;
    text-align: center;
    border-bottom: 2px solid #0969da;
    padding-bottom: 0.3em;
    margin-bottom: 0.5em;
    color: #1f2328;
}

/* Definition lists */
dl {
    padding: 0;
    margin-top: 0;
    margin-bottom: 6px;
}

dt {
    padding: 0;
    margin-top: 6px;
    font-size: 1em;
    font-style: italic;
    font-weight: 600;
}

dd {
    padding: 0 16px;
    margin-bottom: 6px;
}

/* Strikethrough */
del {
    text-decoration: line-through;
}

/* Avoid orphans/widows */
p, li, td, th {
    orphans: 3;
    widows: 3;
}

/* Keep table rows together */
tr {
    page-break-inside: avoid;
}

/* Prevent page breaks in the middle of code blocks */
pre, code {
    page-break-inside: avoid;
}

/* Ensure headers don't appear at the bottom of a page */
h1, h2, h3, h4, h5, h6 {
    page-break-after: avoid;
}

/* Keep lists together when possible */
ul, ol {
    page-break-inside: auto;
}
"""


# Optimized convert_md_to_pdf function
def convert_md_to_pdf(md_path, output_folder, browser):
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        md_name = Path(md_path).stem
        output_dir = output_folder if output_folder else Path(md_path).parent
        pdf_path = output_dir / f"{md_name}.pdf"

        extensions = ['tables', 'fenced_code', 'codehilite', 'toc', 'sane_lists', 'smarty', 'attr_list', 'def_list', 'md_in_html', 'admonition']
        md = markdown.Markdown(extensions=extensions, output_format='html')
        html_content = md.convert(md_content)

        # Fix 1: page.set_content() has no base URL and headless Chromium
        # blocks file:// subresources loaded from it, so relative asset links
        # (e.g. assets/...) render as broken-image icons. Embed local images
        # as base64 data URIs so the PDF is self-contained.
        base_dir = Path(md_path).parent.resolve()

        def _embed(m: re.Match) -> str:
            attr, rel = m.group(1), m.group(2)
            target = (base_dir / rel).resolve()
            try:
                data = target.read_bytes()
            except OSError:
                return m.group(0)  # leave as-is; visibly broken, never silent
            mime, _ = mimetypes.guess_type(str(target))
            b64 = base64.b64encode(data).decode("ascii")
            return f'{attr}="data:{mime or "application/octet-stream"};base64,{b64}"'

        html_content = re.sub(
            r'(src|href)="(?!https?:|data:|file:|#|mailto:)([^"]+)"',
            _embed,
            html_content,
        )

        # Fix 2: Chromium prints <details> blocks collapsed (only <summary>
        # visible). Expand them so long descriptions reach the PDF.
        html_content = html_content.replace("<details>", "<details open>")

        full_html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
        <title>{md_name}</title><style>{GITHUB_CSS}</style></head>
        <body>{html_content}</body></html>"""

        # Reuse the existing browser instance
        page = browser.new_page()
        page.set_content(full_html, wait_until='networkidle')
        page.pdf(
            path=str(pdf_path), format='A4',
            margin={'top': '1.2cm', 'bottom': '1.2cm', 'left': '1.5cm', 'right': '1.2cm'},
            print_background=True, display_header_footer=False
        )
        page.close() # Close the page, keep the browser alive
        
        print(f"  [OK] Converted: {md_path.name} -> {pdf_path.name}")
        return True
    except Exception as e:
        print(f"  [ERROR] Processing {md_path.name}: {str(e)}")
        return False

def main():
    current_dir = Path.cwd()
    md_files = sorted(current_dir.glob('*.md'))
    if not md_files:
        print("No Markdown files found.")
        return

    print(f"Found {len(md_files)} Markdown file(s). Booting Chromium...")
    
    # Launch browser ONCE for the entire batch
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        successful = 0
        for md_file in md_files:
            pdf_path = md_file.with_suffix('.pdf')
            if pdf_path.exists():
                print(f"  [SKIP] Skipped: {pdf_path.name} (already exists)")
                continue
            if convert_md_to_pdf(md_file, None, browser):
                successful += 1
                
        browser.close() # Close browser after all files are done
        
    print(f"\n[DONE] Conversion complete! {successful}/{len(md_files)} successful.")


if __name__ == "__main__":
    main()
