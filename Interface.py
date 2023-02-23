from tkinter import *
from tkinter import ttk
from heap import *
from Tabuleiro import *



janela= Tk()

#frame = ttk.Frame(master=janela, width=800, height=800,)
#frame.pack()

janela.title("Q-uebra-caebças de 8 peças")
janela.minsize(width=800, height=800)
janela.maxsize(width=800, height=800)



    
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(linhas):
            for j in range(colunas):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [(0,1,2),(3,4,5),(6,7,8),]
  
# find total number of rows and
# columns in list
linhas = len(lst)
colunas = len(lst[0])
  
# create root window

t = Table(janela)
#t.place(x=80,y=100)
#root.mainloop()
#t.grid(row=0, column=1, sticky=ttk.N)


geraAleatoriosBotao= Button(janela, text="Gerar aleatorios")
geraAleatoriosBotao.place(x=10,y=10)

geraAleatoriosBotao.configure(height = 10,
                             width = 20)

Resolver= Button(janela, text="Resolver", command= gerar_tabuleiro_aleatorio)
Resolver.place(x=640,y=10)
Resolver.configure(height = 10,width = 20)






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

#Tabuleiro= Button(janela, text="", command= gerar_tabuleiro_aleatorio)
#Tabuleiro.place(x=360,y=600)
#Tabuleiro.configure(height = 5,width = 10)




janela.mainloop()