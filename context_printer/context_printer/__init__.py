#!/usr/bin/env python3

"""
** Allows you to make code blocks verbose. **
---------------------------------------------

Examples
--------
>>> from context_printer.memory import reset_lifo
>>> reset_lifo()
>>> from context_printer.printer import Printer
>>>
>>> with Printer('Main section') as ctp:
...     ctp.print('Text in main section')
...     for i in range(3):
...         with ctp(f'Subsection {i+1}'):
...             ctp.print('Text in subsection')
...             ctp.print('Text in subsection')
...
Main section
█ Text in main section
█ Subsection 1
█ █ Text in subsection
█ █ Text in subsection
█ Subsection 2
█ █ Text in subsection
█ █ Text in subsection
█ Subsection 3
█ █ Text in subsection
█ █ Text in subsection
"""

# python3 -m pytest --full-trace --doctest-modules context_printer/

from context_printer.printer import Printer

__all__ = ['Printer', 'ContextPrinter']

printer = ctp = Printer()
ContextPrinter = printer  # Stragame to make backwards compatible with version 1.3.0.
