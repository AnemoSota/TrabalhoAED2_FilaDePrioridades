

import time
from heap import *
from Tabuleiro import *

solucao = list(range(10))

#entrada = gerar_tabuleiro_aleatorio()
entrada = [1,0,2,3,4,5,6,7,8,9]

saida = resolve(entrada)

if saida != False:
        for i in saida:
            imprimeTabuleiro(i)

def fds():
    print(entrada)

    heap = []
    historico = []

    heap.append(Tabuleiro(entrada, 0, []))

    while heap[0].h != 0 or len(heap) == 0 :
        topo = remove(heap, 0)
        historico.append(topo)

        topo.sequencia.append(topo.tabuleiro)

        novos = trocas(topo.tabuleiro, topo.zero)
        
        for i in novos :
            if naoExisteEm(i, historico) and naoExisteEm(i, heap):
                aumentar_chave(heap,len(heap),Tabuleiro(i , topo.g + 1, topo.sequencia))

    if(len(heap) == 0):
        print("sem solucao")
    else:
        for i in heap[0].sequencia :
            imprimeTabuleiro(i)
        
    print(heap[0])