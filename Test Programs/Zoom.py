from tkinter import *

root = Tk()

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()


TRANSCOLOUR = "gray"


w = Canvas(root, width=WIDTH, height=HEIGHT,highlightthickness=0)
w.pack()

w.config(cursor='tcross')
w.create_rectangle(300, 300, WIDTH, HEIGHT, fill=TRANSCOLOUR,outline=TRANSCOLOUR)


root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", 0.5)
root.mainloop()