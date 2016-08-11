Example
=======

Example hello world:

Make a "testdb" and a "testtable" in the Rethinkdb client.


.. highlight:: python

::

   # in settings.py
   CHANGEFLOW_DB = "testdb"
   CHANGEFLOW_TABLE = "testtable"
   
   CHANGEFLOW_HANDLERS = ['mymodule.r_handlers']
   # or just use a r_handlers.py file in your main app directory
   
   # in mymodule/r_handlers.py
   def flow_handlers(database, table, change):
   	message = change['new_val']['message']
     	print message
     return
     	
    # optionaly define a ReQL query in mymodule/r_handlers.py
    def r_query():
    	r.db("testdb").table("testtable").pluck('message').changes()

   # anywhere in your code
   from changeflow.tasks import push_to_flow
   push_to_flow.delay({"message":"Hello world"})