import numpy as np
from context_printer import ContextPrinter as Ctp
from context_printer import Color

arr = np.array([2, 4, 6])
# Ctp.enter_section(arr, Color.RED)
with Ctp("Entering new section", color="blue"):
    Ctp.print(arr)
    Ctp.print(arr)
    Ctp.print(arr)

    for color in Color:
        Ctp.print(color + "text" + Color.END)
