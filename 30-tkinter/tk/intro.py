from tkinter import *

root = Tk()  # Crear el objeto Tk
root.title('Hola mundo')  # Nombre de la ventana
root.geometry('400x400')  # ancho x alto

l1 = Label(root, text='Hola mundo! primera etiqueta')
l2 = Label(root, text='Chao mundo! segunda etiqueta')
l3 = Label(root, text='                ')

l1.grid(row=0, column=0)
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)

root.mainloop()  # Ejecutar la ventana, escucha a la espera de cambios
