#!/usr/bin/env python3

"""
** High level API for contextual verbosity. **
----------------------------------------------

The *ContextPrinter* class allows the user to nest multiple
display blocks without worrying about indentation levels.
"""

from context_printer.memory import get_lifo


class ContextPrinter:
    """
    ** Main class, only the instance is manipulated. **

    Examples
    --------
    >>> from context_printer.memory import reset_lifo
    >>> reset_lifo()
    >>> from context_printer.printer import ContextPrinter
    >>> with ContextPrinter('Main section', color='blue') as ctp:
    ...     ctp.print('Text in main section')
    ...     for i in range(3):
    ...         with ctp(f'Subsection {i+1}'):
    ...             ctp.print('Text in subsection')
    ...             ctp.print('Text in subsection')
    ...
    Main section
    |---Text in main section
    |---Subsection 1
    |---|---Text in subsection
    |---|---Text in subsection
    |---Subsection 2
    |---|---Text in subsection
    |---|---Text in subsection
    |---Subsection 3
    |---|---Text in subsection
    |---|---Text in subsection
    """

    def __new__(cls, title=None, **formatting):
        """
        ** Guarantees the uniqueness of an instance of this class. **

        Parameters
        ----------
        title : str, optional
            Forwarded to ``ContextPrinter.__call__``.
        formatting : dict
            Forwarded to ``ContextPrinter.__call__``.

        Notes
        -----
        Uniqueness only occurs within the same process.

        Examples
        --------
        >>> from context_printer import ContextPrinter
        >>> c1 = ContextPrinter()
        >>> c2 = ContextPrinter()
        >>> c1 is c2
        True
        >>>
        """
        if 'context_printer' not in globals():
            globals()['context_printer'] = super(ContextPrinter, cls).__new__(cls)
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
        if title is None:
            # TODO : metre un vrai titre, qui par example recupere le numéro de la ligne
            # ou bien le taux d'indentation... Un titre qui apporte de l'info quoi.
            title = 'New Section'
        # TODO : eviter d'afficher le titre en double
        else:
            self.print(title, **formatting)
        get_lifo().add_layer(**formatting)

    def exit_section(self):
        """
        ** Exits the current section to return to the parent section. **
        """
        get_lifo().remove_layer()

    def print(self, message, **formatting):
        """
        ** Displays the message with the formatting of the current section. **

        Parameters
        ----------
        message : str
            The message to display
        **formatting : dict
            Text formatting parameters. They apply only to this message.
        """
        context = {**get_lifo().get_layer(), **formatting}
        # TODO : gérer les retours à la ligne
        # TODO : faire un joli formattage du texte avec les couleurs et tout et tout...
        print(f"{'|---'*context['indent']}{message}")

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
        self : ContextPrinter
            Returns itself around for compatibility with *with*.
        """
        get_lifo().update_layer(**formatting)
        if title is not None:
            self.print(title)
        return self

    def __enter__(self):
        self.enter_section()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # TODO : afficher le message d'erreur
            pass
        self.exit_section()
