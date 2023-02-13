import heap
from random import shuffle

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

