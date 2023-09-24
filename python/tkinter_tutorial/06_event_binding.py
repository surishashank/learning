import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x}, y: {event.y}')

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# widgets
text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='A button')
button.pack()

# events
button.bind('<KeyPress-a>', lambda event: print(event))
window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))
# window.bind('<Motion>', get_pos)
entry.bind('<FocusIn>', lambda event: print(f'entry field was selected'))
entry.bind('<FocusOut>', lambda event: print(f'entry field was unselected'))

text.bind('<Shift-MouseWheel>', lambda event: print(f'Mousewheel'))

# runa
window.mainloop()
