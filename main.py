

from heap import *
from Tabuleiro import *

solucao = list(range(10))

entrada = gera_tabuuleiro_aleatorio()

heap = []

heap.append(Tabuleiro(entrada, 0))

while heap[0].h != 0 or len(heap) == 0 :

