import sys
from tkinter import *

class MinimalMenus (Tk):
    def __init__(self, **kargs):
        """Creates a new application with minimal Mac-standard menus
        Returns the root window, just like Tk()
        To use:
            root = MinimalMenus()
            # configure root and/or create other windows, etc...
            root.mainloop()
        """
        Tk.__init__(self)
        # apply(Tk.__init__, (self,), kargs)

        # create standard menu bar
        menu = Menu(self)
        self.config(menu=menu)

        # add file menu
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(
            label="Close",
            command=self.doClose,
            accelerator="Command-W")
        filemenu.add_command(
            label="Quit",
            command=self.doQuit,
            accelerator="Command-Q")

        # add edit menu
        editmenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(
            label="Cut",
            command=self.doCut,
            accelerator="Command-X")
        editmenu.add_command(
            label="Copy",
            command=self.doCopy,
            accelerator="Command-C")
        editmenu.add_command(
            label="Paste",
            command=self.doPaste,
            accelerator="Command-V")
        editmenu.add_command(
            label="Select All",
            command=self.doSelectAll,
            accelerator="Command-A")

    def doClose(self, evt=None):
        win = self.focus_get().winfo_toplevel()
        win.destroy()

    def doQuit(self, evt=None):
        sys.exit()

    def doCut (self, evt=None):
        widget = self.focus_get()
        if isinstance(widget, Entry):
            if widget.selection_present():
                widget.clipboard_clear()
                widget.clipboard_append(widget.selection_get())
                widget.delete(SEL_FIRST, SEL_LAST)
        else:
            # works for Text, not for Entry (why?); fails quietly
            widget.tk.call('tk_textCut', widget._w)

    def doCopy (self, evt=None):
        widget = self.focus_get()
        if isinstance(widget, Entry):
            if widget.selection_present():
                widget.clipboard_clear()
                widget.clipboard_append(widget.selection_get())
        else:
            # works for Text, not for Entry (why?); fails quietly
            widget.tk.call('tk_textCopy', widget._w)

    def doPaste (self, evt=None):
        widget = self.focus_get()
        # works for Text and Entry, at least; fails quietly
        widget.tk.call('tk_textPaste', widget._w)

    def doSelectAll(self, evt=None):
        widget = self.focus_get()
        if isinstance(widget, Text):
            # the following commented-out code fails on MacPython
            # because the tk commands themselves aren't recognized;
            # hence I am not sure if the code is correct
            print """Cannot yet "Select All" in Text widgets"""
    #       widget.tk_textResetAnchor("1.0")
    #       widget.tk_textSelectTo(END)
        elif isinstance(widget, Entry):
            widget.selection_range(0, END)
            widget.icursor(0)

if __name__ == "__main__":
    root = MinimalMenus()
    aText = Text(root, width=30, height=2)
    aText.insert(END, "some text to manipulate")
    aText.grid(row=0, column=0, sticky=NSEW)
    anEntry = Entry(root)
    anEntry.insert(0, "more text")
    anEntry.grid(row=1, column=0, sticky=EW)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()