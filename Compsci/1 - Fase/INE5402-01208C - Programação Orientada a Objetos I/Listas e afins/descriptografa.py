normal = list(input().lower())
cifragem = list(input().lower())

relacao = dict(zip(cifragem, normal))

frase = input().lower()

descriptografada = ''
for letra in frase:
    if letra in relacao.keys():
        descriptografada += relacao[letra]
    else:
        descriptografada += letra

print(descriptografada) 