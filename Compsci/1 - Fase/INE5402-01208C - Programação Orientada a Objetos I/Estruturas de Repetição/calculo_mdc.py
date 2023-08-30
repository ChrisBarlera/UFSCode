a = int(input('Número inteiro a: '))
b = int(input('Número inteiro b: '))

resto = 1
mdc = 1

while True:
    quociente = a // b
    resto = a % b
    if resto == 0:
        break
    else:
        mdc = resto
        a = b
        b = resto

print(f'MDC dos números é: {mdc}')