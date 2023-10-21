# completo = input()
# nomes_lista = completo.split()
# abreviado = ''

# for i in range(len(nomes_lista)):
#     if i == 0 or i == len(nomes_lista)-1 or len(nomes_lista[i]) <= 3:
#         abreviado += nomes_lista[i]+' '
#     else:
#         recorte = nomes_lista[i][:1]+'. '
#         abreviado += recorte

# print(abreviado)

partes = input().split()
for i in range(1, len(partes)-1):
    if len(partes[i] > 3):
        partes[i] = partes[i][0] + '.'
    
print(' '.join(partes))