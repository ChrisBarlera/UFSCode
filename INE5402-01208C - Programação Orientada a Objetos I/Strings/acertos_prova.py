gabarito = input()
respostas = input()

certas = 0
for i in range(len(respostas)):
    if respostas[i] == gabarito[i]:
        certas += 1

print(certas)