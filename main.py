
from heap import *


n = int(input())
lista = []

for i in range(n):
    j = int(input())
    lista.append(j)
    #aumentar_chave(lista, i, j)

min_heapify(lista, 0)

print(lista)
