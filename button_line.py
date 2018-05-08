import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def click():
    label.configure(text="Widget with focus: %s" % root.focus_get())

e1 = ttk.Entry(root, name="e1")
e2 = ttk.Entry(root, name="e2")
label = ttk.Label(root)

b1 = ttk.Button(root, text="Steal focus", command=click, name="b1", takefocus=True)
b2 = ttk.Button(root, text="Don't Steal focus", command=click, name="b2", takefocus=False)

e1.pack(fill="x")
e2.pack(fill="x")
label.pack(side="top", fill="both", expand=True)
b1.pack(side="left")
b2.pack(side="left")

root.mainloop()
