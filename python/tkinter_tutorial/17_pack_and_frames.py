import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack and Frames')
window.geometry('600x400+600+300')

# top frame
top_frame = ttk.Frame(master=window, relief=tk.GROOVE, borderwidth=10)
label1 = ttk.Label(master=top_frame, text='First label', border=5, relief=tk.RIDGE)
label2 = ttk.Label(master=top_frame, text='Label 2', border=5, relief=tk.RIDGE)

# middle label
label3 = ttk.Label(master=window, text='Another label', border=5, relief=tk.RIDGE)

# bottom frame
bottom_frame = ttk.Frame(master=window, relief=tk.GROOVE, borderwidth=10)
button1 = ttk.Button(master=bottom_frame, text='A Button')
label4 = ttk.Label(master=bottom_frame, text='Last of the labels', border=5, relief=tk.RIDGE)
button2 = ttk.Button(master=bottom_frame, text='Another Button')
sub_frame = ttk.Frame(master=bottom_frame, relief=tk.GROOVE, borderwidth=5)
button3 = ttk.Button(master=sub_frame, text='Button 3')
button4 = ttk.Button(master=sub_frame, text='Button 4')
button5 = ttk.Button(master=sub_frame, text='Button 5')

# top layout
label1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
label2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# middle layout
label3.pack(side=tk.TOP, expand=True, fill=tk.NONE)

# bottom layout
bottom_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=20, pady=20)
button1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
label4.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
button2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
sub_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
button3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
button4.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
button5.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# run
window.mainloop()
