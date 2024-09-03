a = int(input('Número inteiro a: '))
b = int(input('Número inteiro b: '))



resto = 1
while resto != 0:
    resto = a % b
    a = b
    b = resto

# mdc = 1
# contador = 0
# while True:
#     contador += 1
#     quociente = a // b
#     resto = a % b
#     if resto == 0:
#         if contador == 1:
#             mdc = b
#             break
#         else:
#             break
#     else:
#         mdc = resto
#         a = b
#         b = resto

print(f'MDC dos números é: {a}')