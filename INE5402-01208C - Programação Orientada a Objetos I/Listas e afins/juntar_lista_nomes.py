# n1 = int(input())
# lista1_nomes = [input() for _ in range(n1)]

# n2 = int(input())
# lista2_nomes = [input() for _ in range(n2)]
lista_final = []

# for nome in lista1_nomes:
#     lista_final.append(nome)

# for nome in lista2_nomes:
#     lista_final.append(nome)

for _ in range(2):
    n = int(input())
    for i in range(n):
        lista_final.append(input())

lista_final.sort()

for nome in lista_final:
    print(nome)