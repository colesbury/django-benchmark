#!/usr/bin/env python3

from django.conf.urls import url
from django.http import HttpResponse
import sys

def index(request):
    return HttpResponse(
        f'<html><body>Hello World ({sys.implementation.name})</body></html>'
    )


def hello(request, name):
    return HttpResponse(
        f'<html><body>Hello World ({sys.implementation.name})</body></html>'
    )


urlpatterns = [url(r"^hello/(?P<name>.*)$", hello), url("", index)]
