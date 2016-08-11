Usage
=====

Run Rethinkdb and Launch a Celery worker:

.. highlight:: bash

::

   celery -A mogo worker  -l info --broker='redis://localhost:6379/0'
   # or any option you want

Push a document to Rethinkdb
----------------------------

.. highlight:: python

::

   from changeflow.tasks import push_to_flow, push_to_db

   data = {"field_name":"field_value"}
   # this is to push to the default db and table
   push_to_flow.delay(data)
   
   # this is to push to a db and table of your choice
   push_to_db.delay("database_name", "table_name", data)
   
Handle the changes events
-------------------------

To handle the data changes create a ``r_handlers.py`` file in your project directory (where settings.py is).

Set the ReQL query
^^^^^^^^^^^^^^^^^^

The listener will use by default the following ReQL query, listening to all changes in the table:

.. highlight:: python

::

   r.db(database).table(table).changes()

You can set a custom ReQL query for the listener in ``r_handlers.py`` with a ``r_query`` function:

.. highlight:: python

::

   def r_query():
   	return r.db("mydb").table("mytable").pluck('message').changes()
   	
Write the handlers
^^^^^^^^^^^^^^^^^^

In ``r_handlers.py`` use a ``flow_handlers`` function to do whatever you want 
(like sending some data to a websocket for example):

.. highlight:: python

::

   # this function will be triggered on every change in the Rethinkdb data
   def flow_handlers(database, table, change):
       print database
       print table
       print str(change['old_val'])
       print str(change['new_val'])
       return
       
You can also manage handlers directly from your apps by creating a file with a ``flow_handlers`` function, 
and declare it in a setting:

.. highlight:: python

::

   # in settings.py
   CHANGEFLOW_HANDLERS = ['mymodule.myfile']

