from pathlib import Path


HEADER = (
    '<body class="article">\n<div id="main-header">'
    '<a href="/">⇽ back to luminar.dev</a></div>'
)


def customize(filepath: Path):

    text = filepath.read_text()

    text = text.replace('<body class="article">', HEADER)

    filepath.write_text(text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[-1]
    else:
        sys.exit("Provide a filename")

    customize(Path(filename))
