c1 = [x for x in input().split()]
c2 = [x for x in input().split()]

compativel = 'Y'
for i in range(len(c1)):
    if c1[i] == c2[i]:
        compativel = 'N'
        break

print(compativel)