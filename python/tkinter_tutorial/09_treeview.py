import tkinter as tk
from tkinter import ttk
from random import choice

# setup
window = tk.Tk()
window.title('Treeview')
window.geometry('600x400')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Peter']
last_names = ['Smith', 'Garcia', 'Hernandez', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller']

# treeview
table = ttk.Treeview(master=window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Last Name')
table.heading('email', text='Email')
table.pack(fill=tk.BOTH, expand=True)

# insert values into a table
for i in range(50):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first.lower()}.{last.lower()}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)
table.insert(parent='', index=tk.END, values=('XXXXX', 'YYYYY', 'ZZZZZ'))

# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# run
window.mainloop()
