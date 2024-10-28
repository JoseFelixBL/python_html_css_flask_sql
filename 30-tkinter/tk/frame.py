from tkinter import *

root = Tk()
root.title('Usando Frames')

# Este padding es para dentro del marco
frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=10)
# Este padding es para afuera del marco
frame.pack(padx=50, pady=50)

frame_sin = LabelFrame(root, padx=10, pady=10, borderwidth=10)
frame_sin.pack(padx=50, pady=50)

l = Label(frame, text='Estoy dentro de un Frame')
l.pack()

btn = Button(frame_sin, text='Salir', command=root.quit)
btn.pack()

root.mainloop()
