from secprint import SectionPrinter as Spt
from secprint import Color
from example1 import Example1


class Example2:

    def __init__(self):
        self.sub_routine = None

    def start_stuff(self):
        Spt.enter_section("Example2 is doing stuff", Color.BLUE)
        self.sub_routine = Example1()
        self.sub_routine.start_stuff()

    def end_stuff(self):
        self.sub_routine.end_stuff()
        Spt.print("Example2 is done doing stuff")
        Spt.exit_section()


