
from django import template
import re
register=template.Library()

@register.filter
def replace(string) :
    match=re.search(r'(?!www)([A-Za-z0-9]{3,13}\.[a-z]+(\.[a-z]+)?)', string)
    return match.group()
