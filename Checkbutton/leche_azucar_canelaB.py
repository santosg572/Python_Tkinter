import tkinter as tk

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text=cadena)

# Configuración de la raíz
root = tk.Tk()
root.title("Cafetería")

leche = tk.IntVar()    # 1 si, 0 no
azucar = tk.IntVar()   # 1 si, 0 no

imagen = tk.PhotoImage(file="leche.png")
tk.Label(root, image=imagen).pack(side="left")

frame = tk.Frame(root)
frame.pack(side="left")

tk.Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
tk.Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, 
            offvalue=0, command=seleccionar).pack(anchor="w")
tk.Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1, 
            offvalue=0, command=seleccionar).pack(anchor="w")

monitor = tk.Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()

