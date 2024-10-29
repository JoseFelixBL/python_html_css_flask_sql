from tkinter import *

root = Tk()
root.title('OptionMenu = Dropdown')
root.geometry('500x500')


def enviar():
    global l
    l.forget()  # Para no poner una etiqueta debajo cada vez que se presiona Enviar
    l = Label(root, text=value.get())
    l.pack()


lista = [
    'Chanchito feliz',
    'Chanchito triste',
    'Chanchito emocionado'
]

value = StringVar()
value.set(lista[0])

drop = OptionMenu(root, value, *lista)

# value.set('Chanchito feliz')
# drop = OptionMenu(root, value, 'Chanchito feliz',
#                   'Chanchito triste', 'Chanchito emocionado')

drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

l = Label(root, text=value.get())
l.pack()

root.mainloop()
