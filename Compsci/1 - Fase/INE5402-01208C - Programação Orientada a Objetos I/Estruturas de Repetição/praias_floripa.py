n = int(input())

mais_distante = ''
maior_distancia = 0
cont = 0
soma = 0
for _ in range(n):
    praia, distancia = input().split(';')
    distancia = float(distancia)
    if distancia > maior_distancia:
        mais_distante = praia
        maior_distancia = distancia
    
    if distancia >= 15 and distancia <= 20:
        cont +=1
    
    soma += distancia

print(f'{mais_distante};{cont};{soma/n:.1f}')