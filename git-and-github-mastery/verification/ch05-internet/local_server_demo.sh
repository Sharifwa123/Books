#!/usr/bin/env bash
# Client and server on ONE computer: a tiny web server (Python's built-in) and curl as the client.
# Needs python3 and curl. Prints a normalised transcript (Date/Server headers removed) so it can be compared.
set -u
W=$(mktemp -d); cd "$W"
printf '<h1>Sunrise Bakery</h1>\n' > index.html
PORT=8765
python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
SP=$!
trap 'kill $SP 2>/dev/null; rm -rf "$W"' EXIT
for i in 1 2 3 4 5 6 7 8 9 10; do curl -s -o /dev/null "http://127.0.0.1:$PORT/" && break; sleep 0.3; done
OK=$(curl -si "http://127.0.0.1:$PORT/index.html" | tr -d '\r'); BAD=$(curl -si "http://127.0.0.1:$PORT/missing.html" | tr -d '\r')
echo '$ curl -i http://127.0.0.1:8765/index.html'; echo "$OK" | grep -v -i -E '^(Date|Server|Last-Modified):'
echo '$ curl -i http://127.0.0.1:8765/missing.html'; echo "$BAD" | grep -E '^HTTP/'
# Assertions are case-insensitive and version-tolerant (header spelling and HTTP version differ between Python releases)
rc=0
echo "$OK"  | head -1 | grep -qE '^HTTP/[0-9.]+ 200' && echo "PASS  found page -> status 200" || { echo "FAIL  status 200"; rc=1; }
echo "$OK"  | grep -qi '^content-length: 24' && echo "PASS  Content-Length is 24 bytes" || { echo "FAIL  content-length"; rc=1; }
echo "$OK"  | grep -q 'Sunrise Bakery' && echo "PASS  body returned" || { echo "FAIL  body"; rc=1; }
echo "$BAD" | head -1 | grep -qE '^HTTP/[0-9.]+ 404' && echo "PASS  missing page -> status 404" || { echo "FAIL  status 404"; rc=1; }
exit $rc
