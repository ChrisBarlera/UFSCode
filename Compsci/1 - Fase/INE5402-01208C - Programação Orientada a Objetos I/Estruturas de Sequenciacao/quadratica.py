import math

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

delta = b**2-4*a*c

x1 = (-b+math.sqrt(delta))/2*a
x2 = (-b-math.sqrt(delta))/2*a

print(f'As raízes são: {x1} ; {x2}')