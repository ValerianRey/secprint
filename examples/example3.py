from output_decorator.output_decorator import ContextPrinter as Ctp
from output_decorator.output_decorator import Color
from example2 import Example2


class Example3:

    def __init__(self):
        self.sub_routine = None

    def start_stuff(self):
        Ctp.enter_section("Example3 is doing stuff", Color.PURPLE)
        self.sub_routine = Example2()
        self.sub_routine.start_stuff()
        
    def end_stuff(self):
        self.sub_routine.end_stuff()
        Ctp.print("Example3 is done doing stuff")
        Ctp.exit_section()


ex = Example3()
ex.start_stuff()
Ctp.print("YOLO")
ex.end_stuff()
