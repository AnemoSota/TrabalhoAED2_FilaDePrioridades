

from heap import *
from Tabuleiro import *

solucao = list(range(10))

#entrada = gerar_tabuleiro_aleatorio()
entrada = [1,0,2,3,4,5,6,7,8,9]

print(entrada)

heap = []
historico = []

heap.append(Tabuleiro(entrada, 0))

while heap[0].h != 0 or len(heap) == 0 :
    passos = heap[0].g

    historico.append(heap[0])
    
    novos = trocas(heap[0].tabuleiro, heap[0].zero)
    remove(heap, 0)
    for i in novos :
        if naoExisteEm(i, historico) and naoExisteEm(i, heap):
            aumentar_chave(heap,len(heap),Tabuleiro(i , passos + 1))
    
print(heap[0])