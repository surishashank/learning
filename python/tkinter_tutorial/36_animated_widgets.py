import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)
        self.start_pos = start_pos + 0.02
        self.end_pos = end_pos - 0.02
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backward)
        else:
            self.in_start_pos = True

def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx=button_x, rely=0.5, anchor=ctk.CENTER)
    if button_x < 1:
        window.after(10, move_btn)

# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400+600+300')

# animated widget
animated_panel = SlidePanel(parent=window, start_pos=1, end_pos=0.7)
ctk.CTkLabel(master=animated_panel, text='Label 1').pack(expand=True, fill=ctk.BOTH)
ctk.CTkLabel(master=animated_panel, text='Label 2').pack(expand=True, fill=ctk.BOTH)
ctk.CTkButton(master=animated_panel, text='Button 1').pack(expand=True, fill=ctk.BOTH)
ctk.CTkTextbox(master=animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill=ctk.BOTH)

# button
button_x = 0.5
button = ctk.CTkButton(master=window, text='Toggle Sidebar', command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor=ctk.CENTER)

# run
window.mainloop()
