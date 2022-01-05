#!/usr/bin/env python3

"""
Allows to test the backward compatibility.

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

from context_printer import ContextPrinter as Ctp

Ctp.enter_section('Main section', color='blue')
Ctp.print('Text in main section')
for i in range(3):
    Ctp.enter_section('Subsection {}'.format(i + 1))
    Ctp.print('Text in subsection')
    Ctp.print('Text in subsection')
    Ctp.exit_section()
Ctp.exit_section()
