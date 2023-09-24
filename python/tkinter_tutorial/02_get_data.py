import tkinter as tk
from tkinter import ttk


# button function
def button_func():
    # get the content of the entry
    entry_content = entry.get()
    print(entry_content)

    # set the content of the label
    label['text'] = entry_content

    # disable the entry
    entry.configure(state=tk.DISABLED)
    print(label.configure())


def reset_func():
    # reset the label
    label['text'] = 'Some text'
    # enable the entry
    entry.configure(state=tk.NORMAL)


# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master=window, text='Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='The button', command=button_func)
button.pack()

reset_button = ttk.Button(master=window, text='Reset', command=reset_func)
reset_button.pack()

# run window
window.mainloop()
