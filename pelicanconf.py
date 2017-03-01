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

TAG_URL = 'blog/tags/{slug}/'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags/'
TAGS_SAVE_AS = 'blog/tags/index.html'

CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ['index', 'tags', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['index', 'archives']

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_CATEGORY = 'blog'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 5

STATIC_PATHS = [
    '.nojekyll',
    '.well-known',
    'CNAME',
    'favicon.png',
    'README.md',
    'robots.txt',
    'static',
]
STATIC_EXCLUDE_SOURCES = False
PAGE_EXCLUDES = [
    'README.md',
]
ARTICLE_EXCLUDES = PAGE_EXCLUDES

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

PYGMENTS_STYLE = 'solarizedlight'

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

GITHUB_COMMENTS = True
GITHUB_USER = 'bd808'
GITHUB_REPO = 'bd808.github.com'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'pages': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'monthly',
        'indexes': 'daily',
    },
    'exclude': ['blog/tag/', 'blog/category/'],
}

TAG_CLOUD_SORTING = 'alphabetically'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'better_codeblock_line_numbering',
    'i18n_subsites',
    'liquid_tags.img',
    'sitemap',
    'summary',
    'tag_cloud',
]
JINJA_EXTENSIONS = [
    'jinja2.ext.i18n',
]
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}