from pessoa import Pessoa

uma_pessoa = Pessoa("João")

#V1
# print(uma_pessoa.get_nome())
#
# uma_pessoa.set_nome("Christian")
#
# print(uma_pessoa.get_nome())
#
# uma_pessoa.set_nome(1)

#V2
print(uma_pessoa.nome)
uma_pessoa.nome = "Christian"
print(uma_pessoa.nome)

# uma_pessoa.nome = 1
# print(uma_pessoa.nome)


