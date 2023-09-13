# n = int(input('N:'))
# m = int(input('Fim de [1,m]: '))

n = int(input())
m = int(input())


for i in range(1,m+1):
    if i % n == 0:
        print(i,end=' ')