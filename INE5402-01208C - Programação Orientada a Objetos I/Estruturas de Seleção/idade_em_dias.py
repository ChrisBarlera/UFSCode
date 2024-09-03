idade = int(input('Idade em dias: '))

anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30 

print(f'{anos} anos')
print(f'{meses} meses')
print(f'{dias} dias')
