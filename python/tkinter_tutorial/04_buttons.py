import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(master=window, text='A simple button', command=button_func, textvariable=button_string)
button.pack()

# checkbutton
check_var = tk.IntVar()
check1 = ttk.Checkbutton(
    master=window,
    text='checkbox 1',
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(
    master=window,
    text='checkbox 2',
    command=lambda: check_var.set(5))
check2.pack()

# radiobutton
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    master=window,
    text='radio 1',
    value=1,
    variable=radio_var,
    command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(
    master=window,
    text='radio 2',
    value=2,
    variable=radio_var,
    command=lambda: print(radio_var.get()))
radio2.pack()

# create another checkbutton and 2 radiobuttons
# radio button:
#   values for the buttons are A and B
#   ticking either prints the value of the checkbutton
#    ticking the radio button unchecks the checkbutton
# checkbutton:
#   ticking the checkbutton prints the value of the radio button
#   use tkinter var for Booleans!
def print_and_uncheck_checkbutton():
    print(ex_check_var.get())
    ex_check_var.set(False)

ex_radio_var = tk.StringVar()
ex_radio_button_1 = ttk.Radiobutton(
    master=window,
    text='ex_radio_button_1',
    value='A',
    variable=ex_radio_var,
    command=print_and_uncheck_checkbutton)
ex_radio_button_1.pack()
ex_radio_button_2 = ttk.Radiobutton(
    master=window,
    text='ex_radio_button_2',
    value='B',
    variable=ex_radio_var,
    command=print_and_uncheck_checkbutton)
ex_radio_button_2.pack()

ex_check_var = tk.BooleanVar()
ex_check_button = ttk.Checkbutton(
    master=window,
    text='ex_check_button',
    variable=ex_check_var,
    command=lambda: print(ex_radio_var.get()))
ex_check_button.pack()

# run
window.mainloop()
