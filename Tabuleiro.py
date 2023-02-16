

from heap import troca
from random import shuffle

class Tabuleiro:
    def __init__(self, vetor, passos):
        self.tabuleiro = vetor
        self.zero = busca_zero(vetor)
        self.g = passos
        self.h = calcular_heuristica(self.tabuleiro)
        self.f = self.g + self.h    # f(x) = g(x) + h(x)

    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        return False
    
    def __str__(self):
        return str(self.tabuleiro)


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


# faz a contagem das inversoes ha ser feitas no tabuleiro 
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

def trocas(vetor, i):
    possiveis = []

    if trocavel(i, i-1):
        novo = vetor
        troca(novo , i , i-1)
        possiveis.append(novo)

    if trocavel(i, i+1):
        novo = vetor
        troca(novo , i , i+1)
        possiveis.append(novo)

    if trocavel(i, i-3):
        novo = vetor
        troca(novo , i , i-3)
        possiveis.append(novo)

    if trocavel(i, i+3):
        novo = vetor
        troca(novo , i , i+3)
        possiveis.append(novo)

    return possiveis
