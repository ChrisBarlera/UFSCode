# No jogo de xadrez numa jogada a dama pode mover-se qualquer quantidade de casas
# na mesma linha, na mesma coluna, ou numa das duas diagonais.
# Estas casas alcançáveis com um único movimento dizem ser dominadas pela dama.

# No tabuleiro, as colunas são numeradas da esquerda para a direita de 1 a 8 e as linhas de baixo para cima também de 1 a 8.
# As coordenadas de uma casa na linha X e coluna Y são (X, Y).
# Dadas, então, as coordenadas (x1, y1) da casa onde a dama está e as coordenadas (x2, y2) de um segunda casa,
# queremos saber se esta segunda casa está dominada pela dama.

# Entrada:
# Uma linha contendo o par (x1, y1) correspondente às coordenadas onde a dama está e outra linha com o par (x2, y2) correspondente às coordenadas da segunda casa.

#     5 5

#     8 2

# Saída:
# True  se a casa está dominada pela dama; False em caso contrário.

#     True
# melhor como uma única expressão lógica
# for desnecessário

x1, y1 = [int(w) for w in input().split()]
x2, y2 = [int(w) for w in input().split()]

teste = False
if x2 == x1 or y2 == y1:
    teste = True
else:
    for i in range(1,9):
        if (x2 == x1 - i or x2 == x1+i) and (y2 == y1 - i or y2 == y1+i):
            teste = True
            break

print(teste)