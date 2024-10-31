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
            telefono TEXT NOT NULL,
            empresa TEXT NOT NULL
          );
""")


def render_clientes():
    rows = c.execute('SELECT * FROM cliente').fetchall()
    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))


def insertar(cliente):
    c.execute("""
              INSERT INTO cliente (nombre, telefono, empresa) VALUES (?, ?, ?)
              """, (cliente['nombre'], cliente['telefono'], cliente['empresa']))
    conn.commit()
    render_clientes()


def nuevo_cliente():
    def guardar():
        if not enombre.get():
            messagebox.showerror('Error', 'El nombre es obligatorio')
            return
        if not etelefono.get():
            messagebox.showerror('Error', 'El teléfono es obligatorio')
            return
        if not eempresa.get():
            messagebox.showerror(
                'Error', 'El nombre de empresa es obligatorio')
            return

        cliente = {
            'nombre': enombre.get(),
            'telefono': etelefono.get(),
            'empresa': eempresa.get()
        }
        insertar(cliente)
        top.destroy()

    top = Toplevel()
    top.title('Nuevo cliente')

    lnombre = Label(top, text='Nombre')
    enombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    enombre.grid(row=0, column=1)

    ltelefono = Label(top, text='Teléfono')
    etelefono = Entry(top, width=40)
    ltelefono.grid(row=1, column=0)
    etelefono.grid(row=1, column=1)

    lempresa = Label(top, text='Empresa')
    eempresa = Entry(top, width=40)
    lempresa.grid(row=2, column=0)
    eempresa.grid(row=2, column=1)

    guardar = Button(top, text='Guardar', command=guardar)
    guardar.grid(row=3, column=1)

    # top.mainloop()


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

render_clientes()

root.mainloop()
