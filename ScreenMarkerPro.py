import tkinter as tk
import json
from tkinter import colorchooser

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

PEN_SIZE = config.get('settings', 'pen_size')
HIGHLIGHTER_SIZE = config.get('settings', 'highlighter_size')
HIGHLIGHTER_TRANSPARENCY = config.get('settings', 'highlighter_transparency')
ERASER_SIZE = config.get('settings', 'eraser_size')
POINTER_SIZE = config.get('settings', 'pointer_size')
TEXT_SIZE = config.get('settings', 'text_size')
BOARD_WIDTH = config.get('settings', 'board_width')
BOARD_HEIGHT = config.get('settings', 'board_height')
PEN_COLOR = config.get('settings', 'pen_color')
HIGHLIGHTER_COLOR = config.get('settings', 'highlighter_color')
BOARD_COLOR = config.get('settings', 'board_color')
POINTER_COLOR = config.get('settings', 'pointer_color')
SHAPE_COLOR = config.get('settings', 'shape_color')
TEXT_COLOR = config.get('settings', 'text_color')
TOOLBOX_VISIBLE = config.get('settings', 'toolbox_visible')
TOOLBOX_VERTICLE = config.get('settings', 'toolbox_verticle')
SHAPE_FILL = config.get('settings', 'shape_fill')
FULLSCREEN_BOARD = config.get('settings', 'fullscreen_board')
POINTER_ENABLE = config.get('settings', 'pointer_enable')

x = 0
y = 0
CUR_POS = (0,0,0,0)
PEN_FLAG = False
PRESSED = False
global circle
circle = 0

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

POINTER_ENABLE_CHECK = tk.BooleanVar()
POINTER_ENABLE_CHECK.set(POINTER_ENABLE)




def pen():
    global PEN_FLAG
    PEN_FLAG = True
    try:
        canvas.deiconify()
    except:
        pass    

def choose_color():
    # variable to store hexadecimal code of color 
    global PEN_COLOR
    color_code = colorchooser.askcolor(title ="Choose color")  
    PEN_COLOR = color_code[1]

def whiteboard():
    pass

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

def save_settings():
    global PEN_SIZE, HIGHLIGHTER_SIZE, HIGHLIGHTER_TRANSPARENCY, ERASER_SIZE, POINTER_SIZE, TEXT_SIZE, BOARD_WIDTH, BOARD_HEIGHT, PEN_COLOR, HIGHLIGHTER_COLOR, BOARD_COLOR, POINTER_COLOR, SHAPE_COLOR, TEXT_COLOR, TOOLBOX_VISIBLE, TOOLBOX_VERTICLE, SHAPE_FILL, FULLSCREEN_BOARD
    config.set('settings', 'pen_size', str(PEN_SIZE) )
    config.set('settings', 'highlighter_size', str(HIGHLIGHTER_SIZE))
    config.set('settings', 'highlighter_transparency', str(HIGHLIGHTER_TRANSPARENCY))
    config.set('settings', 'eraser_size', str(ERASER_SIZE))
    config.set('settings', 'pointer_size', str(POINTER_SIZE))
    config.set('settings', 'text_size', str(TEXT_SIZE))
    config.set('settings', 'board_width', str(BOARD_WIDTH))
    config.set('settings', 'board_height', str(BOARD_HEIGHT))


    config.set('settings', 'pen_color', str(PEN_COLOR))
    config.set('settings', 'highlighter_color', str(HIGHLIGHTER_COLOR))
    config.set('settings', 'board_color', str(BOARD_COLOR))
    config.set('settings', 'pointer_color', str(POINTER_COLOR))
    config.set('settings', 'shape_color', str(SHAPE_COLOR))
    config.set('settings', 'text_color', str(TEXT_COLOR))


    config.set('settings', 'toolbox_visible', str(TOOLBOX_VISIBLE))
    config.set('settings', 'toolbox_verticle', str(TOOLBOX_VERTICLE))
    config.set('settings', 'shape_fill', str(SHAPE_FILL))
    config.set('settings', 'fullscreen_board', str(FULLSCREEN_BOARD))
    config.set('settings', 'pointer_enable', str(POINTER_ENABLE))


def size(x):
    global PEN_SIZE
    if x:
        PEN_SIZE = x
    else:
        pass        

def close():
    save_settings()
    with open('config.ini', 'w') as userconfigfile:
        config.write(userconfigfile)
    root.destroy()
    canvas.destroy()

def cursor():
    global PEN_FLAG
    PEN_FLAG = False
    root.iconify()

def motion(event):
    global CUR_POS,x,y,POINTER_SIZE,w,circle
    CUR_POS = (x,y,event.x,event.y)
    x, y = event.x, event.y
    if bool(POINTER_ENABLE) is True:
        if circle:
            w.delete(circle)
        radius = int(POINTER_SIZE)
        x_max = x + radius
        x_min = x - radius
        y_max = y + radius
        y_min = y - radius
        
        circle = w.create_oval(x_max, y_max, x_min, y_min, outline=str(POINTER_COLOR))
    else:
        if circle:
            w.delete(circle)


def left_click(event):
    global PRESSED
    global PEN_FLAG
    PRESSED = not PRESSED
   
    if PEN_FLAG is True:
        while PRESSED:
            root.update()
            canvas.update()
            w.create_line(CUR_POS[0], CUR_POS[1],CUR_POS[2], CUR_POS[3], fill=PEN_COLOR, width = PEN_SIZE,capstyle="round",joinstyle="round")
            
def highlight():
    pass


def pointer():
    global POINTER_ENABLE
    POINTER_ENABLE = POINTER_ENABLE_CHECK.get()
    print(POINTER_ENABLE)

menu = tk.Menu(root, tearoff=False)
submenu = tk.Menu(menu,tearoff=False)

menu.add_command(label="Cursor", command=cursor)
menu.add_command(label="Pen", command=pen)
menu.add_command(label="Highlighter", command=highlight)
menu.add_checkbutton(label="Pointer",onvalue=True,offvalue=False,variable=POINTER_ENABLE_CHECK,command=pointer,selectcolor=POINTER_COLOR,foreground=POINTER_COLOR)
menu.add_separator()


menu.add_cascade(label="Size", menu=submenu)
submenu.add_command(label="Small", command = lambda: size(2))
submenu.add_command(label="Normal", command = lambda: size(5))
submenu.add_command(label="Medium", command = lambda: size(10))
submenu.add_command(label="Large", command = lambda: size(15))
submenu.add_command(label="Custom", command = lambda: size(0))
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