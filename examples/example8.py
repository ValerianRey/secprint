from secprint import SectionPrinter as Spt
from secprint import Color

Spt.set_max_depth(3)
Spt.enter_section('Title that will be printed')
Spt.print('Text that will be printed1')
Spt.enter_section('Title that will be printed')
Spt.print('Text that will be printed')
Spt.enter_section('Title that will be printed')
Spt.print('Text that will be printed')
Spt.enter_section('Title that will be printed')
Spt.print('Text that will not be printed')
Spt.enter_section('Title the will not be printed')
Spt.print('Text that will not be printed')
Spt.exit_section()
Spt.exit_section()
Spt.print('Text that will be printed again')
Spt.exit_section()
Spt.print('Text that will be printed again')
