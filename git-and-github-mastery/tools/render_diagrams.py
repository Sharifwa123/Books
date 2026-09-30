#!/usr/bin/env python3
"""Pre-renders every ```mermaid block in the manuscript to a static SVG (needs Node with the 'mermaid' npm package and the
Chromium that ships with Playwright). Output: publishing/build/diagrams/<hash>.svg, keyed by the hash of the diagram source,
so unchanged diagrams are not re-rendered. Text labels use SVG <text> (htmlLabels off) so that the PDF renderer can draw them.
Usage: render_diagrams.py [--mermaid-dir DIR]   (DIR contains node_modules/mermaid; default $MERMAID_DIR or /tmp/mm)"""
import glob, hashlib, html, os, re, subprocess, sys, tempfile
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
mdir = os.environ.get("MERMAID_DIR", "/tmp/mm")
if "--mermaid-dir" in sys.argv: mdir = sys.argv[sys.argv.index("--mermaid-dir") + 1]
lib = os.path.join(mdir, "node_modules", "mermaid", "dist", "mermaid.min.js")
import shutil
chrome = (os.environ.get("CHROME") or next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))), None)
          or shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser") or "chromium")
outdir = os.path.join(root, "publishing", "build", "diagrams"); os.makedirs(outdir, exist_ok=True)
def key(code): return hashlib.sha1(code.encode()).hexdigest()[:12]
blocks = {}
for f in sorted(glob.glob(os.path.join(root, "manuscript", "**", "*.md"), recursive=True)):
    for m in re.finditer(r"```mermaid\n(.*?)```", open(f, encoding="utf-8").read(), flags=re.S):
        blocks[key(m.group(1))] = m.group(1)
force = "--force" in sys.argv
todo = {k: c for k, c in blocks.items() if force or not os.path.exists(os.path.join(outdir, k + ".svg"))}
print(len(blocks), "diagrams;", len(todo), "to render")
if todo:
    body = "".join(f'<div id="d{i}" class="wrap"><pre class="mermaid">{html.escape(c)}</pre></div>' for i, c in enumerate(todo.values()))
    page = f'<!doctype html><html><body>{body}<script src="file://{lib}"></script><script>mermaid.initialize({{startOnLoad:true,theme:"neutral",htmlLabels:false,flowchart:{{htmlLabels:false}},securityLevel:"strict"}});</script></body></html>'
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as t: t.write(page)
    dom = subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files", "--virtual-time-budget=20000", "--dump-dom", "file://" + t.name], capture_output=True, text=True, timeout=180).stdout
    svgs = re.findall(r"<svg\b.*?</svg>", dom, flags=re.S)
    if len(svgs) != len(todo): sys.exit(f"expected {len(todo)} SVGs, got {len(svgs)}")
    for (k, c), svg in zip(todo.items(), svgs):
        vb = re.search(r'viewBox="([\d. -]+)"', svg).group(1).split()
        w, h = float(vb[2]), float(vb[3])
        svg = re.sub(r'\swidth="100%"', f' width="{w:.0f}" height="{h:.0f}"', svg, count=1)
        svg = re.sub(r'style="max-width: [\d.]+px;?"', "", svg, count=1)
        if "<br>" in svg: svg = svg.replace("<br>", "<br/>")
        open(os.path.join(outdir, k + ".svg"), "w", encoding="utf-8").write(svg)
        print("rendered", k)
