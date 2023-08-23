# 81732127
# tempo ~4s ; 8 digitos

# 6362869453
# tempo pra caralho nao computei ; 10 digitos


# 238277375078759
# 794506136775787
# tempo pra caralho nao computei ; 15 digitos

# 5123071683629671
# tempo pra caralho nao computei ; 16 digitos

# 989915795839705658693607666391
# tempo pra caralho nao computei ; 30 digitos

import time

numero = int(input('Digito um inteiro qualquer: '))
resultado = True

start = time.perf_counter()

for i in range (2, numero):
    if i % numero == 0 and i != numero:
        resultado = False

stop = time.perf_counter()

if resultado:
    print('Número é primo!')
else:
    print('Número composto!')

print(f'\nResolvido em {stop-start:0.10f} segundos')