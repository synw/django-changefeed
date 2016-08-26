# -*- coding: utf-8 -*-

from changefeed.tasks import feed_listener
from changefeed.conf import DATABASE, TABLE, LISTEN, HANDLERS


if LISTEN is True:
    for handler in HANDLERS:
        feed_listener.delay(DATABASE, TABLE, handler)