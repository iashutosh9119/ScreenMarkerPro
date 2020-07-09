from tkinter import *
import time
import win32gui
import win32api
from PIL import Image, ImageTk

LINEWIDTH = 1
TRANSCOLOUR = 'gray'
title = 'Virtual whiteboard'
global old
old = ()
global HWND_t
HWND_t = 0
pressed = False
tk = Tk()
tk.geometry("{0}x{1}+0+0".format(tk.winfo_screenwidth(), tk.winfo_screenheight()))
WIDTH = tk.winfo_screenwidth()
HEIGHT = tk.winfo_screenheight()




root = Tk()
root.wm_attributes('-fullscreen',True)
root.wm_attributes("-topmost", True)
root.wm_attributes('-alpha',0)

tk.title(title)
tk.lift()
tk.wm_attributes("-topmost", True)
tk.wm_attributes("-transparentcolor", TRANSCOLOUR)
tk.wm_attributes("-fullscreen",True)

x = 0
y = 0
cur_pos = (0,0,0,0)
pen_flag = False
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.config(cursor='tcross')
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)

def putOnTop(event):
    event.widget.unbind('<Visibility>')
    event.widget.update()
    event.widget.lift()
    event.widget.bind('<Visibility>', putOnTop)
def drawline(data):
    global old
    if old !=():
        canvas.create_line(old[0], old[1], data[0], data[1],fill="WHITE", width=5)
    old = (data[0], data[1])

def enumHandler(hwnd, lParam):
    global HWND_t
    if win32gui.IsWindowVisible(hwnd):
        if title in win32gui.GetWindowText(hwnd):
            HWND_t = hwnd

win32gui.EnumWindows(enumHandler, None)

tk.bind('<Visibility>', putOnTop)
tk.focus()
def pen():
    global pen_flag
    pen_flag = True
    
    
def close():
    tk.destroy()

def cursor():
    global pen_flag
    pen_flag = False
    tk.iconify()

def motion(event):
    global cur_pos
    global x, y
    cur_pos = (x,y,event.x,event.y)
    x, y = event.x, event.y

def left_click(event):
    global pen_flag
    global cur_pos
    global pressed
    global canvas
    pressed = not pressed
    num =0 
    if pen_flag is True:
        while pressed:
            
            tk.update()
            print("left click", num, cur_pos[0], cur_pos[1], cur_pos[2], cur_pos[3])
            canvas.create_line(cur_pos[0], cur_pos[1],cur_pos[2], cur_pos[3], fill="WHITE", width = 5)
            num = num + 1


popup = Menu(tk, tearoff=0)
popup.add_command(label="Cursor", command=cursor)
popup.add_command(label="Pen", command=pen)
popup.add_separator()
popup.add_command(label="Quit",command=close)

def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root)

    finally:
        popup.grab_release()


tk.bind("<Button-3>", do_popup)
tk.bind("<Button-1>", left_click)
tk.bind("<ButtonRelease-1>", left_click)
tk.bind('<Motion>', motion)


running = 1
while running == 1:
    tk.wm_attributes("-topmost", True)
    try:
        tk.update()
        if HWND_t != 0:
            windowborder = win32gui.GetWindowRect(HWND_t)
            cur_pos = win32api.GetCursorPos()
            state_left_new = win32api.GetKeyState(0x01)
            if state_left_new != state_left:
                drawline((cur_pos[0] - windowborder[0] - 5, cur_pos[1] - windowborder[1] - 30))
            else:
                old = ()
    except Exception as e:
        running = 0
        print("error %r" % (e))