from tkinter import *

root = Tk()
root.title('Hola mundo!')

# Si instanciamos Label fuera de la función habrá solo una etiqueta
l = Label(root, text='Hola MUNDO')


def click():
    # Si instanciamos la etiqueta dentro de la función habrá muchas etiquetas
    # l = Label(root, text='Hola MUNDO')
    l.pack()


btn = Button(root, text='Clikéame', command=click, fg='#ffff00', bg='blue')
btn.pack()

root.mainloop()
