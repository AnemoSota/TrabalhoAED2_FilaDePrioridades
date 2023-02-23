from tkinter import *
from tkinter import ttk
from heap import *
from Tabuleiro import *



janela= Tk()


janela.title("Quebra-cabeças de 8 peças")
janela.minsize(width=800, height=800)
janela.maxsize(width=800, height=800)



font1=('Times',22,'normal')
a=" "
b=1
c=2
d=3
e=4
f=5
g=6
h=7
i=8
l1=[a,b,c,d,e,f,g,h,i]
linha,coluna=0,0
labels=[]
indiceX=0.5
indiceY=0.5
for data in l1:
    label=ttk.Label(janela,text=data,font=font1, foreground= "red", background="white")
    
    label.grid(row=linha,column=coluna,padx=50,pady=50)
    coluna=coluna+1
  
    label.place(relx = indiceX,rely = indiceY,anchor = 'center',x=-80,y=-80)
    indiceX+=0.1
    if coluna>=3:
        indiceY+=0.1
        linha+=1
        coluna=0
        indiceX=0.5


geraAleatoriosBotao= Button(janela, text="Gerar aleatorios",command= gerar_tabuleiro_aleatorio)
geraAleatoriosBotao.place(x=10,y=10)

geraAleatoriosBotao.configure(height = 10,
                             width = 20)

Resolver= Button(janela, text="Resolver", command= gerar_tabuleiro_aleatorio)
Resolver.place(x=640,y=10)
Resolver.configure(height = 10,width = 20)


global laabel
laabel=ttk.Label(janela, text="aaa", font=('Aerial 18'))
laabel.place(relx = indiceX,rely = indiceY,anchor = 'center',x=-60,y=85)



Cima= Button(janela, text="↑", command= gerar_tabuleiro_aleatorio)
Cima.place(x=360,y=100)
Cima.configure(height = 5,width = 10)

Esquerda= Button(janela, text="←", command= gerar_tabuleiro_aleatorio)
Esquerda.place(x=100,y=360)
Esquerda.configure(height = 5,width = 10)

Direita= Button(janela, text="→", command= gerar_tabuleiro_aleatorio)
Direita.place(x=600,y=360)
Direita.configure(height = 5,width = 10)

Baixo= Button(janela, text=" ↓", command= gerar_tabuleiro_aleatorio)
Baixo.place(x=360,y=600)
Baixo.configure(height = 5,width = 10)



janela.mainloop()