# -*- coding: utf-8 -*-

from changefeed.orm import R
from changefeed.conf import DATABASE, TABLE
from celery import shared_task


@shared_task(ignore_results=True)
def feed_listener(database, table, handler, r_query=None): 
    R.listen(database, table, handler, r_query)
    return

@shared_task(ignore_results=True)
def push_to_db(database=DATABASE, table=TABLE, data={}):
    R.write(database, table, data)
    return

@shared_task(ignore_results=True)
def push_to_feed(data):
    R.write(DATABASE, TABLE, data)
    return


    
    
