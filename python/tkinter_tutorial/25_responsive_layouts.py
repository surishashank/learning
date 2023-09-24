import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size: tuple[int, int]):
        super().__init__()
        self.title('Responsive Layouts')
        self.geometry(f'{start_size[0]}x{start_size[1]}')

        self.frame: ttk.Frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        SizeNotifier(self, {300: self.create_small_layout,
                            600: self.create_medium_layout,
                            1200: self.create_large_layout})

        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        ttk.Label(self.frame, text='Label 1', borderwidth=2, relief=tk.GROOVE).pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 2', borderwidth=2, relief=tk.GROOVE).pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 3', borderwidth=2, relief=tk.GROOVE).pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 4', borderwidth=2, relief=tk.GROOVE).pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight=1, uniform='group1')
        self.frame.rowconfigure((0,1), weight=1, uniform='group1')
        self.frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.frame, text='Label 1', borderwidth=2, relief=tk.GROOVE).grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 2', borderwidth=2, relief=tk.GROOVE).grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 3', borderwidth=2, relief=tk.GROOVE).grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 4', borderwidth=2, relief=tk.GROOVE).grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)

    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1,2,3), weight=1, uniform='group1')
        self.frame.rowconfigure(0, weight=1, uniform='group1')
        self.frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.frame, text='Label 1', borderwidth=2, relief=tk.GROOVE).grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 2', borderwidth=2, relief=tk.GROOVE).grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 3', borderwidth=2, relief=tk.GROOVE).grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)
        ttk.Label(self.frame, text='Label 4', borderwidth=2, relief=tk.GROOVE).grid(row=0, column=3, sticky=tk.NSEW, padx=5, pady=5)

class SizeNotifier:
    def __init__(self, window: App, size_dict: dict[int, callable]):
        self.window: App = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None
        self.window.bind('<Configure>', self.check_size)

        self.window.update()
        min_height = self.window.winfo_height()
        min_width = min(self.size_dict.keys())
        self.window.minsize(width=min_width, height=min_height)

    def check_size(self, event: tk.Event):
        if event.widget != self.window:
            return

        window_width: int = event.width
        checked_size = None

        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
                checked_size = min_size

        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[checked_size]()

app = App((400, 300))
