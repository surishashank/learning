import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Grid')
window.geometry('600x400+600+300')

# widgets
label1 = ttk.Label(master=window, text='Label 1', border=5, relief=tk.RAISED)
label2 = ttk.Label(master=window, text='Label 2', border=5, relief=tk.RAISED)
label3 = ttk.Label(master=window, text='Label 3', border=5, relief=tk.RAISED)
label4 = ttk.Label(master=window, text='Label 4', border=5, relief=tk.RAISED)
button1 = ttk.Button(master=window, text='Button 1')
button2 = ttk.Button(master=window, text='Button 2')
entry = ttk.Entry(master=window)

# define a grid
window.columnconfigure((0, 1, 2), weight=1, uniform='a')
window.columnconfigure(3, weight=2, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')

# place a widget
label1.grid(row=0, column=0, sticky='nsew')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, columnspan=3, sticky='ensw', padx=20, pady=10)
label4.grid(row=3, column=3, sticky='se')
button1.grid(row=0, column=3, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')
entry.grid(row=2, column=3, rowspan=2, sticky='ew')

# run
window.mainloop()
