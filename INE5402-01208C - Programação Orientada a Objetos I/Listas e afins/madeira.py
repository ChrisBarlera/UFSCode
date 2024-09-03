n = int(input())
especie = 'placeholder'
input()
for _ in range(n):
    arvores = []
    especie = input()
    while especie != '':
        arvores.append(especie)
        especie = input()

    qtd_total = len(arvores)
    em_ordem = sorted(set(arvores))
    for arvore in em_ordem:
        prcnt = 100*arvores.count(arvore)/qtd_total
        print(f'{arvore} {prcnt:.4f}')