Install
=======

.. highlight:: bash

::

   cd my_project
   git clone https://github.com/synw/django-changeflow.git && mv django-changeflow/changeflow . && rm -rf django-changeflow
   pip install rethinkdb celery celery-once
   
Then add ``'changeflow',`` to INSTALLED_APPS.

Now create your database and table in the Rethinkdb client.

Settings
--------
   
You can set a default database and default table to be used:

.. highlight:: python

::

   # default database is set to SITE_SLUG+'_changeflow'
   CHANGEFLOW_DB = "mydb"
   # default table is set to "changeflow"
   CHANGEFLOW_TABLE = "mytable"
   
The worker is verbose by default. To silence it use this in settings.py:

.. highlight:: python

::

   CHANGEFLOW_VERBOSE = False