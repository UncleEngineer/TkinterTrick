from tkinter import *
import tkinter.ttk as ttk

root = Tk()

tree = ttk.Treeview(root)
tree.pack()

style = ttk.Style()
style.configure("Treeview.Heading", font=('tohama', 20))

tree["columns"] = ("one", "two", "three")
tree.column("one", width=150)
tree.column("two", width=150)
tree.column("three", width=150)
tree.heading("one", text="Naar")
tree.heading("two", text="Spoor")
tree.heading("three", text="Vetrektijd")
tree['show'] = 'headings'

tree.insert('','1','item1',text=test)

root.mainloop()