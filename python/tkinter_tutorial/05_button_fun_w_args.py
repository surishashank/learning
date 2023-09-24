import tkinter as tk
from tkinter import ttk

def button_func(entry_content):
    print('button pressed')
    print(entry_content.get())

# window
window = tk.Tk()
window.title('Buttons, functions, and arguments')
window.geometry('600x400')

# widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(master=window, textvariable=entry_string)
entry.pack()

button = ttk.Button(master=window, text='Button', command=lambda: button_func(entry_string))
button.pack()

# run
window.mainloop()
