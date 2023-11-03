from secprint import SectionPrinter as Spt
from secprint import Color


for val in range(0, 8):
    print(str(val) + ' - \033[' + str(val+30) + 'm' + 'Hello--fezafija' + Color.END)
    print(str(val) + ' - \033[' + str(val + 90) + 'm' + 'Hello--fezafija' + Color.END)

print('\033[30mYOOOOO' + Color.END)
print('\033[90mYOOOOO' + Color.END)
print('\033[37mYOOOOO' + Color.END)
print('\033[97mYOOOOO' + Color.END)

print()