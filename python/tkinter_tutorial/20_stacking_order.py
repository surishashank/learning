import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Stacking Order')
window.geometry('400x400+600+300')

# widgets
label1 = ttk.Label(master=window, text='Label 1', border=5, relief=tk.RAISED)
label2 = ttk.Label(master=window, text='Label 2', border=5, relief=tk.RAISED)

# label1.lift()
# label2.lower()

button1 = ttk.Button(master=window, text='Raise Label 1', command=lambda: label1.lift(aboveThis=label2))
button2 = ttk.Button(master=window, text='Raise Label 2', command=lambda: label2.lift())

# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)

button1.place(relx=0.7, rely=1, anchor=tk.SE)
button2.place(relx=1, rely=1, anchor=tk.SE)

# exercise: add a third label and button to raise the label
label3 = ttk.Label(master=window, text='Label 3', border=5, relief=tk.RAISED)
label3.place(x=20, y=80, width=180, height=100)
button3 = ttk.Button(master=window, text='Raise Label 3', command=lambda: label3.lift())
button3.place(relx=0.4, rely=1, anchor=tk.SE)

# run
window.mainloop()
