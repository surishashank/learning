import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Extra Window')
        self.geometry('300x200+700+400')
        ttk.Label(master=self, text='A Label').pack()
        ttk.Button(master=self, text='A Button').pack()
        ttk.Label(master=self, text='Another Label').pack(expand=True)

def ask_yes_no():
    answer = messagebox.askyesno(title='Yes or No', message='Are you sure?')
    print(answer)

def create_window():
    global extra_window
    extra_window = Extra()

def close_window():
    extra_window.destroy()


# window
window = tk.Tk()
window.title('Multiple Windows')
window.geometry('600x400+600+300')

button1 = ttk.Button(master=window, text='Open Main Window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(master=window, text='Close Main Window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(master=window, text='Create yes no window', command=ask_yes_no)
button3.pack(expand=True)

# run
window.mainloop()
