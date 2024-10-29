from tkinter import *
import sqlite3

root = Tk()
root.title('Hola mundo: todo list')
root.geometry('500x500')

conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

conn.commit()
