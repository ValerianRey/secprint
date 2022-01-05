#!/usr/bin/env python3

"""
Example with many formattage.

Mega section of the dead
█ Normal section
█ █ Subsection
█ █ █ This is dope shit
█ █ █ This is dope shit
█ █ █ This is dope shit
█ █ █ This is dope shit
█ █ █ This is dope shit
█ █ NONE - YOOOO
█ █ DARK_GRAY - YOOOO
█ █ GRAY - YOOOO
█ █ WHITE - YOOOO
█ █ RED - YOOOO
█ █ GREEN - YOOOO
█ █ YELLOW - YOOOO
█ █ BLUE - YOOOO
█ █ PURPLE - YOOOO
█ █ CYAN - YOOOO
"""

from context_printer import ctp

with ctp('Mega section of the dead', blink=True):
    with ctp('Normal section', color='red', blink=False):
        with ctp('Subsection', color='green'):
            for _ in range(5):
                ctp.print('This ', end='')
                ctp.print('is ', blink=True, print_headers=False, end='')
                ctp.print('dope ', print_headers=False, end='')
                ctp.print('shit', print_headers=False, blink=True)
        ctp.print('NONE - ', end='')
        ctp.print('YOOOO', print_headers=False)
        ctp.print('DARK_GRAY - ', end='')
        ctp.print('YOOOO', color='coal', print_headers=False)
        ctp.print('GRAY - ', end='')
        ctp.print('YOOOO', color='gray', print_headers=False)
        ctp.print('WHITE - ', end='')
        ctp.print('YOOOO', color='white', print_headers=False)
        ctp.print('RED - ', end='')
        ctp.print('YOOOO', color='red', print_headers=False)
        ctp.print('GREEN - ', end='')
        ctp.print('YOOOO', color='green', print_headers=False)
        ctp.print('YELLOW - ', end='')
        ctp.print('YOOOO', color='yellow', print_headers=False)
        ctp.print('BLUE - ', end='')
        ctp.print('YOOOO', color='blue', print_headers=False)
        ctp.print('PURPLE - ', end='')
        ctp.print('YOOOO', color='purple', print_headers=False)
        ctp.print('CYAN - ', end='')
        ctp.print('YOOOO', color='cyan', print_headers=False)
