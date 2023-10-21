a,d = [int(x) for x in input().split()]

while a != 0 and d != 0:
    atacantes = [int(x) for x in input().split()]
    defensores = [int(x) for x in input().split()]

    atacantes.sort()
    defensores.sort()

    impedido = 'N'
    if len(defensores) == 1:
        impedido = 'Y'
    elif atacantes[0] < defensores[0] or atacantes[0] < defensores[1]: #precisa de 2 ou mais na frente (ou mesma linha) do atacante
        impedido = 'Y'
    
    print(impedido)
    a,d = [int(x) for x in input().split()]