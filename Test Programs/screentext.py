from tkinter import *

root = Tk()
c = Canvas(root, width=640, height=480, bd=0, highlightthickness=0)
c.create_line(0,240,640,240, fill='blue')
c.pack()

#pil image with transparency
try:
    from PIL import Image, ImageTk
except ImportError:
    pass
else:
    pim = Image.new('RGBA', (5,100), (0,255,0,64))
    photo = ImageTk.PhotoImage(pim)
    c.create_image(200,200, image=photo, anchor='nw')

#blank standard photoimage with red vertical borders
im = PhotoImage(width=7, height=480)
dat = ('red',)*480
im.put(dat, to=(0,0))
im.put(dat, to=(6,0))

box = c.create_image(0, 0, image=im, anchor='nw')

def on_motion(event):
    left,top = c.coords(box)
    dx = event.x - (left+7)
    c.move(box, dx, 0)

c.bind('<Motion>', on_motion)
root.mainloop()