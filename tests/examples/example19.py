from secprint import SectionPrinter as Spt

Spt.set_automatic_skip(True)


with Spt("Main section", color="blue"):
    Spt.print('Text in main section')
    for i in range(3):
        with Spt(f"Subsection {i + 1}"):
            Spt.print('Text in subsection')
            Spt.print('Text in subsection')
