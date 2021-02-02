import numpy as np
from context_printer import ContextPrinter as Ctp

arr = np.array([2, 4, 6])
Ctp.enter_section(arr, 'red')
Ctp.print(arr)
Ctp.print(arr)
Ctp.print(arr)
