
from time import sleep
from tkinter import *
from tkinter import ttk
from heap import *
from Tabuleiro import *


global estadoAtual
global zero
global l1
global podeAlterar

estadoAtual = list(range(9))
#estadoAtual = [1,0,2,3,4,5,6,7,8,9]
zero = busca_zero(estadoAtual)
l1 = []
podeAlterar = True


def chamaAle():
    global estadoAtual
    global zero
    global podeAlterar

    if podeAlterar:
        estadoAtual = gerar_tabuleiro_aleatorio()
        zero = busca_zero(estadoAtual)
        atualiza()

def trocaUp():
    global estadoAtual
    global zero

    if podeAlterar and trocavel(zero, zero-3):
        troca(estadoAtual, zero, zero-3)
        zero -= 3
        atualiza()

def trocaDown():
    global estadoAtual
    global zero

    if podeAlterar and trocavel(zero, zero+3):
        troca(estadoAtual, zero, zero+3)
        zero += 3
        atualiza()

def trocaLeft():
    global estadoAtual
    global zero

    if podeAlterar and trocavel(zero, zero-1):
        troca(estadoAtual, zero, zero-1)
        zero -= 1
        atualiza()

def trocaRight():
    global estadoAtual
    global zero

    if podeAlterar and trocavel(zero, zero+1):
        troca(estadoAtual, zero, zero+1)
        zero += 1
        atualiza()

def resolver():
    global estadoAtual
    global podeAlterar
    global zero
    
    podeAlterar = False

    saida = resolve(estadoAtual)

    if saida != False:
        for i in saida:
            sleep(2)
            imprimeTabuleiro(i)
            estadoAtual = i
            atualiza()
        zero = 0

    podeAlterar = True

def atualiza():
    global estadoAtual
    global l1

    for i in range(9):
        l1[i].set(estadoAtual[i])

janela= Tk()


janela.title("Quebra-cabeças de 8 peças")
janela.minsize(width=800, height=800)
janela.maxsize(width=800, height=800)



font1=('Times',22,'normal')
linha,coluna=0,0
labels=[]
indiceX=0.5
indiceY=0.5

for i in range(9):
    l1.append(StringVar())
    l1[i].set(estadoAtual[i])


for data in l1:
    label=ttk.Label(janela,textvariable=data,font=font1, foreground= "red", background="white")
    
    label.grid(row=linha,column=coluna,padx=50,pady=50)
    coluna=coluna+1
  
    label.place(relx = indiceX,rely = indiceY,anchor = 'center',x=-80,y=-80)
    indiceX+=0.1
    if coluna>=3:
        indiceY+=0.1
        linha+=1
        coluna=0
        indiceX=0.5


geraAleatoriosBotao= Button(janela, text="Gerar aleatorios",command= chamaAle)
geraAleatoriosBotao.place(x=10,y=10)

geraAleatoriosBotao.configure(height = 10,
                             width = 20)

Resolver= Button(janela, text="Resolver", command= resolver)
Resolver.place(x=640,y=10)
Resolver.configure(height = 10,width = 20)


global laabel
laabel=ttk.Label(janela, text="aaa", font=('Aerial 18'))
laabel.place(relx = indiceX,rely = indiceY,anchor = 'center',x=-60,y=85)



Cima= Button(janela, text="↑", command= trocaUp)
Cima.place(x=360,y=100)
Cima.configure(height = 5,width = 10)

Esquerda= Button(janela, text="←", command= trocaLeft)
Esquerda.place(x=100,y=360)
Esquerda.configure(height = 5,width = 10)

Direita= Button(janela, text="→", command= trocaRight)
Direita.place(x=600,y=360)
Direita.configure(height = 5,width = 10)

Baixo= Button(janela, text=" ↓", command= trocaDown)
Baixo.place(x=360,y=600)
Baixo.configure(height = 5,width = 10)



janela.mainloop()