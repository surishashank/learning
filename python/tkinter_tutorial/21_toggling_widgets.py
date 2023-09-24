import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Hide Widgets')
window.geometry('600x400+600+300')

# place
# def toggle_label_place():
#     global label_visibile
#     if label_visibile:
#         label.place_forget()
#         label_visibile = False
#     else:
#         label.place(relx=0.5, rely=.5, anchor=tk.CENTER)
#         label_visibile = True
#
# button = ttk.Button(master=window, text='Toggle Label', command=toggle_label_place)
# button.place(x=10, y=10)
#
# label_visibile = True
# label = ttk.Label(master=window, text='A label')
# label.place(relx=0.5, rely=.5, anchor=tk.CENTER)

# grid
# def toggle_label_grid():
#     global label_visibile
#     if label_visibile:
#         label.grid_forget()
#         label_visibile = False
#     else:
#         label.grid(row=0, column=1, sticky='nsew')
#         label_visibile = True
#
# window.columnconfigure(0, weight=1, uniform='a')
# window.columnconfigure(1, weight=1, uniform='a')
# window.rowconfigure(0, weight=1, uniform='a')
#
# button = ttk.Button(master=window, text='Toggle Label', command=toggle_label_grid)
# button.grid(row=0, column=0)
#
# label_visibile = True
# label = ttk.Label(master=window, text='A label', border=5, relief=tk.RAISED)
# label.grid(row=0, column=1, sticky='nsew')

# pack
def toggle_label_pack():
    global label_visibile
    if label_visibile:
        label.pack_forget()
        label_visibile = False
        frame.pack(expand=True, before=button)
    else:
        frame.pack_forget()
        label.pack(expand=True, before=button)
        label_visibile = True

label_visibile = True
label = ttk.Label(master=window, text='A label', border=5, relief=tk.RAISED)
label.pack(expand=True)

button = ttk.Button(master=window, text='Toggle Label', command=toggle_label_pack)
button.pack()

frame = ttk.Frame(master=window)

# run
window.mainloop()
