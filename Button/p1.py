import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")

boton = tk.Button(text="¡Hola, mundo!", activebackground='red')

boton.place(x=50, y=50)
root.mainloop()

