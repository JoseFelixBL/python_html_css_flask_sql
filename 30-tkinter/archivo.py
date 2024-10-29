from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Seleccionar Archivos usando interfaz gráfica')

# # Lo siguiente muestra el diálogo directamente
# root.filename = filedialog.askopenfilename(
#     title='Elige una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))
# l = Label(root, text=root.filename)
# l.pack()
# img = Image.open(root.filename)
# imgTk = ImageTk.PhotoImage(img)

# l2 = Label(root, image=imgTk)
# l2.pack()

# Haremos que presionando un botón se abra el diálogo


def open():
    global imgTk
    root.filename = filedialog.askopenfilename(
        title='Elige una foto', filetypes=(("Archivos PNG", "*.png"), ('Todos', '*')))

    l = Label(root, text=root.filename)
    l.pack()

    img = Image.open(root.filename)
    imgTk = ImageTk.PhotoImage(img)

    l2 = Label(root, image=imgTk)
    l2.pack()


btn = Button(root, text='Cargar imagen', command=open)
btn.pack()

root.mainloop()
