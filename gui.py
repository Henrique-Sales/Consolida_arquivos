

from Functions import chama_funcao
from tkinter import *
import tkinter
from tkinter.ttk import *

app = Tk()
app.geometry("400x240")

app.configure(background="#1a1a1a")
p1 = tkinter.PhotoImage(file='icones/icon.png')
app.iconphoto(False, p1)
app.title("Unifica Relatórios")
bar = Progressbar(app, orient=HORIZONTAL, length=350)
bar.pack(pady=70)

# Foto de icone
p1 = tkinter.PhotoImage(file='icones/icon.png')
app.iconphoto(False, p1)

# Botão gerar extravio
button = tkinter.Button(master=app,background="#d2fa00" ,text="Gerar consolidado", command=chama_funcao)
button.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)