import tkinter as tk

canvas = tk.Canvas(width=400, height=300, bg='white')
canvas.pack(expand= tk.YES, fill= tk.BOTH)
canvas.create_line(10, 10, 80, 80, fill='red')
canvas.create_line(10, 80, 80, 10, fill='blue')
canvas.create_oval(300,210,400,350, outline="red")

tk.mainloop()


