Django Changeflow
=================

This module makes it easy to use the realtime capabilities of
Rethinkdb in Django.

Install
-------

Clone the repository and get the python client `pip install rethinkdb celery celery-once` and add `'changeflow',` to INSTALLED_APPS.
You will also need a Celery worker. It will handle the push data operations as an asynchronous task and will
launch a listener to handle the changes flow.

By default the worker is verbose. Set a ``CHANGEFLOW_VERBOSE = False`` in settings.py to silence it.

Usage
-----

To push some data into Rethinkdb:

  ```python
from changeflow.tasks import push_to_flow

push_to_flow.delay("database_name", "table_name", {"field_name":"field_value"})
  ```

Note: if the database does not exists it will be created. Same for the table. 
This creates new entries in the database.

To handle the data changes create a `changeflow.py` file in your project directory (where settings.py is) and
use a `flow_handlers` function to do whatever you want (like sending some data to a websocket for example):

  ```python
# this function will be triggered on every change in the Rethinkdb data
def flow_handlers(database, table, change):
    print database
    print table
    print str(change['old_val'])
    print str(change['new_val'])
    return
  ```
  
You can also manage handlers directly from your apps by creating a file with a `flow_handlers`
function, and declare it in a setting:

   ```python
# in settings.py
CHANGEFLOW_HANDLERS = ['mymodule.myfile']
  ```
Example hello world:

   ```python
# in settings.py
CHANGEFLOW_HANDLERS = ['myapp.handlers']

# in handlers.py
def flow_handlers(database, table, change):
	if database == 'test' and table == 'testtable':
    	message = change['new_val']['message']
    	print message
    return

# anywhere in your code
from changeflow.tasks import push_to_flow
push_to_flow.delay("testdb", "testtable", {"message":"Hello world"})
  ```
  
Todo
----

- Manage update and delete operations
- Manage indexes and keys
- Autoclean functions

Contributions are welcome.
 