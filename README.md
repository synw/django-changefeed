Django Changeflow
=================

Rethinkdb realtime feeds manager for Django. This module makes it easy to use the realtime capabilities of
Rethinkdb in Django.

Install
-------

Clone the repository and the python client `pip install rethinkdb`
You will also need a Celery worker. It will handle the push data operations as an asynchronous task and will
launch a listener to handle the changes flow.

Usage
-----

To push some data into Rethinkdb:

  ```python
from changeflow.tasks import push_to_flow

push_to_flow.delay("database_name", "table_name", {"field_name":"field_value"})
)
  ```
  
To handle the data changes create a `changeflow.py` file in your project directory (where settings.py is) and
tweak the flow handler to match your needs:

  ```python
# this function will be triggered on every change into the Rethinkdb data
def flow_handlers(database, table, change):
    print str(database)
    print str(table)
    print str(change['old_val'])
    print str(change['new_val'])
    return
  ```