from secprint import SectionPrinter as Spt
from secprint import Color

Spt.print('Hello', color=Color.GREEN)

Spt.enter_section('Section', color='dark_green')
Spt.print('Hello', color='red')
Spt.print('Hello', color='red')
Spt.print('Hello', color='red')
Spt.print('Hello', color='red')
Spt.print('Hello', color='red')
Spt.enter_section('Section2', color='dark_gray')

Spt.print('Hello', color='black')
Spt.print('Hello', color='none')
Spt.print('Hello', color='white')
Spt.print('Hello', color='')
Spt.print('Hello')
