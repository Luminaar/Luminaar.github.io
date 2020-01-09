# -*- coding: utf-8 -*-

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from typing import List, Optional

from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {"deploy_path": "output", "publish_path": "..", "port": 8000}


def article_header(
    title: str,
    summary: Optional[str] = None,
    category: Optional[str] = None,
    tags: Optional[List[str]] = None,
):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not tags:
        tags = []
    return dedent(
        f"""\
        Title: {title}
        Date: {date}
        Category: {category}
        Tags: {', '.join(tags)}
        Summary: {summary}"""
    )


@task
def new_article(_):
    """Create a new article."""

    file_name = input("File name: ")
    if not file_name:
        print("File name is required")
        return

    title = input("Title: ")
    if not file_name:
        print("Title is required")
        return

    summary = input("Summary (optional): ")
    category = input("Category (optional): ")
    tags = input("Comma-separated tags (optional): ").split(",")

    script_path = Path(os.path.dirname(os.path.abspath(__file__)))
    article_path = script_path / "content" / (file_name + ".md")
    article_path.write_text(article_header(title, summary, category, tags))


@task
def clean(_):
    """Remove generated files"""
    path = str(CONFIG["deploy_path"])
    if os.path.isdir(path):
        shutil.rmtree(path)
        os.makedirs(path)


@task
def preview(c):
    """Build local version of site"""
    c.run(f"pelican -s pelicanconf.py -o {CONFIG['deploy_path']}")


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run(f"pelican -d -s pelicanconf.py -o {CONFIG['deploy_path']}")


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run(f"pelican -r -s pelicanconf.py -o {CONFIG['deploy_path']}")


@task
def serve(_):
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def build(c):
    """Build production version of site"""
    c.run(f"pelican -s publishconf.py -o {CONFIG['publish_path']}")


@task
def publish(c):
    """Publish to production via rsync"""

    now = datetime.now().strftime("%Y-%m-%d")

    clean(c)
    build(c)

    with c.cd(CONFIG["publish_path"]):
        c.run("git add .")
        c.run(f"git commit -m 'Published on {now}'")
        c.run("git push")
