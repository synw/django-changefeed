# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


RETHINKDB_HOST = getattr(settings, 'RETHINKDB_HOST', 'localhost')
RETHINKDB_PORT = getattr(settings, 'RETHINKDB_PORT', 28015)

try:
    SITE_SLUG = getattr(settings, 'SITE_SLUG', 'site')
except ImportError:
    raise ImproperlyConfigured(u"Changeflow; a SITE_SLUG setting is required")
    
VERBOSE = getattr(settings, 'CHANGEFLOW_VERBOSE', True)

HANDLERS = getattr(settings, 'CHANGEFLOW_HANDLERS', [SITE_SLUG+'.changeflow'])