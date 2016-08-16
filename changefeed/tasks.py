# -*- coding: utf-8 -*-

from changefeed.orm import R
from changefeed.conf import DATABASE, TABLE
from celery import shared_task
from celery_once import QueueOnce
from changefeed.conf import PUSH_AYSNC

@shared_task(base=QueueOnce, once={'graceful': True, 'keys': []})
def feed_listener(database, table, r_query=None):   
    R.listen(database, table, r_query)
    return

if PUSH_AYSNC is False:
    
    @shared_task(ignore_results=True)
    def push_to_db(database=DATABASE, table=TABLE, data={}):
        R.write(database, table, data)
        return
    
    @shared_task(ignore_results=True)
    def push_to_feed(data):
        R.write(DATABASE, TABLE, data)
        return
    
else:

    def push_to_db(database=DATABASE, table=TABLE, data={}):
        R.write(database, table, data)
        return

    def push_to_feed(data):
        R.write(DATABASE, TABLE, data)
        return


    
    
