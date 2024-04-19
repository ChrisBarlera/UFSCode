# https://www.beecrowd.com.br/repository/UOJ_2434.html

dias, saldo = [int(w) for w in input().split()]
menor = saldo
for _ in range(dias):
    movimentacao = int(input())
    if saldo + movimentacao < menor:
        menor = saldo + movimentacao
    saldo += movimentacao
print(menor)