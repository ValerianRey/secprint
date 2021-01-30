from context_printer import ContextPrinter as Ctp
from context_printer import Color

Ctp.enter_section('New section')
Ctp.print('Text that will be printed with a white header')
Ctp.deactivate()
Ctp.enter_section('New subsection')
Ctp.print('Text that will not be printed')
Ctp.exit_section()
Ctp.activate()
Ctp.exit_section()
Ctp.enter_section('New section', Color.RED)
Ctp.print('Text that will be printed with a red header')
