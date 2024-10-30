import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import matplotlib.image as img

def val(value):
    print(value)
    print(np.max(img))
    print(np.min(img))
    imgn = float(value) * img
    print(imgn.shape)
    image = ImageTk.PhotoImage(image=Image.fromarray(imgn))
    label.config(image=image)
    label.image = image
root = tk.Tk()
root.title("Display Image in Tk")
root.geometry("800x800")

# Load image from disk.
#image = tk.PhotoImage(file="img.png")

array = np.ones((40,40))*150

global img

imgM = img.imread('img.png')
print(type(imgM))
print(imgM.shape)

img = imgM[:,:,0]
img = 255.*img

print(img.shape)
print(np.max(img))
print(np.min(img))

image = ImageTk.PhotoImage(image=Image.fromarray(img))

print(type(image))
print(dir(image))


Scala = tk.Scale(root, from_=0, to=4, resolution=0.01, command=val)
#Scala.pack(padx=5, pady=5)

Scala.place(x=5, y=70) 


# Display it within a label.
label = ttk.Label(image=image)
label.place(x=70, y=70)

root.mainloop()


