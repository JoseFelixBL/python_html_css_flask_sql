from tkinter import *

root = Tk()
root.title('Sliders')

# Obtener los valores de forma continua con cada cambio del slider
vertical = Scale(root, from_=0, to=200, command=lambda x: enviar())
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


def enviar():
    hor = horizontal.get()
    ver = vertical.get()
    print(str(hor) + ' ' + str(ver))


# Obtener los valores de forma discreta cuando se presione un botón
btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
