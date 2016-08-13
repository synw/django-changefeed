# -*- coding: utf-8 -*-

from changefeed.tasks import feed_listener
from changefeed.conf import DATABASE, TABLE

feed_listener.delay(DATABASE, TABLE)