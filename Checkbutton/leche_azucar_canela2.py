from tkinter import *

def seleccionar():
    cadena = ""
    
    if (solo.get()):
        cadena = "café solo"
    else:
      if (leche.get()):
          cadena += "Con leche"
      else:
          cadena += "Sin leche"

      if (azucar.get()):
          cadena += " y con azúcar"
      else:
          cadena += " y sin azúcar"

      if (canela.get()):
          cadena += " y con canela"
      else:
          cadena += " y sin canel"

    monitor.config(text=cadena)

# Configuración de la raíz

root = Tk()
root.title("Cafetería")
root.config(bd=15)

leche = IntVar()    # 1 si, 0 no
azucar = IntVar()   # 1 si, 0 no
solo = IntVar()
canela = IntVar()

imagen = PhotoImage(file="leche.png")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, 
            offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1, 
            offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con canela", variable=canela, onvalue=1,
            offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="solo", variable=solo, onvalue=1,
            offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()

