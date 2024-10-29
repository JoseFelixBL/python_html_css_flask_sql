from tkinter import *

root = Tk()
root.title('Checkbutton')

root.geometry('500x500')

var = StringVar()
# Si no le asignamos un valor por defecto al comienzo está indefinida
var.set('chanchito feliz')

c = Checkbutton(root, text='Soy un Checkbutton', variable=var,
                onvalue='si', offvalue='chanchito feliz')
c.pack()


def mostrar():
    l = Label(root, text=var.get())
    l.pack()


btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()
