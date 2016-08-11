# -*- coding: utf-8 -*-

from changeflow.tasks import flow_listener
from changeflow.conf import DATABASE, TABLE

flow_listener.delay(DATABASE, TABLE)