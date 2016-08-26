Django Changefeed
=================

This module makes it easy to use the realtime capabilities of Rethinkdb in Django.

Features
--------

- Push data to a table
- Handle in Django the data coming from the Rethinkdb changefeed

Depends on Celery for the async jobs.

Quick example
-------------

Push a document to Rethinkdb:

  ```python
from changefeed.tasks import push_to_feed

push_to_feed.delay({"message":"Hello world"})
  ```
Handle the changefeed events:
  
  ```python
# this function will be triggered on every change in the Rethinkdb data
def feed_handlers(database, table, change):
	message = change['new_val']['message']
	print message
	return
  ```

Documentation
-------------

Read the [documentation](http://django-changefeed.readthedocs.io/en/latest/).

Example app
-----------

[Jafeed](https://github.com/synw/jafeed): rss aggregator that listens to the changefeed to display 
live update notifications