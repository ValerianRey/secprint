from secprint import SectionPrinter as Spt
from secprint import Color

Spt.enter_section('New section')
Spt.print('Text that will be printed with a white header')
Spt.deactivate()
Spt.enter_section('New subsection')
Spt.print('Text that will not be printed')
Spt.exit_section()
Spt.activate()
Spt.exit_section()
Spt.enter_section('New section', Color.RED)
Spt.print('Text that will be printed with a red header')
