from Tkinter import *
import ttk

import os
import subprocess

import MySQLdb

#SQL Connection
conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "acdc2007", db = "names")

cursor = conn.cursor()

#Write to SQL
def sqlwrite():
	dname = file_name.get()
	info = text_box.get(1.0, END)
	#Table = "nameof"
	cursor.execute("INSERT INTO nameof (name, info) VALUES ('%s', '%s')" % (dname, info))
	conn.commit()
	conn.close()



root = Tk()
root.title("Create A Text File")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

file_name = StringVar()

file_loc = ttk.Entry(mainframe, width=50, textvariable=(file_name))
file_loc.grid(column=2, row=1, sticky=(N, W))

def write(*args):
	global target
	target = open(str(file_name.get()), "w+")
	target.write(text_box.get(1.0, END))
	target.close()

def open_file(*args):
	os.system("open " + str(file_name.get()))


#Labels
ttk.Label(mainframe, text="Filename").grid(column=1, row=1, sticky=(E))
ttk.Label(mainframe, text="File Text").grid(column=1, row=2, sticky=(E))
ttk.Label(mainframe, text="Created by Hunter Thornsberry").grid(column=2, row=3, sticky=S)

#Buttons
ttk.Button(mainframe, text="Save", command=write).grid(column=3, row=1, sticky=(N, W))
ttk.Button(mainframe, text="Open", command=open_file).grid(column=3, row=2, sticky=(N, W))
ttk.Button(mainframe, text="Database", command=sqlwrite).grid(column=3, row=3, sticky=(N, W))
text_box = StringVar()

#Entry
text_box = Text(mainframe, width=57, height=5)
text_box.grid(column=2, row=2, sticky=(N, W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()