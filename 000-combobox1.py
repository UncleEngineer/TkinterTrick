from tkinter import messagebox, Tk, Menu, ttk

news = ['Mid Day News', 'Evening News']
features = ['Calling Farmers', 'Round About Ja', 'You and the Law', 'Get the Facts',
            'Career Talk', 'Economy and you', 'Arts Page', 'Tourism Roundup',
            'Jeep','Jamaica Promise', 'House Matters', 'Jamaica House Weekly']
features.sort()

class CustomMenu(object):
    def __init__(self, root, values=[], combo_placement=(0, 0), button_placement=(0, 0), label_placement=(0, 0)):
        self.frame = root
        self.combobox = ttk.Combobox(self.frame, values=values)
        self.combobox.bind("<<>ComboboxSelected>")
        self.combobox.grid(row=combo_placement[0], column=combo_placement[1])
        self.label = ttk.Label(self.frame, textvariable=self.combobox.get())
        self.label.grid(row=label_placement[0], column=label_placement[1])
        self.button = ttk.Button(self.frame, text="Add", command=self.update_popup)
        self.button.grid(row=button_placement[0], column=button_placement[1])

    def update_popup(self):
        messagebox.showinfo(
            title="File update",
            message="{} has been added".format(self.combobox.get())
        )


root = Tk()
root.title('Feature Tracking')
root.geometry('255x425')

update_frame = ttk.Frame(root, padding=(5,10))
def show_update_frame():
    update_frame.grid(row=0, column=0)

#Update Menu Frame
features_frame = CustomMenu(update_frame, features, (1, 0), (3, 0), (0, 0))
news_frame = CustomMenu(update_frame, news, (4, 0), (5, 0), (6, 0))

#Menu bar with menu options
menubar = Menu(root)

#Update Menu
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label='New', command=show_update_frame)
menubar.add_cascade(label='Update', menu=filemenu)

root.config(menu = menubar)

root.mainloop()