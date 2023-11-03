from secprint import SectionPrinter as Spt
from secprint import Color
from example2 import Example2


class Example3:

    def __init__(self):
        self.sub_routine = None

    def start_stuff(self):
        Spt.enter_section("Example3 is doing stuff", Color.PURPLE)
        self.sub_routine = Example2()
        self.sub_routine.start_stuff()
        
    def end_stuff(self):
        self.sub_routine.end_stuff()
        Spt.print("Example3 is done doing stuff")
        Spt.exit_section()


ex = Example3()
ex.start_stuff()
Spt.print("YOLO")
ex.end_stuff()
