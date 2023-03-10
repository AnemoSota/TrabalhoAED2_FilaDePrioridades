#########################################################
#   Funções para manipulação e resolução do tabuleiro   #
#########################################################

import Heap
from random import shuffle

class Tabuleiro:
    def __init__(self, vetor, passos, historico):
        self.tabuleiro = vetor
        self.zero = busca_zero(vetor)
        self.sequencia = [] + historico
        self.g = passos
        self.h = calcular_heuristica(self.tabuleiro)
        self.f = self.g + self.h    # f(x) = g(x) + h(x)
        # f(x) é o "custo" total para resolucao apartir do estado X
        # g(x) é a somatoria dos custos anteriores
        # h(x) é a estimativa de custo para a resolução


    # Funcao usada para comparação entre objetos Tabuleiros 
    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        return False
       
# calcula uma estimativa de passos que sao necessarios para resolver o tabuleiro   
def calcular_heuristica(tabuleiro):
    h = 0
    #percorre o tabuleiro e verifica quais pecas estao fora do lugar
    for i in range(0, len(tabuleiro)):
        if i != tabuleiro[i]:
            h += 1
    
    return h

# Gera um tabuleiro aleatorio que exista resolucao
def gerar_tabuleiro_aleatorio():
    tabuleiro = [0,1,2,3,4,5,6,7,8]
    shuffle(tabuleiro)
    while existe_resolucao(tabuleiro) == False:
        shuffle(tabuleiro)
    return tabuleiro


# verifica se o tabuleiro possui solucao
def existe_resolucao(tabuleiro):
    inversoes = contar_inversoes(tabuleiro)

    # retorna true se houver solucao e false se nao
    if inversoes%2 == 0:
        return True
    else:
        return False


# faz a contagem das inversoes ha serem feitas no tabuleiro 
# Se os elementos posteriores ao atual analisado forem menores, isso configura uma inversao 
def contar_inversoes(tabuleiro):
    i = 0
    j = i + 1
    inversoes = 0
    while i <= 8 :
        
        if j <= 8: #garante o range do vetor
            if tabuleiro[j] != 0 and tabuleiro[i] != 0:
                if tabuleiro[j] < tabuleiro[i]: 
                    inversoes += 1
                    j += 1
                else:
                    j += 1
            else:
                if  tabuleiro[j] == 0:
                    j += 1
                if tabuleiro[i] == 0:
                    i += 1
        else:
            i += 1
            j = i + 1

    return inversoes

# Faz a busca pelo elemento zero presente no vetor e retorna o indice nesse vetor
def busca_zero(lista):
    i = 0
    while (i < len(lista)) and (lista[i] != 0):
        i += 1
    return i


# Verifica se as posicoes podem ser trocadas
def trocavel(i, j):
    t = True

    if (i - j == 1) and (i % 3 == 0) :
        t = False
    if (i - j == -1) and (i % 3 == 2):
        t = False
    if (i - j == 3) and (i < 3):
        t = False
    if (i - j == -3) and (i > 5):
        t = False

    return t

# Calcula todas as possiveis trocas que possam ser realizadas(nas 4 direcoes) e retorna um vetor com todas elas
def trocas(vetor, i):
    possiveis = []

    novo = []
    if trocavel(i, i-1):
        novo += vetor
        Heap.troca(novo , i , i-1)
        possiveis.append(novo)

    novo = []
    if trocavel(i, i+1):
        novo += vetor
        Heap.troca(novo , i , i+1)
        possiveis.append(novo)

    novo = []
    if trocavel(i, i-3):
        novo += vetor
        Heap.troca(novo , i , i-3)
        possiveis.append(novo)

    novo = []
    if trocavel(i, i+3):
        novo += vetor
        Heap.troca(novo , i , i+3)
        possiveis.append(novo)

    return possiveis

# Busca a solucao para o tabuleiro com o menor custo
# Caso nao haja solucao, retorna False
# Caso haja solucao, retorna o objeto da solucao com historico do passo a passo
def resolve(entrada):

    heap = []
    historico = []

    heap.append(Tabuleiro(entrada, 0, []))

    while heap[0].h != 0 or len(heap) == 0 :
        topo = Heap.remove(heap, 0)
        historico.append(topo)

        topo.sequencia.append(topo.tabuleiro)

        novos = trocas(topo.tabuleiro, topo.zero)
        
        for i in novos :
            if Heap.naoExisteEm(i, historico) and Heap.naoExisteEm(i, heap):
                Heap.aumentar_chave(heap,len(heap),Tabuleiro(i , topo.g + 1, topo.sequencia))

    if(len(heap) == 0):

        return False
    else:
        heap[0].sequencia.append(heap[0].tabuleiro)
        return heap[0].sequencia
