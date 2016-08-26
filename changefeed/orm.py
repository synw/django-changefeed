# -*- coding: utf-8 -*-

import importlib
import rethinkdb as r
from changefeed.conf import RETHINKDB_HOST, RETHINKDB_PORT, VERBOSE


class RethinkDB():
    
    def connect(self):
        conn = r.connect(RETHINKDB_HOST, RETHINKDB_PORT).repl()
        return conn

    def write(self, database, table, data):
        conn = self.connect()
        # push data into table
        if VERBOSE is True:
            print "Inserting data into database "+database
        res = r.db(database).table(table).insert(data, return_changes=True, conflict="replace").run(conn)
        if res['errors'] == 0:
            if res["inserted"] > 0:
                if VERBOSE is True:
                    print "Data inserted into table "+table
            if res["replaced"] > 0:
                if VERBOSE is True:
                    print "Data updated in table "+table
        else:
            print "ERROR: "+str(res['errors'])
        conn.close()
        return
    
    def run_query(self, r_query):
        conn = self.connect()
        return r_query.run(conn)
    
    def get_default_query(self, database, table):
        q = r.db(database).table(table).changes(include_types=True)
        return q
    
    def get_listener_query(self, database, table, handlerpath):
        handler = importlib.import_module(handlerpath)
        try:
            q = handler.r_query()
        except ImportError:
            q = self.get_default_query(database, table)
        return q
    
    def listen(self, database, table, handler, r_query=None):
        conn = self.connect() 
        if r_query is None:
            r_query = self.get_listener_query(database, table, handler)
        if VERBOSE is True:
            print "*********** Listening "+str(r_query)+" -> "+str(handler)+'.feed_handlers()'
        handler = importlib.import_module(handler)
        for change in r_query.run(conn):
            handler.feed_handlers(database, table, change)
        return
    
R = RethinkDB()