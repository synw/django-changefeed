# -*- coding: utf-8 -*-

import importlib
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


RETHINKDB_HOST = getattr(settings, 'RETHINKDB_HOST', 'localhost')
RETHINKDB_PORT = getattr(settings, 'RETHINKDB_PORT', 28015)

LISTEN = getattr(settings, 'CHANGEFEED_LISTEN', True)

try:
    SITE_SLUG = getattr(settings, 'SITE_SLUG', 'site')
except ImportError:
    raise ImproperlyConfigured(u"Changeflow; a SITE_SLUG setting is required")

DATABASE = getattr(settings, 'CHANGEFEED_DB', SITE_SLUG)
TABLE = getattr(settings, 'CHANGEFEED_TABLE', 'changefeed')
    
VERBOSE = getattr(settings, 'CHANGEFEED_VERBOSE', True)

CUSTOM_HANDLERS = getattr(settings, 'CHANGEFEED_HANDLERS', [])

default_handlers = SITE_SLUG+'.r_handlers'

try:
    mod = importlib.import_module(default_handlers)
    has_default_handler = True
except ImportError:
    has_default_handler = False

HANDLERS = []

# check for a SITE_SLUG/r_handlers.py file
if has_default_handler:
    HANDLERS = [default_handlers]
    # check for the flow_handlers function presence
    try:
        h = mod.feed_handlers
    except:
        raise ImproperlyConfigured(u'Changefeed: You must add a feed_handlers function in you r_handlers.py file')
    # check for the r_query function presence
    try:
        q = mod.r_query
        R_QUERY = q()
    except:
        pass

# check for custom handlers
if len(CUSTOM_HANDLERS) > 0:
    HANDLERS = HANDLERS+CUSTOM_HANDLERS

if HANDLERS == []:
    raise ImproperlyConfigured(u'Changefeed; No handlers set: please create a r_handlers.py in your main application directory (where settings.py is).')