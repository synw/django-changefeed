# -*- coding: utf-8 -*-

import rethinkdb as r
from changefeed.conf import RETHINKDB_HOST, RETHINKDB_PORT, VERBOSE


def insert_in_table(database, table, data):
    conn = r.connect(RETHINKDB_HOST, RETHINKDB_PORT).repl()
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
    conn.close()
    return