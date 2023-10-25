def gerar_nova_fila(anterior):
    nova = []
    for i in range(1,len(anterior)):
        if anterior[i] + anterior[i-1] == 0:
            nova.append(-1)
        else:
            nova.append(1)
    return nova


n = int(input())
primeira_fila = [int(x) for x in input().split()]

aux_fila = gerar_nova_fila(primeira_fila)
for i in range(1,n-1):
    aux_fila = gerar_nova_fila(aux_fila)

if aux_fila[0] == -1:
    print('branca')
else:
    print('preta')