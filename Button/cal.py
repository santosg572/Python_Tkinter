import tkinter as tk

from tkinter import ttk

root = tk.Tk()
root.config(width=500, height=200)
root.title("Botón en Tk")

boton1 = tk.Button(text="1")
boton1.place(x=0, y=0)

boton2 = tk.Button(text="2")
boton2.place(x=40, y=0)

boton3 = tk.Button(text="3")
boton3.place(x=80, y=0)


root.mainloop()

