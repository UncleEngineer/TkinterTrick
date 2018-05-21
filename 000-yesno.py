from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()

def test():

	ok = messagebox.askokcancel("Title","The application will be closed")
	if ok == True:
		print(ok)
	else:
		print(ok)
def test2():

	ok = messagebox.askyesno("Title","Do you want to save?")
	if ok == True:
		print(ok)
	else:
		print(ok)

def test3():

	ok = messagebox.askretrycancel("Title","Installation failed, try again?")
	if ok == True:
		print(ok)
	else:
		print(ok)
#yes = messagebox.askyesno("Title","Do you want to save?")
#retry = messagebox.askretrycancel("Title","Installation failed, try again?")

B1 = ttk.Button(GUI,text='Close Program', command=test)
B2 = ttk.Button(GUI,text='Yes', command=test2)
B3 = ttk.Button(GUI,text='Close Program', command=test3)

B1.pack()
B2.pack()
B3.pack()

GUI.mainloop()