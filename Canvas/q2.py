import tkinter as tk
import numpy as np

canvas = tk.Canvas(width=400, height=300, bg='white')
canvas.pack(expand= tk.YES, fill= tk.BOTH)

x = np.arange(0, 400, 1)

y = np.round(50*np.sin(x)) + 150

zz = []

k=0
for xx in x:
  zz.append(xx)
  zz.append(y[k])
  k = k+1

canvas.create_line(zz, fill='red')

tk.mainloop()


