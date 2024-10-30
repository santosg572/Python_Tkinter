import tkinter as tk

def load_text():
    with open('file.txt', 'r') as file:
        data = file.read()
        text_widget.insert(tk.END, data)

root = tk.Tk()
text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()

load_text()

root.mainloop()

