# -*- coding: utf-8 -*-

import importlib
import rethinkdb as r
from celery import task
from celery_once import QueueOnce
from changeflow.utils import insert_in_table
from changeflow.conf import RETHINKDB_HOST, RETHINKDB_PORT, VERBOSE, HANDLERS ,DATABASE, TABLE, R_QUERY


@task(ignore_results=True)
def push_to_db(database=DATABASE, table=TABLE, data={}):
    insert_in_table(database, table, data)
    return

@task(ignore_results=True)
def push_to_flow(data):
    insert_in_table(DATABASE, TABLE, data)
    return

@task(base=QueueOnce, once={'graceful': True, 'keys': []})
def flow_listener(database, table, r_query=R_QUERY):
    if VERBOSE is True:
        print "*************************** Flow listener started ***************************"
        
    conn = r.connect(RETHINKDB_HOST, RETHINKDB_PORT).repl()
    if r_query is None:
        r_query = r.db(database).table(table).changes()
    for change in r_query.run(conn):
        for handler in HANDLERS:
            changeflow = importlib.import_module(handler)
            changeflow.flow_handlers(database, table, change)


    
    
