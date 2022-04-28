from tkinter import *
from tkinter import ttk
from code import *

janela = Tk()
frame = ttk.Frame(janela, padding=20)
frame.grid()
janela.title('Fórmula Mágica de Joel Greenblatt')
ttk.Label(frame, text='Olá, investidores!').grid(column=0, row=1)
ttk.Label(frame, text='Clique no botão pra rodar a Fórmula Mágica').grid(column=0, row=2)
ttk.Button(frame, text='Sair', command=janela.destroy).grid(column=1, row=1)
ttk.Button(frame, text='Rodar a Fórmula Mágica', command=formula_magica).grid(column=1, row=2)


janela.mainloop()
