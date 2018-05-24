from tkinter import *
from tkinter import ttk


root = Tk()

tree = ttk.Treeview(root)

tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,    text="Line 1", values=("1A","1b"))

id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))

##alternatively:
tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

def edit():
    x = tree.get_children()
    for item in x: ## Changing all children from root item
        tree.item(item, text="blub", values=("foo", "bar"))

def delete():
    selected_item = tree.selection()[0] ## get selected item
    tree.delete(selected_item)

tree.pack()
button_del = Button(root, text="del", command=delete)
button_del.pack()
button_del = Button(root, text="edit", command=edit)
button_del.pack()

root.mainloop()