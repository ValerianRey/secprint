import numpy as np
from secprint import SectionPrinter as Spt
from secprint import Color

arr = np.array([2, 4, 6])
Spt.enter_section(arr, Color.RED)
Spt.print(arr)
Spt.print(arr)
Spt.print(arr)

for color in Color:
    Spt.print(color + "text" + Color.END)
