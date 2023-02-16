def calcular_heuristica(tabuleiro):
    h = 0
    #percorre o tabuleiro e verifica quais pecas estao fora do lugar
    for i in range(0, len(tabuleiro)):
        if i != tabuleiro[i]:
            h += 1
    
    return h
