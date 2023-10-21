testes = 0
n = int(input())
while testes <= 30 and n != 0:
    instantes = [int(x) for x in input().split()]
    segundos = 10
    for i in range(1,n):
        diferenca = instantes[i] - instantes[i-1]
        if diferenca >= 10:
            segundos += 10
        else:
            segundos += diferenca
    
    print(segundos)
    n = int(input())
    testes += 1