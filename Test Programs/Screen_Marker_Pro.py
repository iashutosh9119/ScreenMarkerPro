from tkinter import *

root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

TRANSCOLOUR = "gray"

root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", TRANSCOLOUR)
root.wm_attributes("-fullscreen")
images = []
LINEWIDTH = 1
x = 0
y = 0
cur_pos = (0,0,0,0)
pen_flag = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

pressed = False

w = Canvas(root, width=width, height=height)
w.pack()

w.config(cursor='tcross')

def pen():
    global pen_flag
    global w
    pen_flag = True
    
    
def close():
    root.destroy()

def cursor():
    global pen_flag
    pen_flag = False
    root.iconify()

def motion(event):
    global cur_pos
    global x, y
    cur_pos = (x,y,event.x,event.y)
    x, y = event.x, event.y

def left_click(event):
    global pen_flag
    global cur_pos
    global pressed
    global w
    pressed = not pressed
    num =0 
    if pen_flag is True:
        while pressed:
            
            root.update()
            print("left click", num, cur_pos[0], cur_pos[1], cur_pos[2], cur_pos[3])
            w.create_line(cur_pos[0], cur_pos[1],cur_pos[2], cur_pos[3], fill="WHITE", width = 5)
            num = num + 1


popup = Menu(root, tearoff=0)
popup.add_command(label="Cursor", command=cursor)
popup.add_command(label="Pen", command=pen)
popup.add_separator()
popup.add_command(label="Quit",command=close)

def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root)

    finally:
        popup.grab_release()


root.bind("<Button-3>", do_popup)
root.bind("<Button-1>", left_click)
root.bind("<ButtonRelease-1>", left_click)
root.bind('<Motion>', motion)


root.wm_attributes('-fullscreen',True)
root.wm_attributes("-topmost", True)
root.wm_attributes('-alpha',0.002)
mainloop()