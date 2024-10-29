from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Window')


# Solución 1: poniendo el mainloop de la segunda ventana
# def open():
#     img = ImageTk.PhotoImage(Image.open('30-tkinter\\Periponcio.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()
#
# btn = Button(root, text='Click', command=open).pack()


# Solución 2: definir la variable img como global así no se pierde el contexto y el mainloop 1 la muestra
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('30-tkinter\\Periponcio.png'))
#     top = Toplevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy un texto en una segunda ventana')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#
# btn = Button(root, text='Click', command=open).pack()


# Solución 3: Definir la variable antes y pasarla como un argumento
def open(img):
    top = Toplevel()
    top.title('Hola mundo, nueva ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()


img = ImageTk.PhotoImage(Image.open('30-tkinter\\Periponcio.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()


root.mainloop()
