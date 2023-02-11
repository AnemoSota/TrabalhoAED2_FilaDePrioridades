
#########################
#   FUNÇÕES PARA HEAP   #
#########################

def min_heapfy(lista, i):
	
	tam = len(lista)
	
	f1 = (2*i) + 1
	f2 = (2*i) + 2
	
	exf1 = False
	exf2 = False
	
	if (f1 < tam) :
		exf1 = (lista[i] > lista[f1])
	
	if (f2 < tam) :
		exf2 = (lista[i] > lista[f2])
	
	if (exf1 and exf2) :
		if (lista[f1] <= lista[f2]) :
			troca(lista, f1, i)
			min_heapfy(lista, f1)
		else :
			troca(lista, f2, i)
			min_heapfy(lista, f2)
	elif exf1 :
		troca(lista, f1, i)
		min_heapfy(lista, f1)
	elif exf2 :
		troca(lista, f2, i)
		min_heapfy(lista, f2)

def aumentar_chave(heap, pos, novo):
	if pos == len(heap):
		heap.append(novo)
	else :
		heap[pos] = novo
		min_heapfy(heap, pos)
	verifica_pai(heap, pos)

def verifica_pai(lista, i):
	pai = int((i-1)/2)
	
	if pai < 0 :
		return
	elif lista[pai] > lista[i] :
		troca(lista, pai, i)
		verifica_pai(lista, pai)

def remove(heap, pos):
	troca(heap, pos, len(heap)-1)
	heap.pop()
	min_heapfy(heap, pos)

def troca(lista, p1, p2) :
	aux = lista[p1]
	lista[p1] = lista[p2]
	lista[p2] = aux

