notas = [float(x) for x in input().split()]

notas.sort()

nota_final = 0
for i in range(1,4):
    nota_final += notas[i]

print(f'{nota_final:1f}')