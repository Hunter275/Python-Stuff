import datetime
from Tkinter import *
import ttk
import tkMessageBox


x = datetime.datetime.now().time()
y = str(x)

root = Tk()
root.title("Alarm Clock")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Define variable to be redefined in text
hour = int(y[0:2])
minten = int(y[3:4])
minone = int(y[4:5])
minlow = int(y[3:5])
clock = (y[0:5]) 
amp = "Undefined"
alarm_time = StringVar()
alarm_time_hour = StringVar()
alarm_time_min = StringVar()


#Dropdown Menu variable and default
var = StringVar()
var.set("Unknown")


#Labels
ttk.Label(mainframe, text="Current Time: ").grid(column=1, row=1, sticky=(E))
ttk.Label(mainframe, text=clock).grid(column=2, row=1, sticky=(W))
ttk.Label(mainframe, text="Set Alarm For: ").grid(column=1, row=2, sticky=(E))

ttk.Label(mainframe, text=" : ").grid(column=3, row=2, sticky=(E))
#ENTRY
alarm_time = ttk.Entry(mainframe, width=5, textvariable=(alarm_time_hour))
alarm_time.grid(column=2, row=2, sticky=(N, W))

alarm_time = ttk.Entry(mainframe, width=5, textvariable=(alarm_time_min))
alarm_time.grid(column=4, row=2, sticky=(N, W))



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()