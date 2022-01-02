#!/usr/bin/env python3

from enum import Enum
from typing import Union, Optional


class Color(str, Enum):
    """
    Color class regrouping the ANSI escape sequences to print with colors and effects in console.
    """

    NONE = ''
    END = '\033[0m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'

    BLACK = '\033[30m'
    DARK_GRAY = '\033[90m'
    GRAY = '\033[37m'
    WHITE = '\033[97m'

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

    DARK_RED = '\033[31m'
    DARK_GREEN = '\033[32m'
    DARK_YELLOW = '\033[33m'
    DARK_BLUE = '\033[34m'
    DARK_PURPLE = '\033[35m'
    DARK_CYAN = '\033[36m'

    @staticmethod
    def from_string(color: str) -> 'Color':
        """
        Get a Color from a string. For example "dark_green" will get you the color DARK_GREEN.
        :param color: color stored as the string name of the color.
        """
        return getattr(Color, color.upper(), '')

    @staticmethod
    def remove_colors(text: str) -> str:
        """
        Return a new text corresponding to the input text but with all colors removed.
        :param text: text from which to remove the colors
        """
        for color in Color:
            text = text.replace(color, '')
        return text

    @staticmethod
    def rainbow(text: str) -> str:
        """
        Return a new text corresponding to the input text colored as a rainbow
        :param text: text to color.
        """
        rainbow_colors = [
            Color.RED,
            Color.YELLOW,
            Color.GREEN,
            Color.CYAN,
            Color.BLUE,
            Color.PURPLE,
        ]
        result = ''
        i = 0
        for char in text:
            result = result + rainbow_colors[i % len(rainbow_colors)] + char + Color.END
            if char != ' ':
                i += 1
        return result
