from secprint import SectionPrinter as Spt

Spt.enter_section('Main section', color='blue')
Spt.print('Text in main section')
for i in range(3):
    Spt.enter_section('Subsection {}'.format(i + 1))
    Spt.print('Text in subsection')
    Spt.print('Text in subsection')
    Spt.exit_section()
Spt.exit_section()
