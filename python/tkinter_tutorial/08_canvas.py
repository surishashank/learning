import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Canvas')
window.geometry('600x400')

# canvas
# canvas = tk.Canvas(master=window, width=400, height=400, bg='black')
# canvas.pack()
#
# canvas.create_rectangle(50, 20, 300, 300, fill='red', width=0)
# canvas.create_line(50, 20, 300, 300, fill='white', width=2)
# canvas.create_text(100, 200, text='Hello World', fill='yellow', font=('Arial', 30))
#
# canvas.create_window((150, 100), window=ttk.Label(master=window, text='this is a text in a window'))

# exercise: use event binding to create a basic paint app
def draw_on_canvas(x, y):
    width = brush_size/2
    canvas.create_oval(x-width, y-width, x+width, y+width, fill='white', width=0)

brush_size = 2
canvas = tk.Canvas(master=window, width=400, height=400, bg='black')
canvas.pack()

# bind to mouse event
# when the mouse is clicked, and the event stays in effect till the mouse is released
canvas.bind('<B1-Motion>', lambda event: draw_on_canvas(event.x, event.y))
# canvas.bind('<Button>', lambda event: draw_on_canvas(event.x, event.y))


# run
window.mainloop()
