import tkinter as tk
from tkinter import messagebox

def saludar(button_press):
    print(button_press)
    if button_press == '1':
      let = 'Estamos en tierra'
    else:
      let = 'estamos en Via Láctea'

    messagebox.showinfo(message=let, title="Saludo")

root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")

boton1 = tk.Button(text="¡Hola, mundo!", command=lambda: saludar("1"))
boton1.place(x=50, y=50)

boton2 = tk.Button(text="¡Hola, galaxia!", command=lambda: saludar("2"))
boton2.place(x=50, y=75)

root.mainloop()


