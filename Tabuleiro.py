class Tabuleiro:
    def __init__(self, vetor, passos):
        self.tabuleiro = vetor
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


