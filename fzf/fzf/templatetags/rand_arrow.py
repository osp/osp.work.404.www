"""
Produce a random arrow unicode character
"""

from django import template
register = template.Library()

import random

@register.filter(name='arrow')
def rand_arrow(value):
    r = random.randrange(8592,8652)
    return unichr(r)