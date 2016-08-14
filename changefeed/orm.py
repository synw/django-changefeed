# -*- coding: utf-8 -*-

import importlib
import rethinkdb as r
from changefeed.conf import RETHINKDB_HOST, RETHINKDB_PORT, VERBOSE, HANDLERS


class RethinkDB():
    
    def connect(self):
        conn = r.connect(RETHINKDB_HOST, RETHINKDB_PORT).repl()
        return conn

    def write(self, database, table, data):
        conn = self.connect()
        # push data into table
        if VERBOSE is True:
            print "Inserting data into table "+table
        res = r.db(database).table(table).insert(data, return_changes=True, conflict="replace").run(conn)
        if res['errors'] == 0:
            if res["inserted"] > 0:
                if VERBOSE is True:
                    print "Data inserted in table"
            if res["replaced"] > 0:
                if VERBOSE is True:
                    print "Data was updated in table"
        else:
            print "ERROR: "+str(res['errors'])
        conn.close()
        return
    
    def listener_default_query(self, database, table):
        return r.db(database).table(table).changes()
    
    def listen(self, database, table, r_query):
        conn = R.connect()
        if r_query is None:
            r_query = self.listener_default_query(database, table)
        if VERBOSE is True:
            print "*************************** Listening to feed "+table+" ***************************"
            print "Using handlers "+str(HANDLERS)
        for change in r_query.run(conn):
            for handler in HANDLERS:
                changefeed = importlib.import_module(handler)
                changefeed.feed_handlers(database, table, change)
        return
    
R = RethinkDB( )