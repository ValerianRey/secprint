#!/usr/bin/env python3

"""
Display of a line in several times.

MAINMAIN
█ Helloworld
"""

from context_printer import ctp

with ctp('MAINMAIN'):
    ctp.print('Hello', end='')
    ctp.print(' world', print_headers=False)
