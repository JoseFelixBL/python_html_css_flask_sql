from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('Libreta de clientes - CRM')

conn = sqlite3.connect('crm.db')

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            TELEFONO TEXT NOT NULL,
            EMPRESA TEXT NOT NULL
          );
""")


def nuevo_cliente():
    pass


def eliminar_cliente():
    pass


btn = Button(root, text='Nuevo Cliente', command=nuevo_cliente)
btn.grid(row=0, column=0)

btn_eliminar = Button(root, text='Eliminar Cliente', command=eliminar_cliente)
btn_eliminar.grid(row=0, column=1)

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')
tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Teléfono')
tree.heading('Empresa', text='Empresa')
tree.grid(row=1, column=0, columnspan=2)

root.mainloop()
