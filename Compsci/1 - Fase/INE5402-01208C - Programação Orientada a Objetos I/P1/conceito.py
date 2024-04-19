# https://www.beecrowd.com.br/repository/UOJ_2535.html
# expressão lógica complexa (duplo teste desnecessário)
# ausência de else

nota = int(input())
conceito = 'E'

if nota >= 1 and nota <= 35:
    conceito = 'D'
elif nota >= 36 and nota <= 60:
    conceito = 'C'
elif nota >= 61 and nota <= 85:
    conceito = 'B'
elif nota >= 86 and nota <= 100:
    conceito = 'A'

print(conceito)