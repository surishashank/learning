import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Colors')
window.geometry('600x400+600+300')

# widgets
ttk.Label(master=window, text='Label', foreground='red').pack(expand=True, fill=tk.BOTH)
ttk.Label(master=window, text='Label', foreground='#08F').pack(expand=True, fill=tk.BOTH)
ttk.Label(master=window, text='Label', foreground='#4fc296').pack(expand=True, fill=tk.BOTH)

# run
window.mainloop()
