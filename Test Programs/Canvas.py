from tkinter import Tk,Canvas,mainloop

tk = Tk()
TRANSCOLOUR = 'Gray'
WIDTH = tk.winfo_screenwidth()
HEIGHT = tk.winfo_screenheight()
tk.wm_attributes("-transparentcolor", TRANSCOLOUR)

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.config(cursor='tcross')
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)



tk.call('wm', 'attributes', '.', '-topmost', '1')
mainloop()

#window(tK)->Canvas(canvas)->Rectangle