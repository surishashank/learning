import tkinter as tk
from tkinter import ttk


# button function
def button_func():
    print('a button was pressed')


# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text='This is a test')
label.pack()

# tk.text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# exercise label
exercise_label = ttk.Label(master=window, text='my label')
exercise_label.pack()

# ttk button
button = ttk.Button(master=window, text='A button', command=button_func)
button.pack()

# exercise button
exercise_button = ttk.Button(master=window, text='exercise button', command=lambda: print('helloo'))
exercise_button.pack()




# run
window.mainloop()