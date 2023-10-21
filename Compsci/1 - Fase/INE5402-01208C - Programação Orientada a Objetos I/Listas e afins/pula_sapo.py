p, n =  [int(x) for x in input().split()]

canos = [int(x) for x in input().split()]

# # canos = [int(input().split()[i]) for i in range(n)]
# # canos = []
# resultado = 'YOU WIN'
# # for _ in range(n):
# #     canos.append(int(input()))
# for i in range(n-1):
#     if abs(canos[i] - canos[i+1]) > p:
#         resultado = 'GAME OVER'
#         break
# print(resultado)

maior_diferenca = max(abs(canos[i] - canos[i+1]) for i in range(n-1))
resultado = 'GAME OVER' if maior_diferenca > p else 'YOU WIN'

print(resultado)