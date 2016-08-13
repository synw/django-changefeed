Push a document to Rethinkdb
============================

.. highlight:: python

::

   from changefeed.tasks import push_to_flow, push_to_db

   data = {"field_name":"field_value"}
   # this is to push to the default db and table
   push_to_feed.delay(data)
   
   # this is to push to a db and table of your choice
   push_to_db.delay("database_name", "table_name", data)
  