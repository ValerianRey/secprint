Python library to improve console printing by adding context to your prints. It makes your console much cleaner, and you won't have to worry about making your prints beautiful.

Installation:
> pip install context_printer

Basic usage example:
```python
from context_printer import ctp

@ctp
def decorated_func(x):
    return x**x**x

def error_func():
    with ctp('Section that will fail'):
        return 1/0

ctp.print('we will enter the main section')
with ctp('Main Section', color='cyan'):
    ctp.print('text in main section')
    try:
        with ctp('Subsection 1'):
            for x in [1, 8]:
                decorated_func(x)
            error_func()
    except ZeroDivisionError:
        pass
    with ctp('Subsection 2', color='magenta'):
        ctp.print('text in bold', bold=True)
        ctp.print('underlined text', underline=True)
        ctp.print('blinking text', blink=True)
        ctp.print('yellow text', color='yellow')
        ctp.print('text highlighted in blue', bg='blue')
        ctp.print('text in several ', end='')
        ctp.print('parts', print_headers=False)
        ctp.print('''text in several
                     lines''')
    with ctp(color='green'):
        ctp.print('this subsection is automatically named')
ctp.print('we are out of the main section')
```

The above example will print the following:\
\
![alt text](https://github.com/robinechuca/ContextPrinter/blob/main/images/ctp_0.png "Basic example output")
