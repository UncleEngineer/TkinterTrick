try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk

import random
import string


def insert_something_to_combobox(box):
    box['values'] = [gen_key() for _ in range(10)]


def gen_key(size=6, chars=string.ascii_uppercase + string.digits):
    # just to generate some random stuff
    return ''.join(random.choice(chars) for _ in range(size))


root = tk.Tk()
text_font = ('Courier New', '10')
main_frame = tk.Frame(root, bg='gray')                  # main frame
combo_box = ttk.Combobox(main_frame, font=text_font)    # apply font to combobox
entry_box = ttk.Entry(main_frame, font=text_font)       # apply font to entry
root.option_add('*TCombobox*Listbox.font', text_font)   # apply font to combobox list
combo_box.pack()
entry_box.pack()
main_frame.pack()

insert_something_to_combobox(combo_box)

root.mainloop()