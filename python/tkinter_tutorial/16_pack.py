import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack')
window.geometry('600x400+600+300')

# widgets
label1 = ttk.Label(master=window, text='First Label', border=5, relief=tk.RIDGE)
label2 = ttk.Label(master=window, text='Label 2', border=5, relief=tk.RIDGE)
label3 = ttk.Label(master=window, text='Last of the labels', border=5, relief=tk.RIDGE)
# the button should have a green border
button = ttk.Button(master=window, text='Button')

# layout
label1.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=10, pady=10)
label2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
label3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


# run
window.mainloop()
