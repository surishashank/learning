import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
    global resized_tk
    # size
    width = event.width
    height = event.height

    # resize
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on the canvas
    canvas.create_image(0, 0, anchor='nw', image=resized_tk)

def fill_image(event):
    global resized_tk
    # current ratio
    canvas_ratio = canvas.winfo_width() / canvas.winfo_height()

    # get coordinates of image
    if canvas_ratio > image_ratio: # canvas is wider than image
        width = int(event.width)
        height = int(width / image_ratio)
    else:                          # canvas is taller than image
        height = int(event.height)
        width = int(height * image_ratio)

    # resize
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place image in the middle of the canvas
    canvas.create_image(event.width/2, event.height/2, anchor=tk.CENTER, image=resized_tk)

def show_full_image(event):
    global resized_tk
    # current ratio
    canvas_ratio = canvas.winfo_width() / canvas.winfo_height()

    # get coordinates of image
    if canvas_ratio > image_ratio:  # canvas is wider than image
        height = int(event.height)
        width = int(height * image_ratio)
    else:  # canvas is taller than image
        width = int(event.width)
        height = int(width / image_ratio)

    # resize
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place image in the middle of the canvas
    canvas.create_image(event.width / 2, event.height / 2, anchor=tk.CENTER, image=resized_tk)

# window
window = tk.Tk()
window.title('Images')
window.geometry('600x400+600+300')

# grid layout
window.columnconfigure((0,1,2,3), weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')

# import an image
image_original = Image.open('images/raccoon.webp')
image_ratio = image_original.width / image_original.height
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('images/python_dark.png').resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

python_img_ctk = ctk.CTkImage(light_image=Image.open('images/python_dark.png').resize((30, 30)),
                              dark_image=Image.open('images/python_light.png').resize((30, 30)))

# widget
# label = ttk.Label(master=window, text='Raccoon', image=image_tk)
# label.pack()
button_frame = ttk.Frame(master=window)
button = ttk.Button(master=button_frame, text='A Button', image=python_dark_tk,
                    compound=tk.RIGHT)
button.pack(pady=10)

button_ctk = ctk.CTkButton(master=button_frame, text='A Button', image=python_img_ctk,
                           compound=tk.RIGHT)
button_ctk.pack(pady=10)

button_frame.grid(row=0, column=0, sticky='nsew')

# canvas -> image
canvas = tk.Canvas(master=window, background='black', bd=0, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=3, sticky='nsew')
# canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)
canvas.bind('<Configure>', func=show_full_image)

# run
window.mainloop()
