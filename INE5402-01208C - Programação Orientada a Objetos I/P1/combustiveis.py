# Ao longo do dia as vendas dos diversos produtos de num posto de combustíveis vão sendo anotadas. 
# Ao final do dia o gerente do posto quer saber qual a quantidade vendida de cada combustível (outros produtos devem ser ignorados)
# e o valor total recebido com a venda de combustíveis.
# Escreva um programa que leia os dados e compute estes valores. Os combustíveis vendidos no posto
# e correspondentes códigos e preço por litro são dados pela tabela abaixo: 

# Combustível	Código	Preço por litro
# Álcool	1	4,50
# Gasolina	2	5,13
# Diesel	3	4,89

# Entrada:
# Na primeira contém um número inteiro correspondente à quantidade de vendas do dia. Em seguida estão os dados de
# cada venda no formato c:q, uma em cada linha, onde c é código do produto e q a quantidade de unidades vendidos
# (litros no caso de combustíveis), a exemplo de:

# 5
# 1:30
# 2:50
# 7:3
# 1:45
# 3:70

# Saída:
# Imprima a saída conforme abaixo:

# Álcool: 75 litros
# Gasolina: 50 litros
# Diesel: 70 litros
# Total das vendas: R$ 936.30

# Observações:

# Não utilizar estrutura de controle "while".
# Você pode utilizar o método split para separar os número de cada linha de entrada, como em "x.split(':'), onde x denota um string"

n = int(input())

total_alcool = 0
total_gasolina = 0
total_diesel = 0

for _ in range(n):
    codigo, litros = [int(w) for w in input().split(':')]
    
    if codigo == 1:
        total_alcool += litros
    elif codigo == 2:
        total_gasolina += litros
    elif codigo == 3:
        total_diesel += litros

print(f'Álcool: {total_alcool} litros')
print(f'Gasolina: {total_gasolina} litros')
print(f'Diesel: {total_diesel} litros')
print(f'Total das vendas: R$ {total_alcool*4.5 + total_gasolina*5.13 + total_diesel*4.89:.2f}')
