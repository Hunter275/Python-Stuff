from Tkinter import *
import ttk
import time
 
root = Tk()
root.title("Alarm Clock")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)





time1 = ''
clock = Label(root)
clock.pack(fill=BOTH, expand=1)
 
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

ttk.Label(mainframe, text="Filename ").grid(column=1, row=1, sticky=(N, W))

 
tick()
root.mainloop(  )