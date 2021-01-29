from context_printer import ContextPrinter as Ctp
from context_printer import Color

Ctp.print('Hello', color=Color.GREEN)

Ctp.enter_section('Section', color='dark_green')
Ctp.print('Hello', color='red')
Ctp.print('Hello', color='red')
Ctp.print('Hello', color='red')
Ctp.print('Hello', color='red')
Ctp.print('Hello', color='red')
Ctp.enter_section('Section2', color='dark_gray')

Ctp.print('Hello', color='black')
Ctp.print('Hello', color='none')
Ctp.print('Hello', color='white')
Ctp.print('Hello', color='')
Ctp.print('Hello')
