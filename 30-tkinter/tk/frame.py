from tkinter import *

root = Tk()
root.title('Usando Frames')

# Los Frame no tiene texto ni marco, pero igualmente agrupan widgets
frame = Frame(root, padx=10, pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)


l = Label(frame, text='Estoy dentro de un Frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()
