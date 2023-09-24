import customtkinter as ctk

# Create a window
window = ctk.CTk()
window.title('customtkinter App')
window.geometry('600x400+600+300')

# Create a label
string_var = ctk.StringVar(value='a custom string')
label = ctk.CTkLabel(master=window, text='A Label', fg_color=('blue', 'red'),
                     corner_radius=10, textvariable=string_var)
label.pack(fill=ctk.BOTH)

# Create a button
button = ctk.CTkButton(master=window, text='A Button', fg_color='yellow', text_color='black',
                       hover_color='pink', command=lambda: ctk.set_appearance_mode('light'))
button.pack()

# Create a frame
frame = ctk.CTkFrame(master=window, fg_color='grey')
frame.pack()

slider = ctk.CTkSlider(master=frame)
slider.pack(padx=10, pady=10)

# create a switch
switch = ctk.CTkSwitch(master=frame, switch_width=60, switch_height=25, corner_radius=2,
                       border_width=3, border_color='blue', progress_color='pink',
                       text='Exercise Switch', fg_color='red', button_color='green',
                       button_hover_color='yellow')
switch.pack(padx=10, pady=10)

# run
window.mainloop()
