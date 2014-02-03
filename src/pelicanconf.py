#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = u'dsigned.gr'
AUTHOR = u'dsigned.gr'
AUTHOR_BIO= 'I am a software engineer based in Athens, Greece.'

SITEURL = ''

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = u'en'

THEME= 'theme'
PATH = 'content'
PAGE_DIR = 'pages'

#READERS = {'html': None}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY=True
#DIRECT_TEMPLATES = ('index','page',)

DISPLAY_PAGES_ON_MENU = False
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''


# Blogroll
LINKS =  (
        ('Google+', 'http://github.com/nikosk'),
		('Github', 'http://github.com/nikosk'),
	    ('StackOverflow', 'http://stackoverflow.com/users/56663/javito'),
	    ('Twitter', 'http://twitter.com/nikos_k'),
    )

PLUGIN_PATH = '../../pelican-plugins'
PLUGINS = ['assets']
