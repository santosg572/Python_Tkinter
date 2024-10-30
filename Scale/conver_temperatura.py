from tkinter import * 
 
def val(value):
    print(value)
    Fahrenheit = round((float(value) * 1.8) + 32,3)
    print(Fahrenheit)
    label_var.set(str(Fahrenheit))

root = Tk()
root.geometry("400x400")

label = Label(root, text='Convertidor de Centígrados a Fahrenheit')
label.place(x=50, y=0)

#frame = Frame(root)
#frame.pack()
 
Scala = Scale(root, from_=0, to=100, command=val)
#Scala.pack(padx=5, pady=5)

Scala.place(x=10, y=70) 

#Scala2 = Scale(frame, from_=0, to=10, resolution = 0.5, command=val, orient=HORIZONTAL)
#Scala2.pack(padx=5, pady=5)

res = Label(root, text='CONVERSION: ')
res.place(x=100, y=70)

label_var = StringVar(root)
label_var.set('000')
res = Label(root, textvariable=label_var)                           
res.place(x=200, y=70)
 
root.mainloop()


