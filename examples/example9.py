from context_printer import ContextPrinter as Ctp
from context_printer import Color

Ctp.set_automatic_skip(True)
Ctp.print('Hello')
Ctp.print('Hello')
Ctp.print('Hello')
Ctp.print('Hello')
Ctp.enter_section('MAINMAIN')
Ctp.enter_section('MAIN')
Ctp.enter_section('Section')
Ctp.enter_section('Subsection')
Ctp.enter_section('Subsubsection')
Ctp.exit_section()
Ctp.exit_section()
Ctp.exit_section()
Ctp.exit_section()
Ctp.print('Hello')
Ctp.exit_section()
