import tkinter as tk

root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = tk.Button(text="¡Hola, mundo!")
boton.place(x=50, y=50)
root.mainloop()

