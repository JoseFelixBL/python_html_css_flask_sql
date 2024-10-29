from tkinter import *

root = Tk()
root.configure(background='#333')
root.title('Calculadora')
# root.geometry('386x168')

equation = StringVar()


def press(num):
    equation.set(equation.get() + str(num))


def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('error')


def clear():
    equation.set('')


expression_entry = Entry(root, textvariable=equation,
                         background='#000', foreground='white', )
expression_entry.grid(columnspan=4, row=0, sticky='nswe')

btn7 = Button(root, text=' 7 ', fg='#111',
              bg='#666', width='10', command=lambda: press(7))
btn7.grid(row=1, column=0, sticky='nswe')

btn8 = Button(root, text=' 8 ', fg='#111',
              bg='#666', width='10', command=lambda: press(8))
btn8.grid(row=1, column=1, sticky='nswe')

btn9 = Button(root, text=' 9 ', fg='#111',
              bg='#666', width='10', command=lambda: press(9))
btn9.grid(row=1, column=2, sticky='nswe')

btn4 = Button(root, text=' 4 ', fg='#111',
              bg='#666', width='10', command=lambda: press(4))
btn4.grid(row=2, column=0, sticky='nswe')

btn5 = Button(root, text=' 5 ', fg='#111',
              bg='#666', width='10', command=lambda: press(5))
btn5.grid(row=2, column=1, sticky='nswe')

btn6 = Button(root, text=' 6 ', fg='#111',
              bg='#666', width='10', command=lambda: press(6))
btn6.grid(row=2, column=2, sticky='nswe')

btn1 = Button(root, text=' 1 ', fg='#111',
              bg='#666', width='10', command=lambda: press(1))
btn1.grid(row=3, column=0, sticky='nswe')

btn2 = Button(root, text=' 2 ', fg='#111',
              bg='#666', width='10', command=lambda: press(2))
btn2.grid(row=3, column=1, sticky='nswe')

btn3 = Button(root, text=' 3 ', fg='#111',
              bg='#666', width='10', command=lambda: press(3))
btn3.grid(row=3, column=2, sticky='nswe')

btn0 = Button(root, text=' 0 ', fg='#111',
              bg='#666', width='10', command=lambda: press(0))
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

decimal = Button(root, text=' . ', fg='#111',
                 bg='#666', width='10', command=lambda: press('.'))
decimal.grid(row=4, column=2, sticky='nswe')

plus = Button(root, text=' + ', fg='#111',
              bg='#fe9727', width='10', command=lambda: press('+'))
plus.grid(row=1, column=3, sticky='nswe')

minus = Button(root, text=' - ', fg='#111',
               bg='#fe9727', width='10', command=lambda: press('-'))
minus.grid(row=2, column=3, sticky='nswe')

multiply = Button(root, text=' * ', fg='#111',
                  bg='#fe9727', width='10', command=lambda: press('*'))
multiply.grid(row=3, column=3, sticky='nswe')

divide = Button(root, text=' / ', fg='#111',
                bg='#fe9727', width='10', command=lambda: press('/'))
divide.grid(row=4, column=3, sticky='nswe')

equal = Button(root, text=' = ', fg='#111',
               bg='#fe9727', width='10', command=equalpress)
equal.grid(row=5, column=3, sticky='nswe')

clear = Button(root, text='clear', fg='#111',
               bg='#999', width='10', command=clear)
clear.grid(row=5, column=2, sticky='nswe')

# frame = Frame(root, padx=12, pady=3)
# frame.grid(row=0, column=0)

root.mainloop()
