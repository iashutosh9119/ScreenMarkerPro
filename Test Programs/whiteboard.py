from tkinter import *
import time

tk = Tk()
WIDTH = tk.winfo_screenwidth()
HEIGHT = tk.winfo_screenheight()
LINEWIDTH = 1
TRANSCOLOUR = 'gray'
tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))


tk.wm_attributes("-topmost", True)
tk.wm_attributes("-transparentcolor", TRANSCOLOUR)
tk.wm_attributes("-fullscreen")
tk.overrideredirect(True)
global old
old = ()

tk.title('Virtual whiteboard')
tk.wm_attributes('-transparentcolor', TRANSCOLOUR)
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.config(cursor='tcross')
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR,outline=TRANSCOLOUR)

canvas.create_bitmap(0, 0, background="")
def buttonmotion(evt):
    global old
    if old == ():
        old = (evt.x, evt.y)
        return
    else:
        canvas.create_line(old[0], old[1], evt.x, evt.y,fill="WHITE", width=5)
        old = (evt.x, evt.y)
def buttonclick(evt):
    global old
    canvas.create_line(evt.x-1, evt.y-1, evt.x, evt.y, width=LINEWIDTH)
    old = (evt.x, evt.y)
canvas.bind('<Button-1>', buttonmotion)
canvas.bind('<B1-Motion>', buttonclick)
while True:
    tk.update()
    time.sleep(0.01)
    tk.wm_attributes("-topmost", True)