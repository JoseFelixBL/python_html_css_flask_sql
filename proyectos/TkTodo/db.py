from tkinter import *
import sqlite3

root = Tk()
root.title('Hola mundo: todo list')
root.geometry('400x500')

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


# Currying!
def complete(id):
    def _complete():
        todo = c.execute('SELECT * FROM todo WHERE id = ?', (id, )).fetchone()
        c.execute('UPDATE todo SET completed = ? WHERE id = ?',
                  (not todo[3], id))
        conn.commit()
        render_todos()

    return _complete


# Currying!
def remove(id):
    def _remove():
        c.execute('DELETE FROM todo WHERE id = ?', (id, ))
        conn.commit()
        render_todos()

    return _remove


def render_todos():
    rows = c.execute("SELECT * FROM todo").fetchall()

    for widget in frame.winfo_children():
        widget.destroy()

    for i, row in enumerate(rows):
        id = row[0]
        completed = row[3]
        description = row[2]
        color = '#999999' if completed else '#000000'
        cb = Checkbutton(frame, text=description, fg=color, width=42,
                         anchor='w', command=complete(id))
        cb.grid(row=i, column=0, sticky='w')
        btn = Button(frame, text='Eliminar', command=remove(id))
        btn.grid(row=i, column=1)
        cb.select() if completed else cb.deselect()


def addTodo():
    todo = e.get()
    if todo:
        c.execute("""
                    INSERT INTO todo (description, completed) VALUES (?, ?)
                """, (todo, False)
                  )
        conn.commit()
        e.delete(0, END)
        render_todos()
    else:
        pass


l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=addTodo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text='Mis tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

e.focus()

render_todos()

root.bind('<Return>', lambda x: addTodo())
root.mainloop()
