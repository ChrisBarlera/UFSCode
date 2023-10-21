n,m = [int(x) for x in input().split()]

jogadores = 0
for _ in range(n):
    # gols = [int(x) for x in input().split()]
    # if 0 not in gols:
    #     jogadores+=1

    if '0' not in input():
        jogadores+=1

print(jogadores)