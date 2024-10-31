from tkinter import *

# Hay 5 pasos básicos para usar Treeview:
# 1. Importar ttk
from tkinter import ttk

root = Tk()
root.title('Mostrar datos con Treeview')

# 2. Crear el Treeview
tree = ttk.Treeview(root)

# 3. Configurar las columnas
# 3.1 Qué columnas quiero
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

# 3.2 Especificar los índices de c/u de las columnas
# Siempre hay una columna '#0' de índice
# tree.column('#0')
# con el stretch = NO no se ve el '+' para expandir los hijos, pero puedo hacer Doble-click
tree.column('#0', width=0, stretch=YES)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

# 3.3 Especificar los Headings de las columnas
# tree.heading('#0', text='id')
tree.heading('#0')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Teléfono')
tree.heading('Empresa', text='Empresa')

# 4. Insertar ITEMS - Se pueden insertar después de mostrar el tree...

"""# 4.1 Puede ser como una lista de tuplas:

items = [
    ('John Doe', '123456', 'Engineers Inc.'),
    ('Jane Smith', '456789', 'Marketing & Com.'),
    ('Bob Johnson', '789123', 'Tk Leaders')
]

for item in items:
    tree.insert('', END, values=item)"""

"""
# 4.2 ... como una lista de diccionarios:

# Fetch data from database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM clientes")
data = cursor.fetchall()

data = [
    ('John Doe', '123456', 'Engineers Inc.'),
    ('Jane Smith', '456789', 'Marketing & Com.'),
    ('Bob Johnson', '789123', 'Tk Leaders')
]

# Prepare data for Treeview
tree_data = [{"Nombre": row[0], "Telefono": row[1],
              "Empresa": row[2]} for row in data]

# Insert data into Treeview
for item in tree_data:
    tree.insert("", "end", values=(
        item["Nombre"], item["Telefono"], item["Empresa"]))"""

# 4.3 ...Uno a uno especificando cada campo:

tree.insert('', END, 'lala', values=(
    'Uno', 'Dos', 'Tres'), text='Chanchito feliz')
tree.insert('', END, 'lele', values=(
    'Cuatro', 'Cinco', 'Seis'), text='Chanchito Triste')
tree.insert('lele', END, 'lili', values=('4', '5', '6'), text='Hijo')

# 5. Mostrar/Display el widget
tree.grid(row=0, column=0)

root.mainloop()
