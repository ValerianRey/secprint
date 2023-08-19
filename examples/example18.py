from context_printer import ContextPrinter as Ctp

try:
    with Ctp("New section", color="red"):
        Ctp.print("Hello world")
        Ctp.print("Hello world")
        Ctp.print("Hello world")
        raise ValueError("This text should be printed out of any context")
except ValueError as e:
    Ctp.print(e)
