from tkinter import *
import tkinter

win = Tk()

mbtn = Menubutton(win, text="Courses", relief=RAISED)
mbtn.grid()
mbtn.menu = Menu(mbtn, tearoff = 0)
mbtn["menu"] = mbtn.menu

pythonVar = IntVar()
javaVar = IntVar()
phpVar = IntVar()

mbtn.menu.add_checkbutton(label="Python", variable=pythonVar)
mbtn.menu.add_checkbutton(label="Java", variable=javaVar)
mbtn.menu.add_checkbutton(label="PHP", variable=phpVar)

mbtn.pack()
win.mainloop()

