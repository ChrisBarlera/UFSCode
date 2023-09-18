n = int(input())

melhor_salto = 0
saltador = ''
for _ in range(n):
    a,b,c, nome = [w for w in input().split()]
    melhorzinho = max([float(a), float(b), float(c)])

    if melhorzinho > melhor_salto:
        melhor_salto = melhorzinho
        saltador = nome

print(saltador)