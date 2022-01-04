#!/usr/bin/env python3

"""
** Allows you to make code blocks verbose. **
---------------------------------------------
"""

# python3 -m pytest --full-trace --doctest-modules context_printer/

from context_printer.printer import Printer

__all__ = ['Printer', 'ContextPrinter']

printer = ctp = Printer()
ContextPrinter = printer  # Stragame to make backwards compatible with version 1.3.0.
