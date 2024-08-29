from tkinter import *
import sqlite3
from tkinter import messagebox

# criando a interface
janela = Tk()
janela.title("Agenda")

txtnome = Entry(janela)
nome = Label(janela, text="nome").grid(column=0, row=0)
txtnome.grid(column=0, row=1)

end = Label(janela, text="Endereço").grid(column=0, row=2)
txtend = Entry(janela)
txtend.grid(column=0, row=3)

fone = Label(janela, text="Telefone").grid(column=0, row=4)
txtfone = Entry(janela)
txtfone.grid(column=0, row=5)

def salva():
    bd = sqlite3.connect('Agenda.db')
    cv = bd.cursor()
    # criar a primeira tabela se ela não existir
    cv.execute("Create table if not exists contatos(nome text, endereco text, fone text)")
    n = txtnome.get()
    e = txtend.get()
    p = txtfone.get()
    if (n == "" and e == "" and p == ""):
        messagebox.showinfo("Campos vazios", "Todos os campos devem ser preenchidos")
    else:
        cv.execute("insert into contatos values (?,?,?)", (n, e, p))
        bd.commit()
        messagebox.showinfo("Salvo", "Dados salvos com sucesso!")
        bd.close()

btsalva = Button(janela, text="Guardar", command=salva).grid(column=0, row=7)

janela.mainloop()