#!/usr/bin/env python3

"""
** Allows you to make code blocks verbose. **
---------------------------------------------
"""

# python3 -m pytest --full-trace --doctest-modules context_printer/

from context_printer.printer import ContextPrinter as _ContextPrinter
from context_printer.color import Color

__all__ = ['ContextPrinter', 'Color']

ContextPrinter = _ContextPrinter()  # Stragame to make backwards compatible with version 1.3.0.
