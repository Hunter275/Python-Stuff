from Tkinter import *
import ttk
import tkMessageBox

import os
import subprocess

import MySQLdb


#SQL Connection
conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "acdc2007", db = "purdue_rooms")

cursor = conn.cursor()

#Write to SQL
def sqlwrite():
	if str(name)[0:3] == "PY_" or str(room)[0:3] == "PY_"  or str(cell)[0:3] == "PY_"  or str(major)[0:3] == "PY_":
		tkMessageBox.showinfo(message='Please completely fill out form')
	else:
		dname = name.get()
		dhall = var.get()
		droom = room.get()
		dfloor = droom[0:1]
		dcell = cell.get()
		dmajor = major.get()
		dnotes = text_notes.get(1.0, END)
		#Table = "nameof"
		cursor.execute("INSERT INTO rooms (name, hall, room, floor, cell, major, notes) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (dname, dhall, droom, dfloor, dcell, dmajor, dnotes))
		conn.commit()
		conn.close()
		text_name.delete(0, 200)
		var.set("Unknown")
		text_room.delete(0, 200)
		text_cell.delete(0, 200)
		text_major.delete(0, 200)
		text_notes.delete(1.0, END)
		warn = "SUCCESS"


root = Tk()
root.title("Purdue Student Information")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Define variable to be redefined in text
name = StringVar()
room = StringVar()
cell = StringVar()
major = StringVar()


#Dropdown Menu variable and default
var = StringVar()
var.set("Unknown")


#Labels
ttk.Label(mainframe, text="Name").grid(column=1, row=1, sticky=(E))
ttk.Label(mainframe, text="Hall Name").grid(column=1, row=2, sticky=(E))
ttk.Label(mainframe, text="Room #").grid(column=1, row=3, sticky=(E))
ttk.Label(mainframe, text="Cell Phone").grid(column=1, row=4, sticky=(E))
ttk.Label(mainframe, text="Major").grid(column=1, row=5, sticky=(E))
ttk.Label(mainframe, text="Notes").grid(column=1, row=6, sticky=(E))
ttk.Label(mainframe, text="Created by Hunter Thornsberry").grid(column=2, row=7, sticky=S)



#Entry
text_name = ttk.Entry(mainframe, width=30, textvariable=(name))
text_name.grid(column=2, row=1, sticky=(N, W))

hall = ttk.OptionMenu(root, var, "Unknown", "Cary Quad","Earhart","Towers", "Harrison", "Hawkins", "Hillenbrand", "Hillstop Apts", "McCutcheon", "Meredith", "Owen", "Shreve", "Tarkington", "Wiley", "Windsor", "See Notes")
hall.place(relx=0.19, rely=0.15, anchor=NW)

text_room = ttk.Entry(mainframe, width=5, textvariable=(room))
text_room.grid(column=2, row=3, sticky=(N, W))

text_cell = ttk.Entry(mainframe, width=30, textvariable=(cell))
text_cell.grid(column=2, row=4, sticky=(N, W))

text_major = ttk.Entry(mainframe, width=30, textvariable=(major))
text_major.grid(column=2, row=5, sticky=(N, W))

text_notes = Text(mainframe, width=34, height=5)
text_notes.grid(column=2, row=6, sticky=(N, W))



#Button
ttk.Button(mainframe, text="Database", command=sqlwrite).grid(column=3, row=7, sticky=(N, W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()