Python library to improve console printing by adding context to your prints. It makes your console much cleaner, and you won't have to worry about making your prints beautiful.

Installation:
> pip install context_printer

Basic usage example:
```python
from context_printer import ContextPrinter as Ctp

Ctp.enter_section('Main section', color='blue')
Ctp.print('Text in main section')
for i in range(3):
    Ctp.enter_section('Subsection {}'.format(i + 1))
    Ctp.print('Text in subsection')
    Ctp.print('Text in subsection')
    Ctp.exit_section()
Ctp.exit_section()
```

Advanced usage example, using contexts and automatic line skips when exiting sections:
```python
from context_printer import ContextPrinter as Ctp

Ctp.set_automatic_skip(True)


with Ctp("Main section", color="blue"):
    Ctp.print('Text in main section')
    for i in range(3):
        with Ctp(f"Subsection {i + 1}"):
            Ctp.print('Text in subsection')
            Ctp.print('Text in subsection')
```

The above example will print the following:\
\
![alt text](https://github.com/ValerianRey/ContextPrinter/blob/main/images/ctp_1.png "Basic example output")

> Warning: This library is not maintained anymore and its implementation uses questionable python
> tricks. It is advised for anyone interested in continuing it to figure out a better implementation
> and to start over with an entirely new project.