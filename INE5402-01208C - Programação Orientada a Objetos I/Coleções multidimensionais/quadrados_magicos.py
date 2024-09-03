n = int(input())

matriz = []

# Criando matriz
for i in range(n):
    matriz.append([int(x) for x in input.split()])

magico = True
num_magico = sum(matriz[0])

for i in range(n):
    for j in range(n):
        pass
for i in range(n):
    if sum(matriz[i]) != num_magico:
        magico = False
        break
else:
    pass