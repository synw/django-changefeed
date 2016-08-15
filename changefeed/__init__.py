# -*- coding: utf-8 -*-

from changefeed.tasks import feed_listener
from changefeed.conf import DATABASE, TABLE, LISTEN

if LISTEN is True:
    feed_listener.delay(DATABASE, TABLE)