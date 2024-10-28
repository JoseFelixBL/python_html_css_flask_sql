from tkinter import *

root = Tk()
root.title('Pies a metros')


def calcular(*args):
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 + 0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set('ERROR')


frame = Frame(root, padx=12, pady=3)
frame.grid(row=0, column=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(row=0, column=1)

metros = StringVar()
Label(frame, textvariable=metros).grid(row=1, column=1)

Button(frame, text='Calcular', command=calcular).grid(row=2, column=2)

Label(frame, text='Pies').grid(row=0, column=2)
Label(frame, text='es igual a').grid(row=1, column=0)
Label(frame, text='metros').grid(row=1, column=2)

# Focus hace que cuando se abra la aplicación el campo estará ya "enfocado", o sea, no habrá que darle con el ratón
pies_input.focus()
# Bind enlaza un evento con una función, en este caso el Return con la función calcular
root.bind("<Return>", calcular)
root.mainloop()
