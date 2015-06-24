#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"James Mills"
SITENAME = u"mio-lang"
SITEURL = ""

THEME = "pelican-bootstrap3"

PATH = "content"

TIMEZONE = "Australia/Brisbane"

DEFAULT_LANG = u"en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Documentation", "https://docs.mio-lang.org/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "http://github.com/mio-lang/mio"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {
        "path": "CNAME"
    },
}
