#!/usr/bin/env python3
import mimetypes

mimetypes.knownfiles = ["./mime.types"]

import django
import os
from django.core import management
from django.conf import settings
import sys

addrport = "0.0.0.0:8888"
if len(sys.argv) > 1:
    addrport = sys.argv[1]

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()
management.call_command("runserver", use_reloader=False, use_threading=True, addrport=addrport)
