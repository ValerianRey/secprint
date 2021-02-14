from context_printer import ContextPrinter as Ctp


Ctp.enter_section('MAINMAIN')
Ctp.print('Hello', end='')
Ctp.print(' world', end='', print_headers=False)
