from secprint import SectionPrinter as Spt
from secprint import Color


class Example1:

    def __init__(self):
        pass

    @staticmethod
    def start_stuff():
        Spt.enter_section("Example1 is starting to do stuff", Color.GREEN)

    @staticmethod
    def end_stuff():
        Spt.print("Example1 is done doing stuff")
        Spt.exit_section()



