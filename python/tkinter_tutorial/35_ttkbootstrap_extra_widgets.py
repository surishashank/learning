from PIL import Image
Image.CUBIC = Image.BICUBIC
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

# window
window = ttk.Window(themename='darkly')
window.title('ttkbootstrap extra widgets')
# window.geometry('600x600+400+100')

# scrollable frame
scroll_frame = ScrolledFrame(master=window)
scroll_frame.pack(fill='both', expand=True)

for i in range(50):
    frame = ttk.Frame(master=scroll_frame)
    ttk.Label(master=frame, text=f'Label {i}').pack(pady=10, side=ttk.LEFT)
    ttk.Button(master=frame, text=f'Button {i}').pack(pady=10, side=ttk.LEFT)
    frame.pack(fill='x', pady=10, expand=True)

# toast
toast = ToastNotification(title='This is a message title',
                          message='This is the actual message',
                          duration=1000,
                          bootstyle='dark',
                          position=(0, 0, 'nw'))
ttk.Button(master=window, text='Show Toast', command=toast.show_toast).pack(pady=10)

# tooltip
button = ttk.Button(master=window, text='Tooltip Button', bootstyle='warning')
button.pack(pady=10)
ToolTip(button, text='This is a tooltip message')

# calendar
calendar = DateEntry(master=window)
calendar.pack(pady=10)

ttk.Button(master=window, text='Get Date', command=lambda: print(calendar.entry.get())).pack(pady=10)

# progress -> floodgauge
progress_int = ttk.IntVar(value=50)
progress = Floodgauge(master=window,
                      text='Progress',
                      variable=progress_int,
                      mask='{}%')
progress.pack(pady=10, fill='x')

ttk.Scale(master=window, variable=progress_int, from_=0, to=100, orient='horizontal').pack(pady=10, fill='x')

# meter
meter_int = ttk.IntVar(value=10)
meter = ttk.Meter(master=window,
                  amounttotal=100,
                  amountused=10,
                  interactive=True,
                  metertype='semi',
                  subtext='miles/hr')
meter.pack(pady=10, fill='x')

# run
window.mainloop()
