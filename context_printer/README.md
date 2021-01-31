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

The above example will print the following:\
\
![alt text](https://github.com/ValerianRey/ContextPrinter/blob/main/images/ctp_1.png "Basic example output")
