import tkinter as tk
ventana = tk.Tk()
ventana.geometry("400x300")
listbox = tk.Listbox()
listbox.insert(tk.END, *(f"Elemento {i}" for i in range(100)))
listbox.pack()
ventana.mainloop()

