n = int(input())
print()

maior = 0
pos = 0
for i in range(n):
    num = int(input())
    if num > maior:
        maior = num
        pos = i+1

print(maior, pos)