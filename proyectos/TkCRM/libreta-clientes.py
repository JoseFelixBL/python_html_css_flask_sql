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
# conn.commit()

root.mainloop()
