#!/usr/bin/env python3

"""
** Allows you to format the text color. **
------------------------------------------

Specifically allows you to choose from a reduced list,
the highlighting color and the text color.
"""

import colorama

from context_printer.memory import get_lifo


colorama.init() # for windows


def _str_to_color(color):
    r"""
    ** Normalize the name of the color. **

    Parameters
    ----------
    color : str
        The name of the color that we want to normalize.

    Returns
    -------
    style : str
        The color scheme (DIM, NORMAL, BRIGHT).
    color : str
        The normalized color (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE).

    Raises
    ------
    KeyError
        If the color is not in one of the possible solutions.

    Examples
    --------
    >>> from context_printer.color import _str_to_color
    >>> _str_to_color('blue')
    ('NORMAL', 'BLUE')
    >>> _str_to_color('Pink\n')
    ('BRIGHT', 'MAGENTA')
    >>>
    """
    colors = {
        'BLACK': ('DIM', 'BLACK'),
        'NOIR': ('DIM', 'BLACK'),
        'CHARCOAL': ('NORMAL', 'BLACK'),
        'COAL': ('NORMAL', 'BLACK'),
        'CHARBON': ('NORMAL', 'BLACK'),
        'GRAY': ('BRIGHT', 'BLACK'),
        'GREY': ('BRIGHT', 'BLACK'),
        'GRIS': ('BRIGHT', 'BLACK'),
        'SILVER': ('DIM', 'WHITE'),
        'ARGENT': ('DIM', 'WHITE'),
        'WHITE': ('BRIGHT', 'WHITE'),
        'BLANC': ('BRIGHT', 'WHITE'),

        'BURGUNDY': ('DIM', 'RED'),
        'BORDEAUX': ('DIM', 'RED'),
        'RED': ('NORMAL', 'RED'),
        'ROUGE': ('NORMAL', 'RED'),

        'OLIVE': ('DIM', 'GREEN'),
        'GREEN': ('NORMAL', 'GREEN'),
        'VERT': ('NORMAL', 'GREEN'),
        'MINT': ('BRIGHT', 'GREEN'),
        'MENTHE': ('BRIGHT', 'GREEN'),
        'LIME': ('BRIGHT', 'GREEN'),
        'CIRTON VERT': ('BRIGHT', 'GREEN'),

        'ORANGE': ('DIM', 'YELLOW'),
        'BROWN': ('DIM', 'YELLOW'),
        'MARRON': ('DIM', 'YELLOW'),
        'OCHRE': ('DIM', 'YELLOW'),
        'OCRE': ('DIM', 'YELLOW'),
        'GOLD': ('NORMAL', 'YELLOW'),
        'OR': ('NORMAL', 'YELLOW'),
        'MUSTARD': ('NORMAL', 'YELLOW'),
        'MOUTARDE': ('NORMAL', 'YELLOW'),
        'YELLOW': ('BRIGHT', 'YELLOW'),
        'JAUNE': ('BRIGHT', 'YELLOW'),

        'NAVY BLUE': ('DIM', 'BLUE'),
        'BLEU MARINE': ('DIM', 'BLUE'),
        'BLUE': ('NORMAL', 'BLUE'),
        'BLEU': ('NORMAL', 'BLUE'),

        'INDIGO': ('DIM', 'MAGENTA'),
        'PURPLE': ('NORMAL', 'MAGENTA'),
        'VIOLET': ('NORMAL', 'MAGENTA'),
        'POURPRE': ('NORMAL', 'MAGENTA'),
        'MAGENTA': ('BRIGHT', 'MAGENTA'),
        'PINK': ('BRIGHT', 'MAGENTA'),
        'ROSE': ('BRIGHT', 'MAGENTA'),
        'FUCHSIA': ('BRIGHT', 'MAGENTA'),

        'TEAL': ('DIM', 'CYAN'),
        'BLEU CANARD': ('DIM', 'CYAN'),
        'CANARD': ('DIM', 'CYAN'),
        'SKY BLUE': ('NORMAL', 'CYAN'),
        'BLEU CIEL': ('NORMAL', 'CYAN'),
        'CYAN': ('BRIGHT', 'CYAN'),
        'TURQUOISE': ('BRIGHT', 'CYAN'),
    }
    color = str(color).strip().upper()
    if color not in colors:
        raise KeyError(f'{color} is not a color that is part of the {set(colors)} list')
    return colors[color]


def colorize(color, text, *, kind='fg'):
    """
    ** Adds the flags that allow to format the color text. **

    Parameters
    ----------
    color : str or tuple
        Either the name of the color in str,
        or the result of the function ``_str_to_color``.
    text : str
        The text to be formatted.
    kind : str, optional
        Decides whether to format the background or the text. 'fg' or 'bg'.

    Returns
    -------
    formatted_text : str
        The formatted text with the start and end flag.
    """
    if not isinstance(color, tuple):
        color = _str_to_color(color)
    style = getattr(colorama.Style, color[0])
    if kind == 'fg':
        color_tag = getattr(colorama.Fore, color[1])
    elif kind == 'bg':
        color_tag = getattr(colorama.Back, color[1])
    else:
        raise ValueError(f"'kind' can only take the values 'fg' or 'bg', not '{kind}'")
    reset_tag = colorama.Style.RESET_ALL
    return style + color_tag + text + reset_tag


def format_text(text, **formatting):
    r"""
    ** Format the text with the provided parameters. **

    Parameters
    ----------
    text : str
        Text to be printed. It should be in a single line (no \n character).
    color : str, optional
        The color of the text (only applies to this message).
    bg : str, optional
        The background highlight color (only applies to this message).
    blink : boolean, optional
        If set to True, the line will be blinking (not compatible with all consoles).
    bold : boolean, optional
        If set to true, prints the text in boldface.
    underline : boolean, optional
        If set to true, prints the text underlined.

    Examples
    --------
    >>> from context_printer.color import format_text
    >>> format_text('text')
    'text'
    >>>
    """
    if 'color' in formatting:
        text = colorize(formatting['color'], text)
    if 'bg' in formatting:
        text = colorize(formatting['bg'], text, kind='bg')
    if formatting.get('blink', False):
        text = '\033[5m' + text + '\033[0m'
    if formatting.get('bold', False):
        text = '\033[1m' + text + '\033[0m'
    if formatting.get('underline', False):
        text = '\033[4m' + text + '\033[0m'
    return text


def get_section_header(header_car='█ ', *, partial=False):
    """
    ** Retrieves the tag from the beginning of the current section. **
    """
    header = ''
    for context in get_lifo().lifo[-2::-1] if not partial else get_lifo().lifo[-2:0:-1]:
        header += format_text(header_car, **context)
    if partial:
        header += ' '*len(header_car)
    return header
