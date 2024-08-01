import requests
from tkinter import *
 
def pegar_cotacao():
    requisicao= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    rqs_list = requisicao.json()

    dolarAtual=rqs_list['USDBRL']['bid']
    euroAtual=rqs_list['EURBRL']['bid']
    btcAtual=rqs_list['BTCBRL']['bid']
    
    texto = f'''
    DOLAR:{dolarAtual}
    EURO:{euroAtual}
    BTC:{btcAtual}'''

    #print(texto)
    texto_resposta["text"] = texto

def limpar ():
    texto_resposta["text"]=""
#pegar_cotacao() #comentariorrr

root=Tk()
root.title("janelinha veyr")
root.geometry("400x200")

texto= Label (root, text= "Clique no botãozinho para ver a cotaçãozinha das moedinhas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao= Button(root,text="buscar cotaçõeszinhas", command=pegar_cotacao)
botao.grid(column=0, row=1, padx=5, pady=0)

texto_resposta= Label (root, text= "")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

root.mainloop()
