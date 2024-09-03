contador = 1
while True:
    num_aeroportos, num_voos = [int(x) for x in input().split()]
    if num_aeroportos == 0 and num_voos == 0:
        break

    qtd_voos = [0]*(num_aeroportos+1)

    for _ in range(num_voos):
        origem, destino = [int(x) for x in input().split()]
        qtd_voos[origem] += 1
        qtd_voos[destino] += 1

    maior_qtd_voos = max(qtd_voos)

    print(f'Teste {contador}')
    for id_aeroporto in range(1,len(qtd_voos)):
        if qtd_voos[id_aeroporto] == maior_qtd_voos:
            print(id_aeroporto, end=' ')
    print()
    contador += 1