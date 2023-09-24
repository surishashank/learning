import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.title('Scrolling')
window.geometry('600x400+600+300')

# # canvas
# canvas = tk.Canvas(master=window, bg='red', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)
# for i in range(100):
#     l = randint(0, 2000)
#     t = randint(0, 5000)
#     r = randint(l, 2000)
#     b = randint(t, 5000)
#     color = choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
#     canvas.create_rectangle(l, t, r, b, fill=color)
# canvas.pack(fill=tk.BOTH, expand=True)
#
# # mousewheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta), 'units'))
# canvas.bind('<Shift-MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta), 'units'))
#
# # vertical scrollbar
# vertical_scrollbar = ttk.Scrollbar(master=window, orient=tk.VERTICAL, command=canvas.yview)
# canvas.configure(yscrollcommand=vertical_scrollbar.set)
# vertical_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
#
# # horizontal scrollbar
# horizontal_scrollbar = ttk.Scrollbar(master=window, orient=tk.HORIZONTAL, command=canvas.xview)
# canvas.configure(xscrollcommand=horizontal_scrollbar.set)
# horizontal_scrollbar.place(relx=0, rely=1, relwidth=1, anchor=tk.SW)

# # text
# text = tk.Text(master=window, wrap=tk.WORD)
# for i in range(100):
#     text.insert(tk.END, f'line {i}\n')
# text.pack(fill=tk.BOTH, expand=True)
#
# # vertical scrollbar
# vertical_scrollbar = ttk.Scrollbar(master=window, orient=tk.VERTICAL, command=text.yview)
# text.configure(yscrollcommand=vertical_scrollbar.set)
# vertical_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)

# treeview
table = ttk.Treeview(master=window, columns=(1,2), show='headings')
table.heading(1, text='First name')
table.heading(2, text='Last name')
first_names = ['John', 'Jane', 'Jack', 'Jill', 'Joe', 'Jen', 'Jim', 'Jenny', 'Jeff', 'Jade']
last_names = ['Smith', 'Doe', 'Johnson', 'Jackson', 'Jones', 'Jenkins', 'Jameson', 'Jefferson', 'Jennings', 'Jagger']
for i in range(100):
    table.insert('', tk.END, values=(choice(first_names), choice(last_names)))
table.pack(fill=tk.BOTH, expand=True)

# vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(master=window, orient=tk.VERTICAL, command=table.yview)
table.configure(yscrollcommand=vertical_scrollbar.set)
vertical_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)

# run
window.mainloop()
