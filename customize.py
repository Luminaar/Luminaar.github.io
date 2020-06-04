from pathlib import Path
import re


STYLE = (
    "<style>\n"
    "#main-header {font-variant-caps: small-caps;font-size: 1.2em;margin: 0.2em;}\n"
    "#main-header a {text-decoration: none;color: #ba3925;}\n"
    "#main-header a:hover {color: #822a1c;}\n"
)

HEADER = (
    '<body class="article">\n<div id="main-header">'
    '<a href="/">Back to Luminar.dev</a></div>'
)


def customize(filepath: Path):

    text = filepath.read_text()

    text = text.replace("<style>", STYLE)
    text = text.replace('<body class="article">', HEADER)
    text = re.sub(".*fonts.googleapis.*", "", text)

    filepath.write_text(text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[-1]
    else:
        sys.exit("Provide a filename")

    customize(Path(filename))
