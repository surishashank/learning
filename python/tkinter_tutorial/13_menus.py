import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Menus')
window.geometry('600x400')

# menu
menu = tk.Menu(master=window)

# sub menu
file_menu = tk.Menu(master=menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New File'))
file_menu.add_separator()
file_menu.add_command(label='Open', command=lambda: print('Open File'))
menu.add_cascade(label='File', menu=file_menu)

# another sub menu
help_menu = tk.Menu(master=menu, tearoff=False)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=lambda: print('About'))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='Check', variable=help_check_string, onvalue='On', offvalue='Off',
                          command=lambda: print(help_check_string.get()))

# another sub menu with a sub sub menu
ex_menu = tk.Menu(master=menu, tearoff=False)
menu.add_cascade(label='Exercise', menu=ex_menu)
ex_menu.add_command(label='Ex 1', command=lambda: print('Ex 1'))

ex_sub_menu = tk.Menu(master=ex_menu, tearoff=False)
ex_menu.add_cascade(label='Ex 2', menu=ex_sub_menu)
ex_sub_menu.add_command(label='Ex 2.1', command=lambda: print('Ex 2.1'))
ex_sub_menu.add_command(label='Ex 2.2', command=lambda: print('Ex 2.2'))

window.config(menu=menu)

# menu button
menu_button = ttk.Menubutton(master=window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(master=menu_button, tearoff=False)
button_sub_menu.add_command(label='Button 1', command=lambda: print('Button 1'))
button_sub_menu.add_checkbutton(label='Check 1')
menu_button.config(menu=button_sub_menu)

# run
window.mainloop()
