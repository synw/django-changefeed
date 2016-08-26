from __future__ import unicode_literals

from django.apps import AppConfig


class ChangefeedConfig(AppConfig):
    name = 'changefeed'
    
    def ready(self):
        pass
            
