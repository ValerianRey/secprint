from context_printer import ContextPrinter as Ctp
from context_printer import Color

Ctp.set_max_depth(3)
Ctp.enter_section('Title that will be printed')
Ctp.print('Text that will be printed1')
Ctp.enter_section('Title that will be printed')
Ctp.print('Text that will be printed')
Ctp.enter_section('Title that will be printed')
Ctp.print('Text that will be printed')
Ctp.enter_section('Title that will be printed')
Ctp.print('Text that will not be printed')
Ctp.enter_section('Title the will not be printed')
Ctp.print('Text that will not be printed')
Ctp.exit_section()
Ctp.exit_section()
Ctp.print('Text that will be printed again')
Ctp.exit_section()
Ctp.print('Text that will be printed again')
