# -*- coding: utf-8 -*-

import importlib
import rethinkdb as r
from celery import task
from celery_once import QueueOnce
from changeflow.conf import RETHINKDB_HOST, RETHINKDB_PORT, SITE_SLUG, VERBOSE, HANDLERS

@task(ignore_results=True)
def push_to_flow(database=SITE_SLUG, table='changeflow', data={}):
    conn = r.connect(RETHINKDB_HOST, RETHINKDB_PORT).repl()
    # check if db exists or create it
    dblist = r.db_list().run(conn)
    if database not in dblist:
        if VERBOSE is True:
            print "Database "+database+" not found"
            print "* Creating database "+database
        r.db_create(database).run(conn)
    conn.use(database)
    # check if table exists
    tables_list = r.db(database).table_list().run(conn)
    if table not in tables_list:
        if VERBOSE is True:
            print "Table "+table+" not found"
            print "* Creating table "+table
        r.db(database).table_create(table).run(conn)
    # push data into table
    if VERBOSE is True:
        print "Inserting data into table "+table
    res = r.db(database).table(table).insert(data, return_changes=True, conflict="update").run(conn)
    if res['errors'] == 0:
        if res["inserted"] > 0:
            if VERBOSE is True:
                print "Data inserted in table"
        if res["replaced"] > 0:
            if VERBOSE is True:
                print "Data was updated in table"
    return

@task(base=QueueOnce, once={'graceful': True, 'keys': []})
def flow_listener(**kwargs):
    if VERBOSE is True:
        print "*************************** Flow listener started *********************************************"
    if kwargs.has_key('database'):
        database = kwargs['database']
    else:
        database = SITE_SLUG
    if kwargs.has_key('table'):
        table = kwargs['table']
    else:
        table = "changeflow"
    
    conn = r.connect(RETHINKDB_HOST, RETHINKDB_PORT).repl()
    print "H: "+str(HANDLERS)
    for change in r.db(database).table(table).changes().run(conn):
        for handler in HANDLERS:
            changeflow = importlib.import_module(handler)
            changeflow.flow_handlers(database, table, change)


    
    
