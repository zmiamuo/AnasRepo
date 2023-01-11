
import urllib.request

from django import template
import re
register=template.Library()

def ip_request():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip