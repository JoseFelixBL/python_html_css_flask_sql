from tkinter import *

root = Tk()
root.title('Hola mundo!')
root.geometry('500x500')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto:")


def click():
    texto = e.get()
    l.configure(text=texto)


def click2():
    texto = e.get()
    l2 = Label(root, text=texto)
    l2.pack()
    e.delete(0, END)


btn = Button(root, text='Click', command=click)
btn.pack()

btn2 = Button(root, text='Click2', command=click2)
btn2.pack()

l = Label(root, text='Texto de la etiqueta')
l.pack()


root.mainloop()
