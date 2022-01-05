#!/usr/bin/env python3

"""
Example of a section shared between several methods and modules.

Example2 is doing stuff
█ Example1 is starting to do stuff
█ █ Example1 is done doing stuff
█ Example2 is done doing stuff
"""

from context_printer import ContextPrinter as Ctp
from example1 import Example1


class Example2:
    def __init__(self):
        self.sub_routine = None
    def start_stuff(self):
        Ctp.enter_section("Example2 is doing stuff", color='blue')
        self.sub_routine = Example1()
        self.sub_routine.start_stuff()
    def end_stuff(self):
        self.sub_routine.end_stuff()
        Ctp.print("Example2 is done doing stuff")
        Ctp.exit_section()

if __name__ == '__main__':
    ex = Example2()
    ex.start_stuff()
    ex.end_stuff()
