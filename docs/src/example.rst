Example
=======

Example hello world:

Make a "testdb" and a "testtable" in the Rethinkdb client.


.. highlight:: python

::

   # in settings.py
   CHANGEFEED_DB = "testdb"
   CHANGEFEED_TABLE = "testtable"
   
   CHANGEFEED_HANDLERS = ['mymodule.r_handlers']
   # or just use a r_handlers.py file in your main app directory
   
   # in mymodule/r_handlers.py
   def feed_handlers(database, table, change):
   	message = change['new_val']['message']
     	print message
     return
     	
    # optionaly define a ReQL query in mymodule/r_handlers.py
    def r_query():
    	r.db("testdb").table("testtable").pluck('message').changes()

   # anywhere in your code
   from changefeed.tasks import push_to_flow
   push_to_feed.delay({"message":"Hello world"})