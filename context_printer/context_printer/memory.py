#!/usr/bin/env python3

"""
** Global memory that coordinates all *ContextPrinter*. **
----------------------------------------------------------

It allows, depending on the process or thread,
to provide information such as the indentation level
and the text formatting parameters.
"""

import logging
import math
import multiprocessing
import sys
import tempfile
import threading
import time


DIR = tempfile.mkdtemp()


def get_id():
    """
    ** Retrieves information about processes and threads. **

    Returns
    -------
    context : dict
        * proc_name : str
            * The current process name, 'MainProcess' for the first process.
        * thread_name : str
            * The current thread name, 'MainThread' for the first thread.
        * father_proc : str or None
            * The father process name.

    Examples
    --------
    >>> import concurrent.futures
    >>> import multiprocessing
    >>> from context_printer.memory import get_id
    >>> get_id()
    {'proc_name': 'MainProcess', 'thread_name': 'MainThread', 'father_proc': None}
    >>> with concurrent.futures.ThreadPoolExecutor() as executor:
    ...     executor.submit(get_id).result()
    ...
    {'proc_name': 'MainProcess', 'thread_name': 'ThreadPoolExecutor-0_0', 'father_proc': None}
    >>> with multiprocessing.Pool() as pool:
    ...     pool.apply_async(get_id).get()
    ...
    {'proc_name': 'ForkPoolWorker-1', 'thread_name': 'MainThread', 'father_proc': 'MainProcess'}
    >>>
    """
    proc_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    try:
        father_proc = multiprocessing.parent_process()
    except AttributeError: # if python version < 3.8
        message = (
            'please use a version of python >= 3.8 if you do multiprocessing, your current version is '
            f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'
        )
        logging.warning(message)
        father_proc = None
    else:
        father_proc = father_proc.name if father_proc is not None else None
    return {'proc_name': proc_name, 'thread_name': thread_name, 'father_proc': father_proc}


def get_lifo():
    """
    ** Retrieves the context for immediate display. **

    Automatically manages the creation of a new queue instance
    according to the current process and the current thread.
    In short, inter-thread conflicts are handled automatically here.

    Returns
    -------
    lifo : LIFO
        The instantiated memory stack associated with the correct context.

    Examples
    --------
    >>> from context_printer.memory import get_lifo, reset_lifo
    >>> reset_lifo()
    >>>
    >>> # case in main process and main thread
    >>> print(get_lifo())
    LIFO(father_proc=None, proc_name='MainProcess', thread_name='MainThread'):
    |Layer()
    >>> get_lifo().add_layer(color='red')
    >>> print(get_lifo())
    LIFO(father_proc=None, proc_name='MainProcess', thread_name='MainThread'):
    |Layer()
    |---|Layer(color='red')
    >>>
    >>> # case in main process and secondary thread
    >>> import concurrent.futures
    >>> with concurrent.futures.ThreadPoolExecutor() as executor:
    ...     print(executor.submit(get_lifo).result())
    ...
    LIFO(father_proc=None, proc_name='MainProcess', thread_name='ThreadPoolExecutor-1_0'):
    |Layer(color='red')
    >>>
    >>> # case in a child process
    >>> with multiprocessing.Pool() as pool:
    ...     print(pool.apply_async(get_lifo).get())
    ...
    LIFO(father_proc='MainProcess', proc_name='ForkPoolWorker-9', thread_name='MainThread'):
    |Layer(color='red')
    >>>
    """
    context = get_id()

    if f"_global_fifo_{context['proc_name']}" in globals():
        if context['thread_name'] in globals()[f"_global_fifo_{context['proc_name']}"]:
            # case where the queue is already instantiated
            return globals()[f"_global_fifo_{context['proc_name']}"][context['thread_name']]
        # case where a thread must be instantiated
        globals()[f"_global_fifo_{context['proc_name']}"][context['thread_name']] = globals()[
            f"_global_fifo_{context['proc_name']}"
        ]['MainThread'].fork()
        return get_lifo()

    # case where it is necessary to instantiate the main queue
    if context['proc_name'] == 'MainProcess':
        globals()[f"_global_fifo_{'MainProcess'}"] = {'MainThread': LIFO()}
        return get_lifo()

    # case in a child process
    if f"_global_fifo_{context['father_proc']}" not in globals():
        message = (
            f"the process '{context['proc_name']}' "
            f"has not inherited the process '{context['father_proc']}', "
            "use the method 'fork' to create processes"
        )
        logging.warning(message)
        globals()[f"_global_fifo_{context['father_proc']}"] = {'MainThread': LIFO()}
    globals()[f"_global_fifo_{context['proc_name']}"] = {
        'MainThread': globals()[f"_global_fifo_{context['father_proc']}"]['MainThread'].fork()
    }
    return get_lifo()


def reset_lifo():
    """
    ** Removes all traces of memory. **
    """
    for name in [n for n in globals() if n.startswith('_global_fifo_')]:
        del globals()[name]


class LIFO:
    """
    ** Allows to transfer parameters between blocks. **

    There must be one instance per process.
    The function of this class is to be able to store
    the parameters for each indentation.
    """

    def __init__(self, max_depth=math.inf, **init_context):
        """
        Parameters
        ----------
        init_context : dict
            The initial setup.
        """
        self.context = get_id()
        self.lifo = [init_context]
        self.future_context = {}
        self.max_depth = max_depth

    def add_layer(self, **new_context):
        """
        ** Adds an indentation level and updates the new parameters. **

        Parameters
        ----------
        new_context : dict
            The parameters that change between the previous and the new layer.
            All unspecified parameters inherit from the previous layer.

        Examples
        --------
        >>> from context_printer.memory import LIFO
        >>> queue = LIFO(color='green', toto=True)
        """
        self.lifo.insert(0, {**self.lifo[0], **self.future_context, **new_context})
        self.lifo[0]['time'] = time.time()
        self.future_context = {}

    def get_layer(self, _is_title=False):
        r"""
        ** Retrieves the context of the current layer. **

        This method does not modify the state of the object.

        Returns
        -------
        context : dict
            The context of the current layer.
            Also contains the field *indent* which corresponds
            to the depth level of this layer.

        Examples
        --------
        >>> from context_printer.memory import LIFO
        >>> def p(dico):
        ...     print('{'
        ...         + ', '.join(f'{repr(k)}: {repr(dico[k])}' for k in sorted(dico) if k!='time')
        ...         + '}')
        ...
        >>> queue = LIFO()
        >>> p(queue.get_layer())
        {'display': True, 'indent': 0}
        >>> queue.add_layer(titi=True)
        >>> p(queue.get_layer())
        {'display': True, 'indent': 1, 'titi': True}
        >>> queue.add_layer(toto=False)
        >>> p(queue.get_layer())
        {'display': True, 'indent': 2, 'titi': True, 'toto': False}
        >>>
        """
        context = self.lifo[0].copy()
        context['indent'] = len(self.lifo) - 1
        context['display'] = self.max_depth >= context['indent'] + int(_is_title)
        return context

    def remove_layer(self):
        """
        ** Removes the last layer. **

        Raises
        ------
        IndentationError
            If there is no layer left to remove.
        """
        if len(self.lifo) <= 1:
            raise IndentationError('there are no more layers to remove')
        del self.lifo[0]

    def update_layer(self, **new_context):
        """
        ** Changes the value of the parameters of the current layer. **

        Parameters
        ----------
        new_context : dict
            The new layer parameters.
            All unspecified parameters inherit from the previous layer.
        """
        self.lifo[0] = {**self.lifo[0], **new_context}

    def update_future_layer(self, **new_context):
        """
        ** Changes the of the parameters of the current layer. **

        Parameters
        ----------
        new_context : dict
            The new layer parameters.
            All unspecified parameters inherit from the previous layer.
        """
        self.future_context = {**self.future_context, **new_context}

    def fork(self, **init_context):
        """
        ** Generates a new queue for a new process or thread. **

        The parameters of the first layer of the new queue
        inherit those of the last layer of the current queue.

        Parameters
        ----------
        init_context : dict
            The initial setup of the forked queue.
        """
        return LIFO(max_depth=self.max_depth, **self.lifo[0], **init_context)

    def set_max_depth(self, value):
        """
        ** Sets a maximum number of nested sections. **

        alias to ``context_printer.printer.Printer.set_max_depth``
        """
        self.max_depth = value

    def __str__(self):
        """
        ** Provides a debugging representation. **

        Examples
        --------
        >>> from context_printer.memory import LIFO
        >>> queue = LIFO()
        >>> queue.add_layer(titi=True)
        >>> queue.add_layer(toto=False)
        >>> print(queue)
        LIFO(father_proc=None, proc_name='MainProcess', thread_name='MainThread'):
        |Layer()
        |---|Layer(titi=True)
        |---|---|Layer(titi=True, toto=False)
        >>>
        """
        return f'{repr(self)}:\n' + '\n'.join(
            f'{"|---"*i}|Layer({", ".join(f"{k}={repr(c[k])}" for k in sorted(c) if k!="time")})'
            for i, c in enumerate(self.lifo[::-1])
        )

    def __repr__(self):
        """
        ** Provide a simple representation. **

        Examples
        --------
        >>> from context_printer.memory import LIFO
        >>> LIFO()
        LIFO(father_proc=None, proc_name='MainProcess', thread_name='MainThread')
        >>>
        """
        return f'LIFO({", ".join(f"{k}={repr(self.context[k])}" for k in sorted(self.context))})'
