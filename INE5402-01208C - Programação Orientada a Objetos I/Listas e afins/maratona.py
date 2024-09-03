n,m = [int(x) for x in input().split()]

postos = [int(x) for x in input().split()]

termina = 'S'
for i in range(1,len(postos)):
    if abs(postos[i] - postos[i-1]) > m:
        termina = 'N'
        break

print(termina)