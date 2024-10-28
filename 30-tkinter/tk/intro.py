from tkinter import *

root = Tk()  # Crear el objeto Tk
root.title('Hola mundo')  # Nombre de la ventana
root.geometry('400x400')  # ancho x alto

label = Label(root, text='Hola mundo! mi primera etiqueta')
Label(root, text='Hola mundo! mi SEGUNDA etiqueta').pack()

label.pack()

root.mainloop()  # Ejecutar la ventana, escucha a la espera de cambios
