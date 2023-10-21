inicio = int(input('inicio: '))
fim = int(input('fim: '))

div1 = int(input('div1: '))
div2 = int(input('div2: '))
div3 = int(input('div3: '))

a1 = []
a2 = []
a3 = []

contador = 0
for i in range(inicio, fim+1):
    if i % div1 == 0 and i % div2 != 0 and i % div3 != 0:
        contador += 1
    if i % div2 == 0 and i % div1 != 0 and i % div3 != 0:
        contador += 1
    if i % div3 == 0 and i % div2 != 0 and i % div1 != 0:
        contador += 1
    
    
print(contador)