#from tkinter import *
#from tkinter import ttk

import tkinter as tk

def calculate(*args):
     value = float(feet.get())
     meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
     print(value)

root = tk.Tk()
root.title("convierte pies a metros")
root.geometry('300x200') 

x1 = 100
feet = tk.StringVar()
feet_entry = tk.Entry(root, width=7, textvariable=feet)
feet_entry.place(x=x1, y=10)

tk.Label(root, text="feet").place(x=x1+90, y=10)

tk.Label(root, text="is equivalent to").place(x=5, y=35)

meters = tk.StringVar()
tk.Label(root, textvariable=meters, width=7).place(x=120, y=35)  

tk.Label(root, text="meters").place(x=200, y=35)    

tk.Button(root, text="Calculate", command=calculate).place(x=200, y=60)

'''
meters = tk.StringVar()
tk.Label(root, textvariable=meters).grid(column=2, row=2)

tk.Button(root, text="Calculate", command=calculate).grid(column=3, row=3)


tk.Label(root, text="is equivalent to").grid(column=1, row=2)
tk.Label(root, text="meters").grid(column=3, row=2)
'''

root.mainloop()


