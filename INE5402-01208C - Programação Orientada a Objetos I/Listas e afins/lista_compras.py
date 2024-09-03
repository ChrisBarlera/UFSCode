n = int(input())

for _ in range(n):
    compras = set(input().lower().split())
    compras = sorted(list(compras))
    print(compras)