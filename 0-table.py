from tkinter import *

root = Tk()

height = 5
width = 6

textv = StringVar()
b1 = Entry(root, textvariable=textv).grid(row=7, column=0)

for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, textvariable=textv)
        b.grid(row=i, column=j)

mainloop()