#from tkinter import *
#from tkinter import ttk

import tkinter as tk

def calculate(*args):
     value = float(feet.get())
     meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
     print(value)

root = tk.Tk()
root.title("convierte pies a metros")

feet = tk.StringVar()
feet_entry = tk.Entry(root, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1) 

meters = tk.StringVar()
tk.Label(root, textvariable=meters).grid(column=2, row=2)

tk.Button(root, text="Calculate", command=calculate).grid(column=3, row=3)


tk.Label(root, text="feet").grid(column=3, row=1)

tk.Label(root, text="is equivalent to").grid(column=1, row=2)
tk.Label(root, text="meters").grid(column=3, row=2)

root.mainloop()


