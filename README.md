# TrabalhoAED2_FilaDePrioridades (8 puzzle)
Este repositório contem os arquivos de um trabalho da disciplina de Algoritmos e Estruturas de Dados que implementa alguns jogos para a pratica do conceito de Heaps e Filas de Prioridades.

Autores:
- atos.omena@icomp.ufam.edu.br
- grecia.rivera@icomp.ufam.edu.br
- joao.souza@icomp.ufam.edu.br

## Descrição:

> O problema escolhido para estudo foi o 8-puzzle (ou Quebra-cabeça de 8 peças) que consiste num tabuleiro com peças numeradas e acomodadas de forma aleatória com uma peça faltando. Diante disso, o objetivo consiste na ordenação das peças usando o espaço vazio para deslizá-las. 
No quebra-cabeça em estudo, há um tabuleiro formado por uma matriz de ordem 3 com a numeração de 1 a 8 (com o espaço vazio representando o número zero). Além disso, o usuário poderá mover em até quatro direções a célula vazia para tentar resolver, no menor número de movimentos possível, o quebra-cabeça, ou seja, ordená-lo.

## Pensamento principal por trás do trabalho:

> O algoritmo implementado foi baseado no algoritmo de Dijkstra  que tem por finalidade calcular o caminho de custo mínimo entre dois estados. Nesse sentido, o algoritmo Dijkstra parte de uma estimativa(heurística) para o custo mínimo e gradativamente a suposição é ajustada.



## Comandos de instalações que podem ser necessárias no terminal caso o usuário não tenha pré-instalado na máquina:
pip install keyboard	

## Elaboraçao da interface

>A interface foi elaborada utilizando a biblioteca Tkinter. Através dela, foram implementados 5 botões. O primeiro no canto superior esquerdo, “Gerar aleatórios"  reformula o tabuleiro de maneira que os números estarão dispostos de forma aleatória.
O segundo botão no canto superior esquerdo,”Resolver”, soluciona dinamicamente passo a passo a matriz no tabuleiro e faz aparecer na parte inferior do display uma mensagem de processamento durante o tempo de resolução do programa . Além dele, há 4 botões dispostos de forma adjacente ao tabuleiro com setas indicando seu respectivo sentido. Visto isso, cada um desses botões tem a função de mover a célula vazia na respectiva direção da seta do botão.
Ademais, caso o usuário queira realizar um movimento invalido (mover a célula vazia para um sentido fora dos limites do tabuleiro), na parte inferior do display aparecerá o aviso de “Jogada inválida!". 
Outra decisão aderida ao planejamento de interface é a possibilidade de controle da célula pelas teclas A,W,S,D ; setas do teclado e ao clicar nos botões da interface com o cursor. 



