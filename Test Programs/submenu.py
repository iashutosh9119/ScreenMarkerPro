from tkinter import *
from tkinter import filedialog
def Donothing():
    x = 0

root = Tk()

toolbox = Menu(root)

root.config(menu=toolbox)

menu = Menu(toolbox, tearoff=0)

submenu = Menu(menu, tearoff=0)

toolbox.add_cascade(label="File", menu=menu)

menu.add_cascade(label="Save", menu=submenu)

submenu.add_command(label="Save Nothing", command = Donothing)

menu.add_separator()
menu.add_command(label="Exit", command=root.quit)
root.mainloop()