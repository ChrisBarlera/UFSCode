n,m = [int(x) for x in input().split()]

jogadores = 0
for _ in range(n):
    if '0' not in input():
        jogadores+=1

print(jogadores)