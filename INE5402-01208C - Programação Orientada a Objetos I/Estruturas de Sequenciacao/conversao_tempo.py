tempo = int(input('Tempo total em segundos: '))

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print(f'{horas}:{minutos}:{segundos}')