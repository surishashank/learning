import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Combobox and Spinbox')
window.geometry('600x400')

# combobox
items = ['Ice cream', 'Pizza', 'Broccoli']
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(master=window, values=items, textvariable=food_string)
combo.pack()

combo_label = ttk.Label(master=window)
combo_label.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text=f'Selected value: {food_string.get()}'))

# spinbox
spin_number = tk.DoubleVar(value=3)
spin = ttk.Spinbox(master=window,
                   from_=3,
                   to=20,
                   increment=0.5,
                   textvariable=spin_number,
                   command=lambda: print(spin_number.get()),
                   wrap=True)
spin.bind('<<Increment>>', lambda event: print('Incremented'))
spin.bind('<<Decrement>>', lambda event: print('Decremented'))
spin.pack()

# exercise
# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased
spin_items = ['A', 'B', 'C', 'D', 'E']
spin_string = tk.StringVar()
ex_spin = ttk.Spinbox(master=window, values=spin_items, textvariable=spin_string)
ex_spin.pack()
ex_spin.bind('<<Decrement>>', lambda event: print(spin_string.get()))

# run
window.mainloop()
