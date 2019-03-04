from pelicanconf import *

AUTHOR = "Max K."
SITENAME = "Max K. Luminar"
SITEURL = "http://localhost:8000"
RELATIVE_URLS = True

TYPOGRIFY = True

PATH = "content"

TIMEZONE = "Europe/Prague"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

DEFAULT_LANG = "en"

STATIC_PATHS = ["images", "assets", "extra/CNAME", "assets/images/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "assets/images/favicon.ico": {"path": "favicon.ico"},
}

DEFAULT_METADATA = {"author": "max"}

# Theme
THEME = "attila"
HEADER_COVER = "/assets/images/default-bg.jpg"


# Author
AUTHORS_BIO = {
    "max": {
        "name": "Max K.",
        "cover": "/assets/images/default-bg.jpg",
        "image": "/assets/images/avatar.jpg",
        "location": "Prague",
        "bio": "I'm a backend engineer at Avast. I work mostly with Python, Scala and Kubernetes.",
        "twitter": "Luminar_",
        "github": "Luminaar",
    }
}

# URLs
ARTICLE_URL = "notes/{date:%y}-{date:%m}-{slug}/"
ARTICLE_SAVE_AS = "notes/{date:%y}-{date:%m}-{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
