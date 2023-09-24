import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent: tk.Tk, text_data: list[tuple[str, str]], item_height: int):
        super().__init__(parent)
        self.pack(expand=True, fill=tk.BOTH)

        # widget data
        self.text_data: list[tuple[str, str]] = text_data
        self.item_number = len(text_data)
        self.list_height = item_height * self.item_number

        # canvas
        self.canvas = tk.Canvas(master=self, bg='red', scrollregion=(0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # display frame
        self.frame = ttk.Frame(master=self)
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill=tk.BOTH)

        # scrollbar
        self.vertical_scrollbar = ttk.Scrollbar(master=self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.vertical_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.canvas.configure(yscrollcommand=self.vertical_scrollbar.set)

        # events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta), 'units'))
        self.bind('<Configure>', self.update_size)

    def update_size(self, event: tk.Event) -> None:
        if self.list_height > self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>', lambda x: self.canvas.yview_scroll(-int(x.delta), 'units'))
            self.vertical_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
            self.vertical_scrollbar.place_forget()
        self.canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor='nw',
            width=self.winfo_width(),
            height=height)

    def create_item(self, index: int, item: tuple[str, str]) -> ttk.Frame:
        frame = ttk.Frame(master=self.frame)

        # grid layout
        frame.rowconfigure(0, weight=1, uniform='a')
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'#{index+1}').grid(row=0, column=0, sticky='nsew')
        ttk.Label(frame, text=item[0], border=5, relief=tk.RIDGE).grid(row=0, column=1, sticky='nsew')
        ttk.Button(frame, text=item[1]).grid(row=0, column=2, columnspan=3, sticky='nsew')

        return frame

# setup window
window = tk.Tk()
window.title('Scrollable Widgets')
window.geometry('500x400+600+300')

text_list: list[tuple[str, str]] = [('label', 'button'), ('thing', 'click'), ('third', 'something'),
                                    ('fourth', 'test'), ('fifth', 'hello'), ('sixth', 'world')]
list_frame = ListFrame(window, text_list, 100)

# run
window.mainloop()
