
#########################
#   FUNÇÕES PARA HEAP   #
#########################

def min_heapify (lista, raiz):
    index_menor = raiz
    tamanho_lista = len(lista)
    filho_esquerdo = 2*raiz+1

    if filho_esquerdo < tamanho_lista and lista[filho_esquerdo] < lista[index_menor]:
        index_menor = filho_esquerdo

    filho_direito = 2*raiz+2

    if filho_direito < tamanho_lista and lista[filho_direito] < lista[index_menor]:
        index_menor = filho_direito
    
    if index_menor != raiz:
        troca(lista, index_menor, raiz)
        min_heapify(lista, index_menor)

#Aumenta o valor de uma chave na heap, mantendo a propriedade de heap preservada
def aumentar_chave(heap, index, novo_valor):
	#caso a chave seja aumentada ao final da lista
	if index == len(heap):
		heap.append(novo_valor)
	else :
		heap[index] = novo_valor
		min_heapify(heap, index)
	verifica_pai(heap, index)

#Verifica se os pais estao respeitando as propriedades da heap
def verifica_pai(heap, index_filho):
	index_pai = int((index_filho-1)/2)
	
	if index_pai < 0 :
		return
	elif heap[index_pai] > heap[index_filho] :
		troca(heap, index_pai, index_filho)
		verifica_pai(heap, index_pai)

#Remove um elemento de uma heap respeitando a propriedade de heap
def remove(heap, index):
	troca(heap, index, len(heap)-1)
	removido = heap.pop()
	min_heapify(heap, index)
	return removido

#Troca 2 elementos de uma lista
def troca(lista, p1, p2) :
	aux = lista[p1]
	lista[p1] = lista[p2]
	lista[p2] = aux

def naoExisteEm(estado, lista):
	naoExiste = 1
	
	for i in lista:
		naoExiste -= (i.tabuleiro == estado)
	
	return naoExiste