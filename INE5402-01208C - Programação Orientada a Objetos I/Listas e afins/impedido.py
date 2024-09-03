a,d = [int(x) for x in input().split()]

while a != 0 and d != 0:
    atacantes = [int(x) for x in input().split()]
    defensores = [int(x) for x in input().split()]

    # # Minha opção
    # neymar = min(atacantes)
    # defensores.sort()

    # impedido = 'Y'
    # if len(defensores) != 1:
    #     if defensores[1] > neymar:
    #         impedido = 'N'
    # # if len(defensores) == 1:
    # #     impedido = 'Y'
    # # elif atacantes[0] < defensores[0] or atacantes[0] < defensores[1]: #precisa de 2 ou mais na frente (ou mesma linha) do atacante
    # #     impedido = 'Y'
    
    # # Opção prof
    menor_distancia = min(atacantes)
    defensores = [dist_def for dist_def in defensores if dist_def <= menor_distancia]
    impedido = 'Y' if len(defensores) < 2 else 'N'
    print(impedido)
    a,d = [int(x) for x in input().split()]