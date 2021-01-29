from output_decorator.output_decorator import ContextPrinter as Ctp
from output_decorator.output_decorator import Color


class Example1:

    def __init__(self):
        pass

    @staticmethod
    def start_stuff():
        Ctp.enter_section("Example1 is starting to do stuff", Color.GREEN)

    @staticmethod
    def end_stuff():
        Ctp.print("Example1 is done doing stuff")
        Ctp.exit_section()



