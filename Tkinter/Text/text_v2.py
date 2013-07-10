from Tkinter import *
import ttk

import os
import subprocess

root = Tk()
root.title("Write To File")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


file_name = "HAB"

filename = ttk.Entry(mainframe, width=50, textvariable=(file_name))
filename.grid(column=2, row=1, sticky=(N, W))

target = open(file_name, "w")

def write(*args):
	#target.open(filename, "w")
	target.write(text_write.get())
	target.close()

def open_file(*args):
	os.system("open " + str(file_name))


ttk.Label(mainframe, text="Filename").grid(column=1, row=1, sticky=(E))
ttk.Label(mainframe, text="Type your text here").grid(column=1, row=2, sticky=(E))
ttk.Button(mainframe, text="Write", command=write).grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Hunter Thornsberry").grid(column=2, row=5, sticky=S)
ttk.Button(mainframe, text="Open", command=open_file).grid(column=3, row=5, sticky=W)

text_to_write = StringVar()

text_write = ttk.Entry(mainframe, width=50, textvariable=(text_to_write))
text_write.grid(column=2, row=2, sticky=(N, W))



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', write)

text_write.focus()
root.mainloop()