# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


RETHINKDB_HOST = getattr(settings, 'RETHINKDB_HOST', 'localhost')
RETHINKDB_PORT = getattr(settings, 'RETHINKDB_PORT', 28015)

LISTEN = getattr(settings, 'CHANGEFEED_LISTEN', False)

try:
    SITE_SLUG = getattr(settings, 'SITE_SLUG', 'site')
except ImportError:
    raise ImproperlyConfigured(u"Changeflow; a SITE_SLUG setting is required")

DATABASE = getattr(settings, 'CHANGEFEED_DB', SITE_SLUG)
TABLE = getattr(settings, 'CHANGEFEED_TABLE', 'changefeed')
    
VERBOSE = getattr(settings, 'CHANGEFEED_VERBOSE', True)