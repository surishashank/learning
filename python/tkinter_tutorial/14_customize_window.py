import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Customize Window')
window.geometry('600x400+600+300')
# window.iconbitmap('images/icon.ico')

# window sizes
window.minsize(width=200, height=100)
# window.maxsize(width=800, height=700)
# window.resizable(True, False)

# screen attributes
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print(screen_width, screen_height)

# window attributes
# window.attributes('-alpha', 1)
# window.attributes('-topmost', True)
# window.attributes('-fullscreen', True)

# security event
window.bind('<Escape>', lambda event: window.quit())

# title bar
# window.overrideredirect(True)
# grip = ttk.Sizegrip(master=window)
# grip.place(relx=1.0, rely=1.0, anchor='se')

# run
window.mainloop()
