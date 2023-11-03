from secprint import SectionPrinter as Spt


@Spt.section("New section", color="Purple")
def print_text(text: str) -> None:
    Spt.print(text)
    Spt.print(text)
    Spt.print(text)


print_text("Text in section")
