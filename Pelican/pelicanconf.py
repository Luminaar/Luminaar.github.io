from pelicanconf import *

AUTHOR = "Max K."
SITENAME = "Max K. Luminar"
SITEURL = "http://localhost:8000"
RELATIVE_URLS = True

TYPOGRIFY = True

PATH = "content"

TIMEZONE = "Europe/Prague"

DEFAULT_LANG = "en"

STATIC_PATHS = ["images", "assets", "extra/CNAME"]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Theme
THEME = "attila"
HEADER_COVER = "/assets/images/default-bg.jpg"

# URLs
ARTICLE_URL = "notes/{date:%m}-{slug}/"
ARTICLE_SAVE_AS = "notes/{date:%m}-{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
