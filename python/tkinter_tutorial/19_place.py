import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Place')
window.geometry('400x600+600+100')

# widgets
label1 = ttk.Label(master=window, text='Label 1', border=5, relief=tk.RAISED)
label2 = ttk.Label(master=window, text='Label 2', border=5, relief=tk.RAISED)
label3 = ttk.Label(master=window, text='Label 3', border=5, relief=tk.RAISED)
button = ttk.Button(master=window, text='Button')

# layout
label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button.place(relx=1.0, rely=1.0, anchor=tk.SE)

# frame
frame = ttk.Frame(master=window, relief=tk.RIDGE)
frame_label = ttk.Label(master=frame, text='Frame Label', border=5, relief=tk.RAISED)
frame_button = ttk.Button(master=frame, text='Frame Button')

# frame layout
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1, anchor=tk.NW)

# exercise: create a label and place it right in the center of the window
# the label should be half as wide as the window and be 200px tall
ex_label = ttk.Label(master=window, text='Exercise Label', border=5, relief=tk.RAISED)
ex_label.place(relx=0.5, rely=0.5, relwidth=0.5, height=200, anchor=tk.CENTER)

# run
window.mainloop()
