import pyautogui   # import PyAutoGUI library
  # import tkinter library
from PIL import Image, ImageTk
from tkinter import *
# create main window
root = Tk()
images = []

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
TRANSCOLOUR = "gray"

root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", TRANSCOLOUR)
root.wm_attributes("-fullscreen")
w = Canvas(root, width=width, height=height)
w.pack()

w.config(cursor='tcross')

# define a method that will call whenever button will be clicked
def take():
    image = pyautogui.screenshot()
    image = image.tobitmap()
    w.create_bitmap(0, 0,background=TRANSCOLOUR)

# create a button 
shot_btn = Button(root,text = "Take Screenshot", command= take)

# place the button on the window
shot_btn.place(x=50, y=50)
root.mainloop()