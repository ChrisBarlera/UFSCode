n = int(input())

for _ in range(n):
    num = int(input())
    soma = 0
    for d in range(1,num):
        if num % d == 0:
            soma += d
    
    if soma == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')