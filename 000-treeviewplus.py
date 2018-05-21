from tkinter import *
from tkinter import ttk
root = Tk()


treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('','0','item1',text='First Item')
treeview.insert('','1','item2',text='Second Item')
#-------------
logo = PhotoImage(file='truck.png').subsample(20,20)
treeview.insert('item2','end','truck001',text='Truck No.001', image = logo)




root.mainloop()
