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
	info = str(month.get()) + "/" + str(day.get()) + "/" + str(year.get())
	#Table = "nameof"
	cursor.execute("INSERT INTO nameof (name, info) VALUES ('%s', '%s')" % (dname, info))
	conn.commit()
	conn.close()
	file_loc.delete(0, 200)
	month_loc.delete(0, 200)
	day_loc.delete(0, 200)
	year_loc.delete(0, 200)



root = Tk()
root.title("Create A Text File")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


def write(*args):
	global target
	target = open(str(file_name.get()), "w+")
	target.write(text_box.get(1.0, END))
	target.close()

def open_file(*args):
	os.system("open " + str(file_name.get()))

file_name = StringVar()

#Labels
ttk.Label(mainframe, text="First and Last Name").grid(columnspan=2, row=1, sticky=(E))

ttk.Label(mainframe, text="Birthday").grid(column=1, row=2, sticky=(E))

ttk.Label(mainframe, text="/").grid(column=3, row=2, sticky=(E))

ttk.Label(mainframe, text="/").grid(column=5, row=2, sticky=(E))

ttk.Label(mainframe, text="/").grid(column=7, row=2, sticky=(E))

ttk.Label(mainframe, text="Created by Hunter Thornsberry").grid(column=3, columnspan=4, row=4, sticky=S)



#Buttons
ttk.Button(mainframe, text="Save", command=write).grid(column=7, row=1, sticky=(N, W))

ttk.Button(mainframe, text="Open", command=open_file).grid(column=7, row=2, sticky=(N, W))

ttk.Button(mainframe, text="Database", command=sqlwrite).grid(column=3, row=3, sticky=(N, W))
text_box = StringVar()

month = StringVar()
day = StringVar()
year = StringVar()

#Entry
file_loc = ttk.Entry(mainframe, width=25, textvariable=(file_name))
file_loc.grid(column=2, columnspan=6, row=1, sticky=(N, W))

month_loc = ttk.Entry(mainframe, width=5, textvariable=(month))
month_loc.grid(column=2, columnspan=8, row=2, sticky=(N, W))

day_loc = ttk.Entry(mainframe, width=5, textvariable=(day))
day_loc.grid(column=4, row=2, sticky=(N, W))

year_loc = ttk.Entry(mainframe, width=5, textvariable=(year))
year_loc.grid(column=6, row=2, sticky=(N, W))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()