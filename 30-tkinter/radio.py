from tkinter import *

root = Tk()
root.title('Radio Button List')

CHANCHITOS = [
    ('Feliz', 'Feliz'),
    ('Triste', 'Triste'),
    ('Amargado', 'Amargado'),
    ('Wolfgang', 'Wolfgang')
]

chanchito = StringVar()
chanchito.set('Wolfgang')
for texto, chancho in CHANCHITOS:
    Radiobutton(root, text=texto, variable=chanchito, value=chancho).pack()

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()
