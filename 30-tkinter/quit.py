from tkinter import *

root = Tk()
root.title('Quit')

exit = Button(root, text='Salir', command=root.quit)
exit.pack()

root.mainloop()
