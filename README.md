Django Changefeed
=================

This module makes it easy to use the realtime capabilities of Rethinkdb in Django.

Features:

- Push data to a table
- Handle in Django the data coming from the Rethinkdb changefeed

Depends on Celery for the async jobs.

Quick example:

Push a document to Rethinkdb:

  ```python
from changefeed.tasks import push_to_flow
push_to_feed.delay({"message":"Hello world"})
  ```
Handle the changefeed events:
  
  ```python
def feed_handlers(database, table, change):
	# get the field "message" from the table "table" from db "database"
	message = change['new_val']['message']
	old_message = change['old_val']['message']
	# do what you want whith it
	print message
	return
  ```

Read the [documentation](http://django-changefeed.readthedocs.io/en/latest/) for details.