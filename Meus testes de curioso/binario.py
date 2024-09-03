sim = '100101'
talvez = '1111'
nao = '2322142'

def isBin(s):
    teste = ('0' not in s and '1' not in s) and ('0' in s or '1' in s)
    return not teste


print(f'{sim} : {isBin(sim)}')
print(f'{talvez} : {isBin(talvez)}')
print(f'{nao} : {isBin(nao)}')
