Django Changeflow
=================

This module makes it easy to use the realtime capabilities of
Rethinkdb in Django.

Install
-------

Clone the repository and get the python client `pip install rethinkdb`
You will also need a Celery worker. It will handle the push data operations as an asynchronous task and will
launch a listener to handle the changes flow. Add `'changeflow',` to INSTALLED_APPS.

Usage
-----

To push some data into Rethinkdb:

  ```python
from changeflow.tasks import push_to_flow

push_to_flow.delay("database_name", "table_name", {"field_name":"field_value"})
  ```

Note: if the database does not exists it will be created. Same for the table. If the field exists it will
be updated, otherwise it will be created.

To handle the data changes create a `changeflow.py` file in your project directory (where settings.py is) and
use a `flow_handlers` function to do whatever you want (like sending some data to a websocket for example):

  ```python
# this function will be triggered on every change in the Rethinkdb data
def flow_handlers(database, table, change):
    print str(database)
    print str(table)
    print str(change['old_val'])
    print str(change['new_val'])
    return
  ```
  
You can also create handlers directly in your apps by creating a file with a `flow_handlers`
function, and declare it in a setting:

   ```python
# in settings.py
CHANGEFLOW_HANDLERS = ['mymodule.myfile']
  ```

 