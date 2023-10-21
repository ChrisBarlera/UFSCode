n = -1
contador = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    participantes = [int(x) for x in input().split()]
    sortudo = -1
    for i in range(n):
        if participantes[i] == i+1:
            sortudo = participantes[i]
            break
    print(f'Teste {contador}')
    print(f'{sortudo}\n')
    contador += 1