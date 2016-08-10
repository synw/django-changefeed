# -*- coding: utf-8 -*-

from django.conf import settings


RETHINKDB_HOST = getattr(settings, 'RETHINKDB_HOST', 'localhost')
RETHINKDB_PORT = getattr(settings, 'RETHINKDB_PORT', 28015)

SITE_SLUG = getattr(settings, 'SITE_SLUG', 'site')
VERBOSE = getattr(settings, 'CHANGEFLOW_VERBOSE', True)