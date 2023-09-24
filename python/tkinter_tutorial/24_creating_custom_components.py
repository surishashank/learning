import tkinter as tk
from tkinter import ttk

def create_segment(master: tk.Tk, label_text: str, button_text: str) -> ttk.Frame:
    frame = ttk.Frame(master=master)

    # grid layout
    frame.rowconfigure(0, weight=1, uniform='a')
    frame.columnconfigure((0, 1, 2), weight=1, uniform='a')

    # create widgets
    label = ttk.Label(master=frame, text=label_text, border=5, relief=tk.RIDGE)
    button = ttk.Button(master=frame, text=button_text)

    # place widgets
    label.grid(row=0, column=0, sticky='nsew')
    button.grid(row=0, column=1, sticky='nsew')

    return frame

class Segment(ttk.Frame):
    def __init__(self, master: tk.Tk, label_text: str, button_0_text: str, button_1_text: str):
        super().__init__(master)

        # grid layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')

        # create widgets
        ttk.Label(self, text=label_text, border=5, relief=tk.RIDGE).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_0_text).grid(row=0, column=1, sticky='nsew')

        # create third column
        self.create_exercise_box(button_1_text).grid(row=0, column=2, sticky='nsew')

        # pack
        self.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

    def create_exercise_box(self, button_text: str) -> ttk.Frame:
        frame = ttk.Frame(master=self)
        ttk.Entry(frame).pack(expand=True, fill=tk.BOTH)
        ttk.Button(frame, text=button_text).pack(expand=True, fill=tk.BOTH)

        return frame



# window
window = tk.Tk()
window.title('Creating Custom Components')
window.geometry('600x600')

# widgets
Segment(window, 'Label', 'Button', 'ex_1')
Segment(window, 'test', 'click', 'ex_2')
Segment(window, 'hello', 'test', 'ex_3')
# create_segment(master=window, label_text='Label', button_text='Button').pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
# create_segment(master=window, label_text='test', button_text='click').pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
# create_segment(master=window, label_text='hello', button_text='test').pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# run
window.mainloop()
