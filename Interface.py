
import Heap
import Tabuleiro
import tkinter
import time
import threading
import keyboard
import os


global estadoAtual
global zero
global l1
global podeAlterar
global teclado
global textoLabel
global processando

estadoAtual = list(range(9))
zero = Tabuleiro.busca_zero(estadoAtual)
l1 = []
podeAlterar = True


def chamaAle():
    global estadoAtual
    global zero
    global podeAlterar

    if podeAlterar:
        estadoAtual = Tabuleiro.gerar_tabuleiro_aleatorio()
        zero = Tabuleiro.busca_zero(estadoAtual)
        atualiza()

def trocaUp():
    global estadoAtual
    global zero

    if podeAlterar and Tabuleiro.trocavel(zero, zero-3):
        Heap.troca(estadoAtual, zero, zero-3)
        zero -= 3
        atualiza()
    else:
        nova = threading.Thread(target=jogadaInvalida)
        nova.daemon = True
        nova.start()

def trocaDown():
    global estadoAtual
    global zero

    if podeAlterar and Tabuleiro.trocavel(zero, zero+3):
        Heap.troca(estadoAtual, zero, zero+3)
        zero += 3
        atualiza()
    else:
        nova = threading.Thread(target=jogadaInvalida)
        nova.daemon = True
        nova.start()

def trocaLeft():
    global estadoAtual
    global zero

    if podeAlterar and Tabuleiro.trocavel(zero, zero-1):
        Heap.troca(estadoAtual, zero, zero-1)
        zero -= 1
        atualiza()
    else:
        nova = threading.Thread(target=jogadaInvalida)
        nova.daemon = True
        nova.start()

def trocaRight():
    global estadoAtual
    global zero

    if podeAlterar and Tabuleiro.trocavel(zero, zero+1):
        Heap.troca(estadoAtual, zero, zero+1)
        zero += 1
        atualiza()
    else:
        nova = threading.Thread(target=jogadaInvalida)
        nova.daemon = True
        nova.start()

def jogadaInvalida():
    global textoLabel
    textoLabel.set("Jogada invalida!")
    time.sleep(1)
    textoLabel.set("")

def teclaUp():
    global teclado
    while teclado:
        keyboard.wait('w')
        trocaUp()

def teclaDown():
    global teclado
    while teclado:
        keyboard.wait('s')
        trocaDown()

def teclaLeft():
    global teclado
    while teclado:
        keyboard.wait('a')
        trocaLeft()

def teclaRight():
    global teclado
    while teclado:
        keyboard.wait('d')
        trocaRight()

def teclaUpSeta():
    global teclado
    while teclado:
        keyboard.wait("UP")
        trocaUp()

def teclaDownSeta():
    global teclado
    while teclado:
        keyboard.wait("DOWN")
        trocaDown()

def teclaLeftSeta():
    global teclado
    while teclado:
        keyboard.wait("LEFT")
        trocaLeft()

def teclaRightSeta():
    global teclado
    while teclado:
        keyboard.wait("RIGHT")
        trocaRight()

def chamaResolver():
    resolvedor = threading.Thread(target=resolver)
    resolvedor.daemon = True
    resolvedor.start()

def resolver():
    global estadoAtual
    global podeAlterar
    global zero
    global processando

    podeAlterar = False
    processando = True

    nova = threading.Thread(target = mensagemDeProcessamento)
    nova.daemon = True
    nova.start()

    saida = Tabuleiro.resolve(estadoAtual)

    processando = False
    for i in saida:
        estadoAtual = i
        atualiza()
        time.sleep(1)
    zero = 0

    podeAlterar = True

def mensagemDeProcessamento():
    global processando
    global textoLabel

    while processando:
        textoLabel.set("Processando    ")
        time.sleep(0.2)
        textoLabel.set("Processando .  ")
        time.sleep(0.2)
        textoLabel.set("Processando .. ")
        time.sleep(0.2)
        textoLabel.set("Processando ...")
        time.sleep(0.2)
    textoLabel.set("")

def atualiza():
    global estadoAtual
    global l1

    for i in range(9):
        if estadoAtual[i] != 0:
            l1[i].set(estadoAtual[i])
        else:
            l1[i].set(" ")

def telaStart():
    janela= tkinter.Tk()


    janela.title("Quebra-cabeças de 8 peças")
    janela.minsize(width=800, height=800)
    janela.maxsize(width=800, height=800)
    janela.config(bg = "#C0C0C0")

    pasta = os.path.dirname(__file__)
    image_borda = tkinter.PhotoImage(file= pasta+"\\Borda.png")
    borda = tkinter.Label(janela, image = image_borda, background= "#C0C0C0")
    borda.place(x = 188, y = 100)

    font1=('Times',22,'normal')
    linha,coluna=0,0
    indiceX=0.5
    indiceY=0.5

    for i in range(9):
        l1.append(tkinter.StringVar())
        if estadoAtual[i] != 0:
            l1[i].set(estadoAtual[i])
        else:
            l1[i].set(" ")


    for data in l1:
        label=tkinter.Label(janela,textvariable=data,font=font1, foreground= "red", background= "#C0C0C0")
        
        label.grid(row=linha,column=coluna,padx=50,pady=50)
        coluna=coluna+1
    
        label.place(relx = indiceX,rely = indiceY,anchor = 'center',x=-80,y=-80)
        indiceX+=0.1
        if coluna>=3:
            indiceY+=0.1
            linha+=1
            coluna=0
            indiceX=0.5


    geraAleatoriosBotao= tkinter.Button(janela, text="Gerar aleatorios",command= chamaAle)
    geraAleatoriosBotao.place(x=10,y=10)

    geraAleatoriosBotao.configure(height = 10, width = 20)

    Resolver= tkinter.Button(janela, text="Resolver", command= chamaResolver)
    Resolver.place(x=640,y=10)
    Resolver.configure(height = 10,width = 20)


    global textoLabel
    textoLabel = tkinter.StringVar()
    laabel = tkinter.Label(janela, textvariable=textoLabel, font=('Aerial 18'), wraplength= 300)
    laabel.place(relx = indiceX,rely = indiceY,anchor = 'center',y=50)



    Cima= tkinter.Button(janela, text="↑", command= trocaUp )
    Cima.place(x=360,y=180)
    Cima.configure(height = 5,width = 10)

    Esquerda= tkinter.Button(janela, text="←", command= trocaLeft)
    Esquerda.place(x=190,y=360)
    Esquerda.configure(height = 5,width = 10)

    Direita= tkinter.Button(janela, text="→", command= trocaRight)
    Direita.place(x=530,y=360)
    Direita.configure(height = 5,width = 10)

    Baixo= tkinter.Button(janela, text=" ↓", command= trocaDown)
    Baixo.place(x=360,y=530)
    Baixo.configure(height = 5,width = 10)

    global teclado
    teclado = True

    threads = []

    threads.append(threading.Thread(target=teclaUp))
    threads.append(threading.Thread(target=teclaDown))
    threads.append(threading.Thread(target=teclaLeft))
    threads.append(threading.Thread(target=teclaRight))
    threads.append(threading.Thread(target=teclaUpSeta))
    threads.append(threading.Thread(target=teclaDownSeta))
    threads.append(threading.Thread(target=teclaLeftSeta))
    threads.append(threading.Thread(target=teclaRightSeta))

    for i in threads:
        i.daemon = True
        i.start()

    janela.mainloop()

    teclado = False
