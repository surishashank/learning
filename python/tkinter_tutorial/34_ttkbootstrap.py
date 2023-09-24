import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='journal')
window.title('ttkbootstrap intro')
window.geometry('600x400+600+300')

label = ttk.Label(master=window, text='Label')
label.pack(pady=10)

button1 = ttk.Button(master=window, text='Red', bootstyle='danger-outline')
button1.pack(pady=10)

button2 = ttk.Button(master=window, text='Button 2', bootstyle='warning')
button2.pack(pady=10)

button3 = ttk.Button(master=window, text='Button 3')
button3.pack(pady=10)

# run
window.mainloop()
