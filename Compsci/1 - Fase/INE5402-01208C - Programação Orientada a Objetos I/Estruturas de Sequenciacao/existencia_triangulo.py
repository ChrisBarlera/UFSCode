import math

a = abs(float(input('Valor do lado a: ')))
b = abs(float(input('Valor do lado b: ')))
c = abs(float(input('Valor do lado c: ')))

print(a+b>c and b+c>a and a+c > b)