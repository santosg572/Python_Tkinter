#from tkinter import *
#from tkinter import ttk

import tkinter as tk

def calculate(*args):
     value = float(feet.get())
     meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
     print(value)

root = tk.Tk()
root.title("convierte pies a metros")

lin1 = tk.Frame(root)

tk.Label(lin1, text="       ", width=7).pack( side = tk.LEFT )
 
feet = tk.StringVar()
feet_entry = tk.Entry(lin1, width=7, textvariable=feet)
feet_entry.pack( side = tk.LEFT )

tk.Label(lin1, text="feet").pack( side = tk.LEFT)

lin2 = tk.Frame(root)

tk.Label(lin2, text="is equivalent to").pack( side = tk.LEFT)
meters = tk.StringVar()

tk.Label(lin2, textvariable=meters,  width=7).pack( side = tk.LEFT)
tk.Label(lin2, text="meters").pack( side = tk.LEFT)


lin3 = tk.Frame(root)

tk.Label(lin3, text="       ", width=7).pack( side = tk.LEFT )
tk.Label(lin3, text="       ", width=7).pack( side = tk.LEFT )
tk.Button(lin3, text="Calculate", command=calculate).pack( side = tk.LEFT )

lin3.pack( side = tk.BOTTOM )
lin2.pack( side = tk.BOTTOM )
lin1.pack( side = tk.BOTTOM )

root.mainloop()


