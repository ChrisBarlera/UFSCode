linha = int(input())
operacao = input()

matriz = [[0]*12 for _ in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
    if i == linha:
        soma = sum(matriz[i])
        break

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')