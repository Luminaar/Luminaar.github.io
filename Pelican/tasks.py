# -*- coding: utf-8 -*-

import os
import shutil
import sys
from datetime import datetime

from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {"deploy_path": "output", "publish_path": "..", "port": 8000}


@task
def clean(_):
    """Remove generated files"""
    path = str(CONFIG["deploy_path"])
    if os.path.isdir(path):
        shutil.rmtree(path)
        os.makedirs(path)


@task
def build(c):
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
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run(f"pelican -s publishconf.py -o {CONFIG['publish_path']}")


@task
def publish(c):
    """Publish to production via rsync"""

    now = datetime.now().strftime("%Y-%m-%d")

    clean(c)

    c.run(f"pelican -s publishconf.py -o {CONFIG['publish_path']}")
    with c.cd(CONFIG["publish_path"]):
        c.run("git add .")
        c.run(f"git commit -m 'Published on {now}'")
        c.run("git push")
