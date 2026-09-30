#!/usr/bin/env bash
# Validates PDFs with veraPDF 1.28.2 (fetched from Maven Central with Maven; needs Java and Maven).
# Profile: PDF/UA-1 by default; PDF/A-2b for a file whose name contains "pdfa-2b". Set FLAVOUR to force one.
# usage: verapdf_check.sh FILE.pdf...   Exit status 1 if any file is not compliant.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
work="${VERAPDF_DIR:-/tmp/verapdf}"
if [ ! -d "$work/libs" ]; then
  mkdir -p "$work"; cp "$here/verapdf/pom.xml" "$work/pom.xml"
  (cd "$work" && mvn -q -B dependency:copy-dependencies -DoutputDirectory=libs)
fi
rc=0
for f in "$@"; do
  fl="${FLAVOUR:-ua1}"; case "$f" in *pdfa-2b*) fl="${FLAVOUR:-2b}";; esac
  out="$(java -Xmx3g -cp "$work/libs/*" org.verapdf.apps.GreenfieldCliWrapper --flavour "$fl" --format text "$f" 2>&1 | grep -v '^Picked up')"
  echo "$out"
  case "$out" in PASS*) ;; *) rc=1;; esac
done
exit $rc
