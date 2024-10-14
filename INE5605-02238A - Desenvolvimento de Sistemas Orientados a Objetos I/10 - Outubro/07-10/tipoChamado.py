from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        # Testando tipo de codigo
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valor inválido. O valor deve ser do tipo int")

        # Testando tipo de descricao
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            print("Valor inválido. O valor deve ser do tipo str")

        # Testando tipo de nome
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valor inválido. O valor deve ser do tipo str")

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            print("Valor inválido. O valor deve ser um str")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valor inválido. O valor deve ser um str")
