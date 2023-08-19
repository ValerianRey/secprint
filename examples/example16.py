from context_printer import ContextPrinter as Ctp


@Ctp.section("New section", color="Purple")
def print_text(text: str) -> None:
    Ctp.print(text)
    Ctp.print(text)
    Ctp.print(text)


print_text("Text in section")
