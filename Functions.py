import datetime
from tkinter import *
import threading
from tkinter import ttk
import time
from tkinter.ttk import *
import os
import pandas as pd


def consolida():
    from gui import bar
    bar['value'] = 0
    inicio = time.time()
    lista = os.listdir('dados')
    lista2 = []
    tamanho = len(lista)
    #print(lista[0])
    i = 0
    while i < tamanho:
        lgn_label = ttk.Label(background="#1a1a1a", foreground='#d2fa00', text=" Carregando...   "+str(i+1)+"/"+str(tamanho), anchor=SW)
        lgn_label.place(x=1, y=210, width=350)
        li = pd.read_excel('dados/'+lista[i], sheet_name='BD')
        lista2.append(li)
        bar['value'] += (100 / int(tamanho))
        app.update()
        i += 1
    # concat both DataFrame into a single DataFrame
    df = pd.concat(lista2, ignore_index=True)
    # Export Dataframe into Excel file
    novo_titulo = 'CLIENTE PAGADOR'
    df = df.rename(columns={' CLIENTE PAGADOR': novo_titulo})
    coluna_para_excluir = 'chave de controle'
    coluna_para_excluir2 = 'Status final gris'
    df = df.drop(coluna_para_excluir, axis=1)
    df = df.drop(coluna_para_excluir2, axis=1)
    colunas = 'EMPRESA'
    df = df.dropna(subset=colunas)

    lgn_label = ttk.Label(background="#1a1a1a", foreground='#d2fa00', text="Consolidando...", anchor=SW)
    lgn_label.place(x=1, y=210, width=350)
    hora = int(time.time())
    df.to_excel(f'Consolidado_{hora}.xlsx', sheet_name='Base', index=False)
    fim = time.time()
    tempo = int(fim - inicio)
    ftempo = datetime.timedelta(seconds = tempo)    
    lgn_label = ttk.Label(background="#1a1a1a", foreground='#d2fa00', text="Concluido!", anchor=SW)
    lgn_label.place(x=1, y=210, width=350)
    tkinter.messagebox.showinfo(title="Concluido!", message="Relatório gerado com sucesso!"+ "\n\nTempo de processamento: " + str(ftempo))


def chama_funcao():
    threading.Thread(target=consolida).start()