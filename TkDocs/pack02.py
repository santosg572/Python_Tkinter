import tkinter as tk

root = tk.Tk()

ff = tk.Frame(root)
ff.pack()

redbutton = tk.Button(ff, text="Red", fg="red")
redbutton.pack( side = tk.LEFT)

greenbutton = tk.Button(ff, text="Brown", fg="brown")
greenbutton.pack( side = tk.LEFT )

bluebutton = tk.Button(ff, text="Blue", fg="blue")
bluebutton.pack( side = tk.LEFT )

blackbutton = tk.Button(ff, text="Black", fg="black")
blackbutton.pack( side = tk.BOTTOM)

blackbutton2 = tk.Button(ff, text="Black2", fg="black")
blackbutton2.pack( side = tk.BOTTOM)


root.mainloop()


