# 81732127
# 6362869453
# 238277375078759
# 794506136775787
# tempo < 2s ; 15 digitos

# 5123071683629671
# tempo 3~4s ; 16 digitos

# 989915795839705658693607666391
# tempo pra caralho nao computei ; 30 digitos

import time

numero = int(input('Digito um inteiro qualquer: '))
resultado = True

start = time.perf_counter()

if numero > 3:
    if numero % 2 == 0 or numero % 3 == 0:
        resultado = False
    else:
        contador = 5
        while contador <= numero**(1/2)+1:
            if numero % contador == 0  or numero % (contador+2) == 0:
                resultado = False
                break
            contador += 6


stop = time.perf_counter()

if resultado:
    print('Número é primo!')
else:
    print('Número composto!')

print(f'\nResolvido em {stop-start:0.10f} segundos')