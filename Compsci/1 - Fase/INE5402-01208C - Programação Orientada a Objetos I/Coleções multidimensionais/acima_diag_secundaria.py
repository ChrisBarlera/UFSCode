operacao = input()

matriz = [[0]*12 for _ in range(12)]

soma = 0
n = 0
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
        if i+j == 11:
            soma += sum(matriz[i][0:j])
            n += len(matriz[i][0:j])
        
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/n:.1f}')