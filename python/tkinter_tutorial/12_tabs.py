import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tabs')
window.geometry('600x400')

# notebook
notebook = ttk.Notebook(master=window)


# tab 1
tab1 = ttk.Frame(master=notebook)
tab1.pack()

label1 = ttk.Label(master=tab1, text='Text in tab 1')
label1.pack()
button1 = ttk.Button(master=tab1, text='Button in tab 1')
button1.pack()

# tab 2
tab2 = ttk.Frame(master=notebook)
tab2.pack()

label2 = ttk.Label(master=tab2, text='Text in tab 2')
label2.pack()
entry2 = ttk.Entry(master=tab2)
entry2.pack()

# tab 3
tab3 = ttk.Frame(master=notebook)
button3_0 = ttk.Button(master=tab3, text='Button 1 in tab 3')
button3_0.pack()
button3_1 = ttk.Button(master=tab3, text='Button 2 in tab 3')
button3_1.pack()
label3 = ttk.Label(master=tab3, text='Text in tab 3')
label3.pack()

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')
notebook.pack()
# run
window.mainloop()