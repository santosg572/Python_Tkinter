import tkinter as tk
from tkinter import messagebox, ttk
def saludar():
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")
def saludar_enter(event):
    saludar()
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = tk.Button(text="¡Hola, mundo!", command=saludar)
boton.bind("<Return>", saludar_enter)
boton.place(x=50, y=50)
root.mainloop()

