#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bryan Davis'
SITENAME = u'bd808.com'
SITESUBTITLE = u'FOSS in, FOSS out: software, process and operations'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'GMT'
DEFAULT_LANG = u'en'

INDEX_URL = 'blog/'
INDEX_SAVE_AS = 'blog/index.html'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARCHIVES_URL = 'blog/archives/'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'

TAGS_URL = 'blog/tag/'
TAGS_SAVE_AS = 'blog/tag/index.html'

CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ['index', 'tags', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['index', 'archives']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_CATEGORY = 'blog'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

STATIC_PATHS = [
    '.nojekyll',
    '.well-known',
    'CNAME',
    'favicon.png',
    'robots.txt',
    'static',
]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MENUITEMS = [
    ('Home', '/'),
    ('Blog', '/blog/'),
]

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'
BOOTSTRAP_FLUID = True
CUSTOM_CSS = 'static/site.css'

# BANNER = True
# BANNER_ALL_PAGES = True
# BANNER_SUBTITLE = SITESUBTITLE

ABOUT_ME = u"""
Code and ramblings from Bryan Davis, coder, software architect, and highly opinionated geek.
"""
AVATAR = 'static/6af4be9e5e433d21909a0eb60fc258bc.png'
CC_LICENSE = 'CC-BY-SA'

PYGMENTS_STYLE = 'solarizeddark'

USE_PAGER = True
DISPLAY_BREADCRUMBS = False
FAVICON = 'favicon.png'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True

TWITTER_CARDS = True
TWITTER_USERNAME = 'bd808'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'i18n_subsites',
    'liquid_tags.img',
    'summary',
    'tag_cloud',
]
JINJA_EXTENSIONS = [
    'jinja2.ext.i18n',
]
