from secprint import SectionPrinter as Spt
from secprint import Color

Spt.set_automatic_skip(True)
# Spt.set_default_header('✘ ')
Spt.set_max_depth(3)
Spt.enter_section()
Spt.enter_section('Main section', Color.BLUE)
Spt.print('Text in main section')
for i in range(3):
    Spt.enter_section(color="red")
    # Spt.enter_section('Subsection {}'.format(i + 1), "red")
    Spt.print('Text in subsection')
    Spt.print('Text in subsection')
    Spt.exit_section()
Spt.exit_section()

Spt.set_default_header('✘✘ ')
Spt.set_coloring(False)
Spt.enter_section('Main section', color='blue')
Spt.print('Text in main section')
for i in range(3):
    Spt.enter_section('Subsection {}'.format(i + 1), Color.BOLD)
    Spt.print('Text in subsection')
    Spt.print('Text in subsection')
    Spt.exit_section()
Spt.exit_section()

Spt.set_default_header('✘✘✘ ')
Spt.set_coloring(True)
Spt.enter_section('Main section', color='blue')
Spt.print('Text in main section')
for i in range(3):
    Spt.enter_section('Subsection {}'.format(i + 1), Color.BOLD)
    Spt.print('Text in subsection')
    Spt.print('Text in subsection')
    Spt.exit_section()
Spt.exit_section()
Spt.exit_section()
