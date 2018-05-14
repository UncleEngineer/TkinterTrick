from tkinter import *
from tkinter import ttk


def expxl():
	pass


GUI = Tk()
GUI.geometry('700x700')
GUI.title('Unitex Co.,Ltd.')

menubar = Menu(GUI)
#----------------Menu File > Export to Excel > Exit---------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Export to Excel', command=expxl)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=GUI.quit)

menubar.add_cascade(label='File', menu=filemenu)
#----------------Menu File > Export to Excel > Exit---------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Bar', command=expxl)
filemenu.add_command(label='Line', command=expxl)
filemenu.add_separator()
filemenu.add_command(label='Graph', command=GUI.quit)

menubar.add_cascade(label='Summary', menu=filemenu)

GUI.config(menu=menubar)

GUI.mainloop()