# -*- coding: utf-8 -*-

from changefeed.tasks import feed_listener
from changefeed.conf import DATABASE, TABLE, LISTEN, SITE_SLUG


if LISTEN is True:
    handler = SITE_SLUG+'.r_handlers'
    feed_listener.delay(DATABASE, TABLE, handler)