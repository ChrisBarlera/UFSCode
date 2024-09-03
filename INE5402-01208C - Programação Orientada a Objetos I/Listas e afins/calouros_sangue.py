# proporção de calouros que doaram sangue em relação ao total de calouros.
# qtd_calouros_doadores / n_calouros

# for _ in range(2):
    
n_calouros = int(input())
calouros = {}
for i in range(n_calouros):
    calouros[i] = input()

n_doadores = int(input())
doadores = {}
for i in range(n_doadores):
    doadores[i] = input()

qtd_calouros_doadores = 0
for i in range(n_calouros):
    if calouros[i] in doadores.values():
        qtd_calouros_doadores += 1

print(qtd_calouros_doadores/n_calouros)