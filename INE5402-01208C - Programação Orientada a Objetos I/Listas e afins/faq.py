n, k = [int(x) for x in input().split()]
while n != 0 and k != 0:
    perguntas = [int(x) for x in input().split()]
    distintas = set(perguntas)

    cont = 0
    for pergunta in distintas:
        freq_perg = perguntas.count(pergunta)
        if freq_perg >= k:
            cont+=1
    
    print(cont)
    n, k = [int(x) for x in input().split()]