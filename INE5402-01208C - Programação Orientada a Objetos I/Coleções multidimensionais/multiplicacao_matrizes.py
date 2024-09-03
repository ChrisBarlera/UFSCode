def multiplica_matrizes(a, b):
    # matrizes, a(m,n) . b(n,p) = c(m,p)
    m = len(a)
    n = len(b)
    p = len(b[0])

    c = []
    for linha in range(m):
        c.append([0]*p)
        for i in range(p):
            soma = 0
            for j in range(n):
                soma += a[linha][j] * b[j][i]
            c[linha][i] = soma
    return c

ordem = int(input())

#parametros
p,q,r,s,x,y = [int(x) for x in input().split()]

matrizA = []
for _ in range(ordem):
    matrizA.append([1]*ordem)

matrizB = []
for _ in range(ordem):
    matrizB.append([1]*ordem)

for i in range(ordem):
    for j in range(ordem):
        # +1 nos indices na hora de fazer operacao pois devemos contar de forma matematica e nao pythoniana
        matrizA[i][j] = (p*(i+1) + q*(j+1))%x
        matrizB[i][j] = (r*(i+1) + s*(j+1))%y

matrizC = multiplica_matrizes(matrizA,matrizB)

pos = [int(x)-1 for x in input().split()]

print(matrizC[pos[0]][pos[1]])