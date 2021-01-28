class Color:
    """
    Color class regrouping the ANSI escape sequences to print with colors and effects in console.
    """

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    BRIGHT_GREEN = '\033[92m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    GRAY = '\033[90m'
    BLACK = '\u001b[30m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    NONE = ''

    def __add__(self, other):
        return self + other


class ContextPrinter:
    @staticmethod
    def check_init() -> None:
        """
        Verify that the OutputDecorator is correctly initialized.
        """
        try:
            ContextPrinter.self.is_init
        except AttributeError:
            ContextPrinter.reset()
            ContextPrinter.self.is_init = True

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
        ContextPrinter.self.headers = []

    @staticmethod
    def __add_header(header: str, color: Color) -> None:
        """
        Adds a header to print before the text.
        :param header: header string to print.
        :param color: color of the header to print.
        """
        ContextPrinter.self.headers.append(color + header + Color.END)

    @staticmethod
    def enter_section(title: str = None, color: Color = Color.NONE, header: str = '█ ') -> None:
        """
        Enter a new section with the corresponding color code and prints the corresponding title.
        :param title: name of the section.
        :param color: color to use for this section.
        :param header: string to use as header for the whole section.
        """
        ContextPrinter.check_init()
        if title is not None:
            ContextPrinter.print(title, color=color, bold=True)

        ContextPrinter.__add_header(header, color)

    @staticmethod
    def exit_last_section() -> None:
        """
        Exit the last section added.
        """
        ContextPrinter.self.headers = ContextPrinter.self.headers[:-1]

    @staticmethod
    def __print_line(text: str = '', color: Color = Color.NONE, bold: bool = False, underline: bool = False,
                     rewrite: bool = False, end: str = '\n') -> None:
        """
        Print the sections' headers and the input text line.
        :param text: text to be printed. It should be in a single line (no \n character).
        :param color: color to give to the text.
        :param bold: if set to true, prints the text in boldface.
        :param underline: if set to true, prints the text underlined.
        :param rewrite: if set to true, rewrites over the current line instead of printing a new line.
        :param end: character to print at the end of the line.
        """
        if rewrite:
            print('\r', end='')
        for header in ContextPrinter.self.headers:
            print(header, end='')

        print(color + (Color.BOLD if bold else '') + (Color.UNDERLINE if underline else '') + text + Color.END, end=end)

    @staticmethod
    def print(text: str = '', color: Color = Color.NONE, bold: bool = False, underline: bool = False,
              rewrite: bool = False, end: str = '\n') -> None:
        """
        Print the sections' headers and the input text
        :param text: text to be printed.
        :param color: color to give to the text.
        :param bold: if set to true, prints the text in boldface.
        :param underline: if set to true, prints the text underlined.
        :param rewrite: if set to true, rewrites over the current line instead of printing a new line.
        :param end: character to print at the end of the text.
        """
        ContextPrinter.check_init()
        lines = text.split('\n')
        for line in lines:
            ContextPrinter.__print_line(line, color=color, bold=bold, underline=underline, rewrite=rewrite, end=end)
