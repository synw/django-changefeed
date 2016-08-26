# -*- coding: utf-8 -*-

import rethinkdb as r
from changefeed.conf import SITE_SLUG


def feed_handlers(database, table, change):
    print "Default handler ->"
    print 'DB: '+str(database)
    print 'Table: '+str(table)
    print 'Old values: '+str(change['old_val'])
    print 'New values: '+str(change['new_val'])
    return


def r_query():
    return r.db(SITE_SLUG).table("changefeed").changes()