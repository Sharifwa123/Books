# Cover

`cover-front.svg` is the source; `cover-front.png` (1600 x 2560 pixels, 5:8) is rendered from it. This is a **draft typographic cover** made for the book: title, subtitle, author, the SHARIF TECHNOLOGIES brand line and the slogan, with a commit-and-branch graph. It states no ISBN, publisher, price or award. The author or publisher may replace it with a designed cover of their own; the builders use `cover-front.png` if it exists.

Only a front cover exists. A back cover, spine and print-wrap cover need the trim size, page count, paper and printer's specification, and an ISBN barcode once an ISBN is assigned; none of these is decided.

To render the PNG again from the SVG (headless Chromium, then crop to the exact size):

```
chrome --headless --no-sandbox --hide-scrollbars --force-device-scale-factor=1 --window-size=1600,2800 --screenshot=/tmp/cover-big.png file://$PWD/cover-front.svg
python3 -c "from PIL import Image; Image.open('/tmp/cover-big.png').crop((0,0,1600,2560)).save('cover-front.png', optimize=True)"
```
