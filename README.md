Python library to improve console printing by adding context to your prints. It makes your console much cleaner, and you won't have to worry about making your prints beautiful.

> Warning: This library is not maintained anymore and its implementation uses questionable python
> tricks. It is advised for anyone interested in continuing it to figure out a better implementation
> and to start over with an entirely new project.
> A fork with more some additional features and more maintenance efforts is available at 
> https://pypi.org/project/context-verbose/

Installation:
```
pip install secprint
```

Basic usage example:

```python
from secprint import SectionPrinter as Spt

Spt.enter_section('Main section', color='blue')
Spt.print('Text in main section')
for i in range(3):
    Spt.enter_section('Subsection {}'.format(i + 1))
    Spt.print('Text in subsection')
    Spt.print('Text in subsection')
    Spt.exit_section()
Spt.exit_section()
```

The above example will print the following:\
\
![alt text](https://github.com/ValerianRey/ContextPrinter/blob/main/images/secprint_1.png "Basic example output")

Advanced usage example, using contexts and automatic line skips when exiting sections:

```python
from secprint import SectionPrinter as Spt

Spt.set_automatic_skip(True)

with Spt("Main section", color="blue"):
    Spt.print('Text in main section')
    for i in range(3):
        with Spt(f"Subsection {i + 1}"):
            Spt.print('Text in subsection')
            Spt.print('Text in subsection')
```

The above example will print the following:\
\
![alt text](https://github.com/ValerianRey/ContextPrinter/blob/main/images/secprint_2.png "Basic example output")
