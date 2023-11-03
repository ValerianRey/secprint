from secprint import SectionPrinter as Spt


Spt.enter_section('MAINMAIN')
Spt.print('Hello', end='')
Spt.print(' world', end='', print_headers=False)
