from context_printer import ContextPrinter as Ctp


@Ctp.section("New section", color="Purple")
def print_text(text: str) -> None:
    Ctp.print(text)
    Ctp.print(text)
    Ctp.print(text)
    raise ValueError("This text should be printed out of any context")


try:
    print_text("Text in section")
except ValueError as e:
    Ctp.print(e)
