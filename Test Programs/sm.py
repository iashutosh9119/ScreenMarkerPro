import tkinter as tk
from tkinter import ttk


LINEWIDTH = 1
TRANSCOLOUR = 'gray'

class Main(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        self.tree = ttk.Treeview(self.master)
        self.tree.pack(fill='x')
        self.rclick = RightClick(self.master)
        self.num = 0

        # attach popup to treeview widget
        self.tree.bind('<Button-3>', self.rclick.popup)


class RightClick:
    def __init__(self, master):

        # create a popup menu
        self.aMenu = tk.Menu(master, tearoff=0)
        self.aMenu.add_command(label='Cursor', command=self.cursor)
        self.aMenu.add_command(label='Pen', command=self.pen)
        self.aMenu.add_command(label='Highlighter', command=self.highlighter)
        self.aMenu.add_command(label='Eraser', command=self.eraser)
        self.aMenu.add_command(label='Eraser All', command=self.erase_all)
        self.aMenu.add_command(label='Close', command=self.close)

        self.tree_item = ''

    def cursor(self):
        if self.tree_item:
            app.tree.delete(self.tree_item)

    def pen(self):
        print ('hello!')

    def highlighter(self, event):
        self.aMenu.post(event.x_root, event.y_root)
        self.tree_item = app.tree.focus()

    def eraser(self):
        if self.tree_item:
            app.tree.delete(self.tree_item)

    def erase_all(self):
        if self.tree_item:
            app.tree.delete(self.tree_item)

    def popup(self, event):
        self.aMenu.post(event.x_root, event.y_root)
        self.tree_item = app.tree.focus()

    def close(self):
        print ('Close')
        root.destroy()
    

root = tk.Tk()
app=Main(root)
root.wm_attributes('-fullscreen',False)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", TRANSCOLOUR)
root.mainloop()