from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.config(width=300, height=200)
root.title("Virtual Thermostat")
temp_label = ttk.Label(text="Temperature:")
temp_label.place(x=20, y=30, width=100)
spin_temp = ttk.Spinbox()
spin_temp.place(x=105, y=30, width=70)
root.mainloop()

