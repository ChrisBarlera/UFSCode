from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        # Testando tipo de nome
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valor inválido. O valor deve ser do tipo str")

        # Testando tipo de codigo
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valor inválido. O valor deve ser do tipo int")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print("Valor inválido. O valor deve ser um str")

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valor inválido. O valor deve ser um int")