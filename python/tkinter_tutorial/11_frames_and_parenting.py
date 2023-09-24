import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Frames and Parenting')
window.geometry('600x400')

# frames
frame = ttk.Frame(master=window, width=200, height=200, relief=tk.GROOVE, borderwidth=10)
frame.pack_propagate(False)
frame.pack(side=tk.LEFT)

# master setting
label = ttk.Label(master=frame, text='Label in frame')
label.pack()

button = ttk.Button(master=frame, text='Button in frame')
button.pack()

label_outside = ttk.Label(master=window, text='Label outside frame')
label_outside.pack(side=tk.LEFT)

# exercise
ex_frame = ttk.Frame(master=window, width=200, height=200, relief=tk.GROOVE, borderwidth=10)
ex_frame.pack_propagate(False)
ex_frame.pack(side=tk.RIGHT)

ex_label = ttk.Label(master=ex_frame, text='Label in ex_frame')
ex_label.pack()

ex_button = ttk.Button(master=ex_frame, text='Button in ex_frame')
ex_button.pack()

ex_entry = ttk.Entry(master=ex_frame)
ex_entry.pack()

# run
window.mainloop()
