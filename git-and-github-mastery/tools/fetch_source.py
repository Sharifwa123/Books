#!/usr/bin/env python3
"""Fetch an official source over HTTPS, save it under a cache folder, and record url, time, size and sha256
in research/sources-manifest.csv, so that a ledger row can cite evidence that can be re-checked.
usage: fetch_source.py URL [--out DIR]   (default DIR: $SOURCE_CACHE or /tmp/book-sources)"""
import csv, hashlib, os, sys, time, urllib.request, urllib.error
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
manifest = os.path.join(root, "research", "sources-manifest.csv")
args = sys.argv[1:]
out = os.environ.get("SOURCE_CACHE", "/tmp/book-sources")
if "--out" in args:
    i = args.index("--out"); out = args[i + 1]; del args[i:i + 2]
if len(args) != 1: sys.exit(__doc__)
url = args[0]
req = urllib.request.Request(url, headers={"User-Agent": "book-verification/1.0"})
try:
    data = urllib.request.urlopen(req, timeout=60).read()
except urllib.error.HTTPError as e:
    sys.exit(f"HTTP {e.code} for {url}")
except Exception as e:
    sys.exit(f"failed: {e} for {url}")
sha = hashlib.sha256(data).hexdigest()
name = url.split("://", 1)[1].replace("/", "__")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, name)
open(path, "wb").write(data)
new = not os.path.exists(manifest)
rows = []
if not new:
    rows = list(csv.reader(open(manifest)))
if not any(r[0] == url and r[3] == sha for r in rows[1:]):
    with open(manifest, "a", newline="") as f:
        w = csv.writer(f)
        if new: w.writerow(["url", "fetched_utc", "bytes", "sha256"])
        w.writerow([url, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), len(data), sha])
print(path)
