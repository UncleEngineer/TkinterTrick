from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook

def expxl():
	pass


GUI = Tk()
GUI.geometry('650x600')
GUI.resizable(width=False, height=False)
GUI.title('Unitex Co.,Ltd.')

### --------------- Menubar------------------###
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

# Frame
tab = Notebook(GUI,height=700)

F1 = Frame(tab, width=200, height=500)
F2 = Frame(tab, width=200, height=500)
F3 = Frame(tab, width=200, height=500)

tab.add(F1, text='Reception Tank')
tab.add(F2, text='Latex')
tab.add(F3, text='Summary')




# Tab 1 Reception Tank - Wet Weight
rc_opening = StringVar()
rc_process_intake = StringVar()
rc_process_production = StringVar()
rc_closing = StringVar()

# Select Tank
SLT = ttk.Label(F1, text='Select Tank')
SLT.grid(row=0, column=0, padx=10, pady=10, sticky='e')

tankvalue = ('Tank 1','Tank 2','Tank 3','Tank 4','Tank 5','Tank 6','Tank 7','Tank 8','Tank 9','Tank 10','Tank 11')

tankselect = ttk.Combobox(F1, values = tankvalue)
tankselect.set('Tank 1')
tankselect.grid(row=0,column=1, padx=10, pady=10, sticky='w')

receptionframe = LabelFrame(F1, text="Wet Weight")
receptionframe.grid(row=1, column=0, padx=10, pady=10, sticky='w')

T1L1 = ttk.Label(receptionframe, text='Opening Storage')
T1L1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

T1E1 = ttk.Entry(receptionframe, textvariable= rc_opening)
T1E1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

T1L2 = ttk.Label(receptionframe, text='Processed (Intake)')
T1L2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

T1E2 = ttk.Entry(receptionframe, textvariable= rc_process_intake)
T1E2.grid(row=1, column=1, padx=10, pady=10, sticky='w')

T1L3 = ttk.Label(receptionframe, text='Processed (Production)')
T1L3.grid(row=2, column=0, padx=10, pady=10, sticky='w')

T1E3 = ttk.Entry(receptionframe, textvariable= rc_process_production)
T1E3.grid(row=2, column=1, padx=10, pady=10, sticky='w')

T1L4 = ttk.Label(receptionframe, text='Closing Stock')
T1L4.grid(row=3, column=0, padx=10, pady=10, sticky='w')

T1E4 = ttk.Entry(receptionframe, textvariable= rc_closing, state='disabled')
T1E4.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Tab 1 Reception Tank - Dry Weight
d_rc_opening = StringVar()
d_rc_process_intake = StringVar()
d_rc_process_production = StringVar()
d_rc_closing = StringVar()

receptionframe2 = LabelFrame(F1, text="Dry Weight")
receptionframe2.grid(row=1, column=1, padx=10, pady=10, sticky='w')

d_T1L1 = ttk.Label(receptionframe2, text='Opening Storage')
d_T1L1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

d_T1E1 = ttk.Entry(receptionframe2, textvariable= d_rc_opening)
d_T1E1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

d_T1L2 = ttk.Label(receptionframe2, text='Processed (Intake)')
d_T1L2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

d_T1E2 = ttk.Entry(receptionframe2, textvariable= d_rc_process_intake)
d_T1E2.grid(row=1, column=1, padx=10, pady=10, sticky='w')

d_T1L3 = ttk.Label(receptionframe2, text='Processed (Production)')
d_T1L3.grid(row=2, column=0, padx=10, pady=10, sticky='w')

d_T1E3 = ttk.Entry(receptionframe2, textvariable= d_rc_process_production)
d_T1E3.grid(row=2, column=1, padx=10, pady=10, sticky='w')

d_T1L4 = ttk.Label(receptionframe2, text='Closing Stock')
d_T1L4.grid(row=3, column=0, padx=10, pady=10, sticky='w')

d_T1E4 = ttk.Entry(receptionframe2, textvariable= d_rc_closing, state='disabled')
d_T1E4.grid(row=3, column=1, padx=10, pady=10, sticky='w')

d_T1B1 = ttk.Button(F1, text='Add')
d_T1B1.grid(row=3, column=1, padx=10, pady=10, sticky='e')


# state='disabled'
# Tab 2 Latex Concentrate Production
latexconcentrate = LabelFrame(F3, text="Latex Concentrate Production")
latexconcentrate.grid(row=2, column=0, padx=10, pady=10, sticky='w')


tab2 = Notebook(latexconcentrate,height=500)

F3 = Frame(tab2, width=200, height=500)
F4 = Frame(tab2, width=200, height=500)
F5 = Frame(tab2, width=200, height=500)
F6 = Frame(tab2, width=200, height=500)
F7 = Frame(tab2, width=200, height=500)

tab2.add(F3, text='Skim Production')
tab2.add(F4, text='Raw Material')
tab2.add(F5, text='Production Utilitization')
tab2.add(F6, text='Shipment')
tab2.add(F7, text='Production Performance')
tab2.pack(fill=BOTH, padx=10, pady=10)


#L2 = ttk.Label(latexconcentrate, text='Opening Storage')
#L2.pack()
#L2.grid(row=0, column=0, padx=10, pady=10, sticky='w')

#E2 = ttk.Entry(latexconcentrate, textvariable= rc_opening)
#E2.grid(row=0, column=1, padx=10, pady=10, sticky='w')









tab.pack(fill=BOTH)

GUI.mainloop()