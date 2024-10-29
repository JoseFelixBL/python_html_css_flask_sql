from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image')

# imagen = Image.open('Periponcio.png')
# # Abre la imagen en el programa que el SO tenga configurado, pero no la incluye en nuestra interfaz
# imagen.show()

# De esta forma sí podemos incluir la imagen en la interfaz
img = ImageTk.PhotoImage(Image.open('Periponcio.png'))
l = Label(image=img)
l.pack()

root.mainloop()
