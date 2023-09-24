import tkinter as tk
from tkinter import ttk, font


# window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300+600+300')

# style
style = ttk.Style()
# style.theme_use('default')
# print(style.theme_names())
style.configure('new.TButton', foreground='green', font=('AppleMyungjo', 16))
style.map('new.TButton',
          foreground=[('pressed', 'red'), ('disabled', 'grey')])

# widgets
label = ttk.Label(master=window,
                  text='A label\nAnd then type of another line',
                  background='red',
                  foreground='white',
                  font=('AppleMyungjo', 24),
                  justify=tk.CENTER)
label.pack()

button = ttk.Button(master=window, text='A button', style='new.TButton')
button.pack()

# exercise
style.configure('exercise.TFrame', background='pink')
ex_frame = ttk.Frame(master=window, width=200, height=200, style='exercise.TFrame', relief=tk.GROOVE, borderwidth=10)
ex_frame.pack()

# run
window.mainloop()
