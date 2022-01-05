#!/usr/bin/env python3

"""
** High level API for contextual verbosity. **
----------------------------------------------

The *Printer* class allows the user to nest multiple
display blocks without worrying about indentation levels.
"""

import inspect
import time

from context_printer.memory import get_lifo
from context_printer.color import get_section_header, colorize, format_text


class Printer:
    """
    ** Main class, only the instance is manipulated. **

    Examples
    --------
    >>> from context_printer.memory import reset_lifo
    >>> reset_lifo()
    >>> from context_printer.printer import Printer
    >>>
    >>> with Printer('Main section') as ctp:
    ...     ctp.print('Text in main section')
    ...     for i in range(3):
    ...         with ctp(f'Subsection {i+1}'):
    ...             ctp.print('Text in subsection')
    ...             ctp.print('Text in subsection')
    ...
    Main section
    █ Text in main section
    █ Subsection 1
    █ █ Text in subsection
    █ █ Text in subsection
    █ Subsection 2
    █ █ Text in subsection
    █ █ Text in subsection
    █ Subsection 3
    █ █ Text in subsection
    █ █ Text in subsection
    """

    def __new__(cls, title=None, **formatting):
        """
        ** Guarantees the uniqueness of an instance of this class. **

        Parameters
        ----------
        title : str, optional
            Forwarded to ``Printer.__call__``.
        formatting : dict
            Forwarded to ``Printer.__call__``.

        Notes
        -----
        Uniqueness only occurs within the same process.

        Examples
        --------
        >>> from context_printer import Printer
        >>> c1 = Printer()
        >>> c2 = Printer()
        >>> c1 is c2
        True
        >>>
        """
        if 'context_printer' not in globals():
            globals()['context_printer'] = super(Printer, cls).__new__(cls)
        return globals()['context_printer'](title, **formatting)

    def enter_section(self, title=None, **formatting):
        """
        ** Opens a new section. **

        Parameters
        ----------
        title : str, optional
            The name of the new section.
        **formatting : dict
            Text formatting parameters. These settings will affect
            not only this section but also all child sections.

        Examples
        --------
        >>> from context_printer.memory import reset_lifo
        >>> reset_lifo()
        >>> from context_printer.printer import Printer
        >>> ctp = Printer()
        >>> ctp.enter_section() # doctest: +SKIP
        Section __run l1336 in /usr/lib/python3.8/doctest.py
        >>> reset_lifo()
        >>> ctp.enter_section('Section')
        Section
        >>>
        """
        if not get_lifo().get_layer().get('title', False):
            get_lifo().update_future_layer(**formatting)
            if title is None:
                try:
                    frame = inspect.currentframe().f_back.f_back
                except AttributeError:
                    frame = inspect.currentframe().f_back
                if frame.f_code.co_name == '<module>':
                    title = f'Section l{frame.f_lineno} in {frame.f_code.co_filename}'
                else:
                    title = (
                        f'Section {frame.f_code.co_name} l{frame.f_lineno} '
                        f'in {frame.f_code.co_filename}'
                    )

            self.print(title, **{**get_lifo().get_layer(), **get_lifo().future_context, **formatting})
        elif title is not None:
            raise NameError('there is already a title in this section')
        get_lifo().add_layer(**formatting, title=False)

    @staticmethod
    def exit_section():
        """
        ** Exits the current section to return to the parent section. **
        """
        get_lifo().remove_layer()
        get_lifo().update_layer(title=False)

    @staticmethod
    def print(message, *, print_headers=True, rewrite=False, end='\n', **formatting):
        r"""
        ** Displays the message with the formatting of the current section. **

        Parameters
        ----------
        message : str
            The message to display
        print_headers : boolean, optional
            If set to true, all section headers will be printed before the text.
        rewrite : boolean, optional
            If set to true, rewrites over the current line instead of printing a new line.
        end : str, default='\n'
            Character to print at the end of the line.
        **formatting : dict
            The text formatting parameters are passed to the
            ``context_printer.color.format_text`` function.
            They apply only to this message, they do not affect future messages.

        Examples
        --------
        >>> from context_printer.memory import reset_lifo
        >>> reset_lifo()
        >>> from context_printer.printer import Printer
        >>> ctp = Printer()
        >>> ctp.print('a simple message')
        a simple message
        >>> ctp.print('this is a\nmulti-line message')
        this is a
          multi-line message
        >>> with ctp('Section'):
        ...     ctp.print('a simple message')
        ...     ctp.print('this is a\nmulti-line message')
        ...     ctp.print('start of the message ', end='')
        ...     ctp.print('end of message', print_headers=False)
        ...
        Section
        █ a simple message
        █ this is a
          multi-line message
        █ start of the message end of message
        >>>
        """
        if get_lifo().get_layer().get('title', False):
            raise NameError('there can be a maximum of one title per section')

        if rewrite:
            print('\r', end='')
        messages = message.split('\n')
        _end = '\n'
        for i, mes in enumerate(messages):
            mes = format_text(mes.lstrip(), **formatting)
            if print_headers:
                print(get_section_header(partial=(i!=0)), end='')
            if i == len(messages)-1:
                _end = end
            print(mes, end=_end)

    @staticmethod
    def elapsed_time():
        """
        ** Displays the time elapsed since the entry in the section. **

        Parameters
        ----------
        **formatting : dict
            Text formatting parameters. They apply only to this message.

        Examples
        --------
        >>> from context_printer.memory import reset_lifo
        >>> reset_lifo()
        >>> from context_printer.printer import Printer
        >>> with Printer('Section') as ctp:
        ...     t = ctp.elapsed_time()
        ...
        Section
        >>> t # doctest: +SKIP
        '1.91 us'
        >>>
        """
        delta_t = time.time() - get_lifo().get_layer()['time']
        unit = 's'
        if delta_t < 1:
            delta_t *= 1000
            unit = 'ms'
        if delta_t < 1:
            delta_t *= 1000
            unit = 'us'
        return f'{delta_t:.2f} {unit}'

    def __call__(self, title_or_func=None, **formatting):
        """
        ** Update the parameters of the section. **

        Parameters
        ----------
        title_or_func : str or callable, optional
            The message to display. None allows to display nothing at all.
            Otherwise, it can be the function to decorate.
        **formatting : dict
            Text formatting new parameters. These settings will affect
            not only this section but also all child sections.

        Returns
        -------
        self : Printer
            Returns itself around for compatibility with *with*.
        """
        if isinstance(title_or_func, str):
            self.print(title_or_func, **{**get_lifo().get_layer(), **formatting})
            get_lifo().update_layer(title=True)
        elif hasattr(title_or_func, '__call__'):
            from context_printer.decorator import decorate
            return decorate(title_or_func)
        elif title_or_func is not None:
            raise TypeError(
                f'the parameter must be str or function, not {title_or_func.__class__.__name__}'
            )
        get_lifo().update_future_layer(**formatting)
        return self

    def __enter__(self):
        self.enter_section()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.print(
                f"{colorize('red', exc_type.__name__, kind='bg')} l{exc_tb.tb_lineno} ({exc_val})"
            )
        self.exit_section()
