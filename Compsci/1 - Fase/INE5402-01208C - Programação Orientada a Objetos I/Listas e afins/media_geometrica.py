n = int(input())

produtorio = 1
for _ in range(n):
    valor = float(input())
    produtorio *= valor

print(produtorio**(1/n))