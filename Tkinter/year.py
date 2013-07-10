from Tkinter import *
import ttk

def calculate(*args):
	try:
		value = float(year.get())
		x.set(value * 1)
	except ValueError:
		pass

root = Tk()
root.title("USD to Pounds")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

year = StringVar()
x = StringVar()

ttk.Label(mainframe, text="What year is it? ").grid(column=1, row=1, sticky=(N, W))
ttk.Label(mainframe, textvariable=x).grid(column=2, row=2, sticky=(S))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


year_entry = ttk.Entry(mainframe, width=5, textvariable=year)
year_entry.grid(column=2, row=1, sticky=(N, W))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.bind('<Return>', calculate)

year_entry.focus()
root.mainloop()