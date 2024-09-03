cartas = [int(x) for x in input().split()]
crescente = cartas.copy()
decrescente = cartas.copy()

crescente.sort()
decrescente.sort(reverse = True)

if cartas == crescente:
    print('C')
elif cartas == decrescente:
    print('D')
else: 
    print('N')