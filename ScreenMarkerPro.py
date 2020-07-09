import tkinter as tk
import json
from tkinter import colorchooser
with open('config.json') as config_file:
    config = json.load(config_file)


x = 0
y = 0
CUR_POS = (0,0,0,0)
PEN_FLAG = False

PRESSED = False
LINEWIDTH = config.get('LINEWIDTH')
COLOR = config.get('COLOR')


root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


canvas = tk.Tk()
canvas.geometry("{0}x{1}+0+0".format(canvas.winfo_screenwidth(), canvas.winfo_screenheight()))

WIDTH = canvas.winfo_screenwidth()
HEIGHT = canvas.winfo_screenheight()


TRANSCOLOUR = "gray"

root.wm_attributes("-transparentcolor", TRANSCOLOUR)
root.wm_attributes("-fullscreen",True)
root.wm_attributes("-topmost", True)
root.wm_attributes('-alpha',0.002)


canvas.wm_attributes("-topmost", True)
canvas.wm_attributes("-transparentcolor", TRANSCOLOUR)
canvas.wm_attributes("-fullscreen",True)

w = tk.Canvas(canvas, width=WIDTH, height=HEIGHT,highlightthickness=0)
w.pack()

w.config(cursor='tcross')
i = w.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR,outline=TRANSCOLOUR)

canvas.config(cursor='tcross')
root.config(cursor='tcross')


def pen():
    global PEN_FLAG
    PEN_FLAG = True
    try:
        canvas.deiconify()
    except:
        pass    

def choose_color():
    global COLOR
    # variable to store hexadecimal code of color 
    color_code = colorchooser.askcolor(title ="Choose color")  
    COLOR = color_code[1]

def whiteboard():
    w.itemconfig(i,fill="White")

def blackboard():
    pass

def save():
    pass

def erase():
    pass

def hide():
    pass

def color():
    pass

def size():
    global LINEWIDTH
    LINEWIDTH = 20

def close():
    root.destroy()
    canvas.destroy()

def cursor():
    global PEN_FLAG
    PEN_FLAG = False
    root.iconify()

def motion(event):
    global CUR_POS
    global x, y
    CUR_POS = (x,y,event.x,event.y)
    x, y = event.x, event.y

def left_click(event):
    global PEN_FLAG
    global CUR_POS
    global PRESSED
    global w
    PRESSED = not PRESSED
   
    if PEN_FLAG is True:
        while PRESSED:
            root.update()
            canvas.update()
            w.create_line(CUR_POS[0], CUR_POS[1],CUR_POS[2], CUR_POS[3], fill=COLOR, width = LINEWIDTH,capstyle="round",joinstyle="round")
            


menu = tk.Menu(root, tearoff=False)
submenu = tk.Menu(menu,tearoff=False)

menu.add_command(label="Cursor", command=cursor)
menu.add_command(label="Pen", command=pen)
menu.add_separator()

#menu.add_command(label="Size", command=size)

menu.add_cascade(label="Size", menu=submenu)

submenu.add_command(label="Size 1", command = size)
menu.add_command(label="Color", command=choose_color)
menu.add_separator()

menu.add_command(label="Hide", command=hide)
menu.add_command(label="Erase", command=erase)
menu.add_separator()

menu.add_command(label="WhiteBoard", command=whiteboard)
menu.add_command(label="BlackBoard", command=blackboard)
menu.add_separator()

menu.add_command(label="Quit",command=close)

def do_popup(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)

    finally:
        menu.grab_release()

#canvas--->transcolor
#root -----> alpha
root.bind("<Button-3>", do_popup)
root.bind("<Button-1>", left_click)
root.bind("<ButtonRelease-1>", left_click)
root.bind('<Motion>', motion)

canvas.overrideredirect(1)
canvas.wm_attributes("-topmost", True)

canvas.call('wm', 'attributes', '.', '-topmost', '1')

tk.mainloop()