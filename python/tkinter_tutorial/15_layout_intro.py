import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout Intro')
window.geometry('600x400')

# widgets
label1 = ttk.Label(master=window, text='Label 1', border=5, relief=tk.RIDGE)
label2 = ttk.Label(master=window, text='Label 2', border=5, relief=tk.RIDGE)

# pack
# label1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# label2.pack(side=tk.LEFT, expand=True, fill=tk.Y)

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
#
# label1.grid(row=0, column=1, sticky='ns')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# place
label1.place(x=100, y=200, width=100, height=50)
label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# run
window.mainloop()
