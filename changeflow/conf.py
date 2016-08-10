# -*- coding: utf-8 -*-

import importlib
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


RETHINKDB_HOST = getattr(settings, 'RETHINKDB_HOST', 'localhost')
RETHINKDB_PORT = getattr(settings, 'RETHINKDB_PORT', 28015)

try:
    SITE_SLUG = getattr(settings, 'SITE_SLUG', 'site')
except ImportError:
    raise ImproperlyConfigured(u"Changeflow; a SITE_SLUG setting is required")
    
VERBOSE = getattr(settings, 'CHANGEFLOW_VERBOSE', True)

DEFAULT_HANDLER = SITE_SLUG+'.changeflow'
CUSTOM_HANDLERS = getattr(settings, 'CHANGEFLOW_HANDLERS', [])

try:
    importlib.import_module(DEFAULT_HANDLER)
    has_default_handler = True
except ImportError:
    has_default_handler = False

if has_default_handler:
    if CUSTOM_HANDLERS == []:
        HANDLERS = [DEFAULT_HANDLER]
    else:
        CUSTOM_HANDLERS.append(DEFAULT_HANDLER)
else:
    HANDLERS = CUSTOM_HANDLERS