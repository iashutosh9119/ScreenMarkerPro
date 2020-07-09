import tkinter as tk
import time

# --- functions ---

def on_ok():
    x, y = entry.get().split('x')
    for row in range(int(y)):
        for col in range(int(x)):
            print((col, row))

def tick():
    global time1

    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')

    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)

# --- main window ---

time1 = ''

root = tk.Tk()
root.title('Logging')

# add frame in main window (root)

other = tk.Frame(root)
other.pack()

# put widgets in frame (other)

status = tk.Label(other, text="v1.0", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.grid(row=10, column=10)

clock = tk.Label(other, font=('times', 20, 'bold'), bg='green')
clock.grid(row=0, column=1) 

# put other widget directly in main widnow (root)

tk.Label(root, text='Time logging').pack(side=tk.TOP, padx=100, pady=100)

entry = tk.Entry(root, width=25)
entry.pack(side=tk.TOP, padx=25, pady=25)

tk.Button(root, text='Log Time', command=on_ok).pack(side=tk.LEFT)
tk.Button(root, text='CLOSE', command=root.destroy).pack(side= tk.RIGHT)

tick()

# --- start ---

root.mainloop()