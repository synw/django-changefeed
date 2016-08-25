from __future__ import unicode_literals

from django.apps import AppConfig


class ChangefeedConfig(AppConfig):
    name = 'changefeed'
    
    def ready(self):
        from changefeed.tasks import feed_listener
        from changefeed.conf import DATABASE, TABLE, LISTEN
        if LISTEN is True:
            feed_listener.delay(DATABASE, TABLE)
            
