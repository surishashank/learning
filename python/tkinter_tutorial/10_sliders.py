import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# setup
window = tk.Tk()
window.title('Sliders')
window.geometry('1600x1400')

# slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    master=window,
    command=lambda x: progress.stop(),
    from_=0,
    to=25,
    length=300,
    orient=tk.VERTICAL,
    variable=scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(
    master=window,
    variable=scale_float,
    maximum=25,
    orient=tk.HORIZONTAL,
    mode='indeterminate',
    length=400)
progress.pack()

# ScrolledText
scrolled_text = scrolledtext.ScrolledText(master=window, width=100, height=5)
scrolled_text.pack()

# exercise: create a progress bar that is vertical, starts automatically and also shows the progress as
# a number. There should also be a scale slider that is affected by the progress bar
# slider
exercise_int = tk.IntVar(value=0)
ex_scale = ttk.Scale(
    master=window,
    from_=0,
    to=100,
    length=300,
    orient=tk.HORIZONTAL,
    variable=exercise_int)
ex_scale.pack()

# progress bar
ex_progress = ttk.Progressbar(
    master=window,
    variable=exercise_int,
    maximum=100,
    orient=tk.VERTICAL,
    mode='determinate',
    length=300)
ex_progress.pack()
ex_progress.start()

label = ttk.Label(master=window, textvariable=exercise_int)
label.pack()

# run
window.mainloop()
