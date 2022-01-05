#!/usr/bin/env python3

"""
Example of a section shared between several methods and modules.

Example3 is doing stuff
█ Example2 is doing stuff
█ █ Example1 is starting to do stuff
█ █ █ YOLO
█ █ █ Example1 is done doing stuff
█ █ Example2 is done doing stuff
█ Example3 is done doing stuff
"""

from context_printer import ContextPrinter as Ctp
from example2 import Example2


class Example3:
    def __init__(self):
        self.sub_routine = None
    def start_stuff(self):
        Ctp.enter_section("Example3 is doing stuff", color='purple')
        self.sub_routine = Example2()
        self.sub_routine.start_stuff()
    def end_stuff(self):
        self.sub_routine.end_stuff()
        Ctp.print("Example3 is done doing stuff")
        Ctp.exit_section()

if __name__ == '__main__':
    ex = Example3()
    ex.start_stuff()
    Ctp.print("YOLO")
    ex.end_stuff()
