from Tkinter import *
import ttk

import os
import subprocess

root = Tk()
root.title("Create A File")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


file_name = StringVar()

file_loc = ttk.Entry(mainframe, width=50, textvariable=(file_name))
file_loc.grid(column=2, row=1, sticky=(N, W))

def create(*args):
	global target
	target = open(str(file_name), "w+")

def write(*args):
	#target.open(file_name, "w")
	target.write(text_write.get())
	#target.write(file_name.get())
	target.close()

def open_file(*args):
	os.system("open " + str(file_name))

#Labels
ttk.Label(mainframe, text="Filename").grid(column=1, row=1, sticky=(E))
ttk.Label(mainframe, text="File Text").grid(column=1, row=2, sticky=(E))
ttk.Label(mainframe, text="Created by Hunter Thornsberry").grid(column=2, row=3, sticky=S)

#Buttons
ttk.Button(mainframe, text="Create", command=create).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Write", command=write).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Open", command=open_file).grid(column=3, row=3, sticky=W)

text_to_write = StringVar()

text_write = ttk.Entry(mainframe, width=50, textvariable=(text_to_write))
text_write.grid(column=2, row=2, sticky=(N, W))



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', write)

text_write.focus()
root.mainloop()