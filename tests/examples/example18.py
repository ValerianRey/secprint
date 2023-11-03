from secprint import SectionPrinter as Spt

try:
    with Spt("New section", color="red"):
        Spt.print("Hello world")
        Spt.print("Hello world")
        Spt.print("Hello world")
        raise ValueError("This text should be printed out of any section")
except ValueError as e:
    Spt.print(e)
