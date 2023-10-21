n,m = [int(x) for x in input().split()]

# carros = []
# for i in range(n):
#     carros.append(sum([int(x) for x in input().split()]))

# tempos = carros.copy()
# tempos.sort()

# for i in range(3):
#     print(carros.index(tempos[i])+1)

carros = {}

for i in range(n):
    carros[sum([int(x) for x in input().split()])] = i+1

classificacao = sorted(carros.keys())
for i in range(3):
    print(carros[classificacao[i]])