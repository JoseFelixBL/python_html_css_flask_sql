from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Messagebox')


# def click():
# messagebox.showwarning('Popup', 'Hola mundo')


# def click():
#     messagebox.showinfo('Popup', 'Hola mundo')

# def click():
#     messagebox.showerror('Popup', 'Hola mundo :(')

# def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola mundo ?')
#     # print(respuesta)
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', ':( la respuesta fue ' + respuesta)

# def click():
#     respuesta = messagebox.askokcancel('Hola mundo', '¿Desea realizar acción?')
#     # print(respuesta)
#     if respuesta:
#         messagebox.showinfo('Hola mundo', 'la respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola mundo', ':( la respuesta fue CANCELAR')

def click():
    respuesta = messagebox.askyesno('Hola mundo', '¿Desea realizar acción?')
    # print(respuesta)
    if respuesta:
        messagebox.showinfo('Hola mundo', 'la respuesta fue YES')
    else:
        messagebox.showinfo('Hola mundo', ':( la respuesta fue NO')


btn = Button(root, text='Presióname', command=click)
btn.pack()

root.mainloop()
