from context_printer import ContextPrinter as Ctp

Ctp.set_automatic_skip(True)


with Ctp("Main section", color="blue"):
    Ctp.print('Text in main section')
    for i in range(3):
        with Ctp(f"Subsection {i + 1}"):
            Ctp.print('Text in subsection')
            Ctp.print('Text in subsection')
