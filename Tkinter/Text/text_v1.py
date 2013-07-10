from Tkinter import *
import ttk

filename = "test33"
target = open(filename, "w")

def write(*args):
	target.write(str(text_write))
	target.close()



root = Tk()
root.title("Write To File")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)



ttk.Label(mainframe, text="Type your text here ").grid(column=1, row=1, sticky=(N, W))
ttk.Button(mainframe, text="Write", command=write).grid(column=3, row=3, sticky=W)

text_to_write = StringVar()

text_write = ttk.Entry(mainframe, width=50, textvariable=(text_to_write))
text_write.grid(column=2, row=1, sticky=(N, W))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', write)

text_write.focus()
root.mainloop()