def fatorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n*fatorial_recursivo(n-1)

def fatorial(n):
    fat = 1
    for i in range(2, n+1):
        fat *= i
    return fat

n = int(input())    
print(fatorial_recursivo(n))
print(fatorial(n))