def fibonacci_recursivo(n):
    if n <= 2:  
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci(n):
    proximo = 0
    atual = 1
    anterior = 0
    for _ in range(n):
        # print(atual)
        proximo = atual + anterior
        anterior = atual
        atual = proximo
    return anterior

n = int(input())
print()
# print(fibonacci(n))
print(fibonacci_recursivo(n))