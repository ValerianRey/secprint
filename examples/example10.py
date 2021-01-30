from context_printer import ContextPrinter as Ctp

Ctp.enter_section('Main section', color='blue')
Ctp.print('Text in main section')
for i in range(3):
    Ctp.enter_section('Subsection {}'.format(i + 1))
    Ctp.print('Text in subsection')
    Ctp.print('Text in subsection')
    Ctp.exit_section()
Ctp.exit_section()
