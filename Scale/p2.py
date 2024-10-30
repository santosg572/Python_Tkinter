from tkinter import *
def Scale_select():
selected_value = "Value = " + str(var.get())
label.config(text = selected_value)
root = Tk()
var = DoubleVar()
scale_widget_variable = Scale( root,
activebackground = "red",
bg="grey",
bd=10,
digits=5,
troughcolor="yellow",
fg="Black",
label="Acurracy Score",
length=150,
orient="horizontal",
resolution=10,
variable = var )
scale_widget_variable.pack()
button = Button(root, text="Display scale value", command=Scale_select)
button.pack()
label = Label(root)
label.pack()
root.mainloop()

