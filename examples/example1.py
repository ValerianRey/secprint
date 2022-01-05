#!/usr/bin/env python3

"""
Example of a section shared between several methods.

Example1 is starting to do stuff
█ Example1 is done doing stuff
"""

from context_printer import ContextPrinter as Ctp

class Example1:
    @staticmethod
    def start_stuff():
        Ctp.enter_section("Example1 is starting to do stuff", color='green')
    @staticmethod
    def end_stuff():
        Ctp.print("Example1 is done doing stuff")
        Ctp.exit_section()

if __name__ == '__main__':
    Example1.start_stuff()
    Example1.end_stuff()
