from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Carrusel de imágenes')

img_path = '30-tkinter\\images'
lst_img = []
for img in os.listdir(img_path):
    photo = ImageTk.PhotoImage(Image.open((img_path + '\\' + img)))
    lst_img.append(photo)

l = Label(root, image=lst_img[0])
l.grid(row=0, column=0, columnspan=3)


def otra_imagen(img_num):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    btn_adelante.grid_forget()
    btn_atras.grid_forget()

    l = Label(root, image=lst_img[img_num])
    btn_atras = Button(
        root, text='<-', command=lambda: otra_imagen(img_num - 1))
    btn_adelante = Button(
        root, text='->', command=lambda: otra_imagen(img_num + 1))

    if img_num + 1 == len(lst_img):
        btn_adelante = Button(
            root, text='N/A', state=DISABLED)

    if img_num == 0:
        btn_atras = Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)


btn_atras = Button(root, text='N/A', state=DISABLED)
btn_adelante = Button(root, text='->', command=lambda: otra_imagen(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()
