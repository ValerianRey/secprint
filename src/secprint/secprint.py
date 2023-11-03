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
        rainbow_colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.PURPLE]
        result = ''
        i = 0
        for char in text:
            result = result + rainbow_colors[i % len(rainbow_colors)] + char + Color.END
            if char != ' ':
                i += 1
        return result


class SectionPrinter:
    @staticmethod
    def check_init() -> None:
        """
        Verify that the OutputDecorator is correctly initialized.
        """
        try:
            SectionPrinter.self.is_init
        except AttributeError:
            SectionPrinter.reset()
            SectionPrinter.self.is_init = True

    @staticmethod
    def self() -> None:
        """
        Does nothing, only used to store static attributes.
        """
        pass

    @staticmethod
    def reset() -> None:
        """
        Reset the parameters of the decorator.
        """
        SectionPrinter.self.headers = []
        SectionPrinter.self.activated = True
        SectionPrinter.self.max_depth = None
        SectionPrinter.self.automatic_skip = False
        SectionPrinter.self.buffered_skiplines = 0
        SectionPrinter.self.coloring = True
        SectionPrinter.self.default_header = '█ '

    @staticmethod
    def __add_header(header: str, color: Color) -> None:
        """
        Adds a header to print before the text.
        :param header: header string to print.
        :param color: color of the header to print.
        """
        SectionPrinter.self.headers.append(color + header + Color.END)

    @staticmethod
    def enter_section(title: Optional[str] = None, color: Union[Color, str] = Color.NONE, header: Optional[str] = None) -> None:
        """
        Enter a new section with the corresponding color code and prints the corresponding title.
        :param title: name of the section.
        :param color: color to use for this section.
        :param header: string to use as header for the whole section. Leave it as None to use the default value. Use an empty
        string ('') to have no header.
        """
        SectionPrinter.check_init()
        if header is None:
            header = SectionPrinter.self.default_header

        if SectionPrinter.self.automatic_skip:
            SectionPrinter.__skip_lines(SectionPrinter.self.buffered_skiplines)
            SectionPrinter.self.buffered_skiplines = 0

        if SectionPrinter.self.activated:
            if not isinstance(color, Color):
                color = Color.from_string(color)

            if title is not None:
                SectionPrinter.print(title, color=color, bold=True)
            else:
                SectionPrinter.self.print_next_headers = True

            SectionPrinter.__add_header(header, color)

    @staticmethod
    def exit_section() -> None:
        """
        Exit the last section added.
        """
        if SectionPrinter.self.automatic_skip:
            if SectionPrinter.self.max_depth is None or SectionPrinter.self.max_depth >= len(SectionPrinter.self.headers):
                SectionPrinter.self.buffered_skiplines += 1

        if SectionPrinter.self.activated:
            SectionPrinter.self.headers = SectionPrinter.self.headers[:-1]

    @staticmethod
    def __skip_lines(n_lines: int):
        for i in range(n_lines):
            SectionPrinter.__print_line('', end='\n')

    @staticmethod
    def __print_headers():
        if SectionPrinter.self.coloring:
            for header in SectionPrinter.self.headers:
                print(header, end='')
        else:
            for header in SectionPrinter.self.headers:
                print(Color.remove_colors(header), end='')

    @staticmethod
    def __print_line(text: str = '', color: Color = Color.NONE, bold: bool = False, underline: bool = False, blink: bool = False,
                     print_headers: bool = True, rewrite: bool = False, end: str = '\n') -> None:
        """
        Print the sections' headers and the input text line.
        :param text: text to be printed. It should be in a single line (no \n character).
        :param color: color to give to the text.
        :param bold: if set to true, prints the text in boldface.
        :param underline: if set to true, prints the text underlined.
        :param blink: if set to true, the line will be blinking (not compatible with all consoles).
        :param print_headers: if set to true, all section headers will be printed before the text.
        :param rewrite: if set to true, rewrites over the current line instead of printing a new line.
        :param end: character to print at the end of the line.
        """
        if rewrite:
            print('\r', end='')

        if print_headers:
            SectionPrinter.__print_headers()

        if SectionPrinter.self.coloring:
            text = color + (Color.BOLD if bold else '') + (Color.UNDERLINE if underline else '') + \
                   (Color.BLINK if blink else '') + text + Color.END
        else:
            text = Color.remove_colors(text)  # we still remove the colors in case the user included them in the text itself
        print(text, end=end)

    @staticmethod
    def print(text='', color: Union[Color, str] = Color.NONE, bold: bool = False, underline: bool = False, blink: bool = False,
              print_headers: bool = True, rewrite: bool = False, end: str = '\n') -> None:
        """
        Print the sections' headers and the input text
        :param text: text to be printed.
        :param color: color to give to the text.
        :param bold: if set to true, prints the text in boldface.
        :param underline: if set to true, prints the text underlined.
        :param blink: if set to true, the text will be blinking (not compatible with all consoles).
        :param print_headers: if set to true, all section headers will be printed before the text.
        :param rewrite: if set to true, rewrites over the current line instead of printing a new line.
        :param end: character to print at the end of the text.
        """
        SectionPrinter.check_init()

        if SectionPrinter.self.activated and (SectionPrinter.self.max_depth is None or
                                              SectionPrinter.self.max_depth >= len(SectionPrinter.self.headers)):
            if not isinstance(text, str):
                try:
                    text = str(text)
                except AttributeError:
                    try:
                        text = repr(text)
                    except AttributeError:
                        raise AttributeError('text object is not a string and does not implement __str__ or __repr__')

            if not isinstance(color, Color):
                color = Color.from_string(color)

            lines = text.split('\n')
            for i, line in enumerate(lines):
                line_end = end if i == len(lines) - 1 else '\n'
                SectionPrinter.__print_line(line, color=color, bold=bold, underline=underline, blink=blink,
                                            print_headers=print_headers, rewrite=rewrite, end=line_end)

    @staticmethod
    def activate() -> None:
        """
        Reactivate the printer so that it gets back to work after a call to deactivate.
        """
        SectionPrinter.check_init()
        SectionPrinter.self.activated = True

    @staticmethod
    def deactivate() -> None:
        """
        Deactivate the printer so that it does not do anything (printing, entering sections, exiting sections) until reactivation.
        """
        SectionPrinter.check_init()
        SectionPrinter.self.activated = False

    @staticmethod
    def set_coloring(value: bool) -> None:
        """
        Sets on or off the coloring of the text printed. This can be used to deactivate coloring when running a script on a console
        that does not support ANSI escape characters, by just adding a call to set_coloring instead of modifying every call to print
        in the whole script.
        :param value: value to set on or off the coloring of the text.
        """
        SectionPrinter.check_init()
        SectionPrinter.self.coloring = value

    @staticmethod
    def set_max_depth(value: int) -> None:
        """
        Sets a maximum number of nested sections after which the printer will stop printing (it will still be able to enter or exit
        deeper sections but without printing their title or their header at all).
        :param value: value to set to the max depth parameter.
        """
        SectionPrinter.check_init()
        SectionPrinter.self.max_depth = value

    @staticmethod
    def set_automatic_skip(value: bool) -> None:
        """
        Sets on or off the automatic skip-line mode of the printer. When it's set to True, it will automatically skip an appropriate
        number of lines when exiting a section. When set to false it will not do anything special when exiting a section.
        :param value: value to set on or off the automatic skip-line mode.
        """
        SectionPrinter.check_init()
        SectionPrinter.self.automatic_skip = value

    @staticmethod
    def set_default_header(value: str) -> None:
        """
        Sets a default header text for the sections.
        :param value: text to set the default header to.
        """
        SectionPrinter.check_init()
        SectionPrinter.self.default_header = value

    def __init__(self, title: str = '', color: Union[Color, str] = Color.NONE, header: Optional[str] = None):
        # This is a shortcut (Ahem... disgusting trick...) to call
        # a static method of SectionPrinter directly.
        SectionPrinter.enter_section(title, color, header)

    @staticmethod
    def __enter__() -> None:
        pass

    @staticmethod
    def __exit__(exc_type, exc_val, exc_tb) -> None:
        SectionPrinter.exit_section()

    @staticmethod
    def section(text: str = '', color: Union[Color, str] = Color.NONE):
        """
        Parametrized decorator that allows to set a function to do its job inside a SectionPrinter section.
        """

        def decorator(func):
            def func_in_section(*args, **kwargs):
                with SectionPrinter(text, color):
                    func(*args, **kwargs)

            return func_in_section

        return decorator
