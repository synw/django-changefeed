Install
=======

.. highlight:: bash

::

   cd my_project
   git clone https://github.com/synw/django-changefeed.git && mv django-changefeed/changefeed . && rm -rf django-changefeed
   pip install rethinkdb celery
   
Then add ``'changefeed',`` to INSTALLED_APPS.

Now create your database and table in the Rethinkdb client.

Settings
--------

Required settings
^^^^^^^^^^^^^^^^^

.. highlight:: python

::

   SITE_SLUG = "mysite"
   
This is required for internal prefixing

Optional settings
^^^^^^^^^^^^^^^^^
   
You can set a default database and default table to be used:

.. highlight:: python

::

   # default database is set to SITE_SLUG+'_changefeed'
   CHANGEFEED_DB = "mydb"
   # default table is set to "changefeed"
   CHANGEFEED_TABLE = "mytable"
   
The worker is verbose by default. To silence it use this:

.. highlight:: python

::

   CHANGEFEED_VERBOSE = False
   
The feed listener is launched by default. If you wish not to listen to the changefeed:

.. highlight:: python

::

   CHANGEFEED_LISTEN = False
   
Run
---
   
Run Rethinkdb and Launch a Celery worker:

.. highlight:: bash

::

   celery -A project_name worker  -l info --broker='redis://localhost:6379/0'
   # or any option you want