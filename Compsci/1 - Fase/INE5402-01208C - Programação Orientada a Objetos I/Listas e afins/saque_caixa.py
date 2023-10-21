n_tipos_cedulas = int(input())

# caixa = {} # cedula : quantidade

# # preenche o caixa
# for i in range(n_tipos_cedulas):
#     tipo_cedula = float(input())
#     qtd_cedulas = int(input())
#     caixa[tipo_cedula] = qtd_cedulas

tipos_cedulas = []
qtd_cedulas = []
for i in range(n_tipos_cedulas):
    tipos_cedulas.append(float(input()))
    qtd_cedulas.append(int(input()))

valor_saque = float(input())

qtd_notas_saque = []
for i in range(n_tipos_cedulas-1,-1,-1):
    qtd_a_sacar = int(valor_saque // tipos_cedulas[i])
    if qtd_cedulas[i] >= qtd_a_sacar:
        qtd_notas_saque.append(qtd_a_sacar)
        qtd_cedulas[i] -= qtd_a_sacar
        valor_saque -= tipos_cedulas[i] * qtd_a_sacar
    else:
        qtd_notas_saque.append(qtd_cedulas[i])
        valor_saque -= tipos_cedulas[i] * qtd_cedulas[i]
        qtd_cedulas[i] = 0

qtd_notas_saque.reverse()
for qtd in qtd_notas_saque:
    print(qtd, end=' ')