#!/usr/bin/env python3

"""
** High level API for contextual verbosity. **
----------------------------------------------

The *Printer* class allows the user to nest multiple
display blocks without worrying about indentation levels.
"""

import inspect

from context_printer.memory import get_lifo
from context_printer.color import get_section_header, colorize


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
                    title = f'Section {frame.f_code.co_name} l{frame.f_lineno} in {frame.f_code.co_filename}'

            self.print(title, **{**get_lifo().get_layer(), **formatting})
        elif title is not None:
            raise NameError('there is already a title in this section')
        get_lifo().add_layer(**formatting)

    def exit_section(self):
        """
        ** Exits the current section to return to the parent section. **
        """
        get_lifo().remove_layer()
        get_lifo().update_layer(title=False)

    def print(self, message, end='\n', **formatting):
        """
        ** Displays the message with the formatting of the current section. **

        Parameters
        ----------
        message : str
            The message to display
        end : str
            The end character is by default a line break.
            It is for example possible to put '' to have
            different text formatting on the same line.
        **formatting : dict
            Text formatting parameters. They apply only to this message.
        """
        # TODO : gérer les retours à la ligne
        section_header = get_section_header()
        print(section_header, end='')
        if 'color' in formatting:
            message = colorize(formatting['color'], message)
        if 'bg' in formatting:
            message = colorize(formatting['bg'], message, kind='bg')
        print(message, end=end)

    def __call__(self, title=None, **formatting):
        """
        ** Update the parameters of the section. **

        Parameters
        ----------
        title : str, optional
            The message to display. None allows to display nothing at all.
        **formatting : dict
            Text formatting new parameters. These settings will affect
            not only this section but also all child sections.

        Returns
        -------
        self : Printer
            Returns itself around for compatibility with *with*.
        """
        get_lifo().update_layer(title=True)
        get_lifo().update_future_layer(**formatting)
        if title is not None:
            self.print(title, **{**get_lifo().get_layer(), **formatting})
        return self

    def __enter__(self):
        self.enter_section()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # TODO : afficher le message d'erreur
            pass
        self.exit_section()
