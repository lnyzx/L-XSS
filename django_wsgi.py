#!/usr/bin/env python
# coding: utf-8

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lxss.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()