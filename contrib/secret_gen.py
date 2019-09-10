#!/usr/bin/env python
"""
Django SECRECT_KEY generator.
"""

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwyz0123456789!@#$%ˆˆ*(-_=+)'
print(get_random_string(50, chars))
