from secprint import SectionPrinter as Spt


@Spt.section("New section", color="Purple")
def print_text(text: str) -> None:
    Spt.print(text)
    Spt.print(text)
    Spt.print(text)
    raise ValueError("This text should be printed out of any section")


try:
    print_text("Text in section")
except ValueError as e:
    Spt.print(e)
