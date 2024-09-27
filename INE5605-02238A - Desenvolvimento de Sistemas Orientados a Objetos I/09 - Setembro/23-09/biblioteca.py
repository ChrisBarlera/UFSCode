from livro import Livro

class Biblioteca:

    def __init__(self):
        pass

    # @property
    # def nome(self):
    #     return self.__nome

    # @nome.setter
    # def nome(self, nome: str):
    #     self.__nome = nome

    def incluir_livro(livro: Livro):
        if isinstance(livro, Livro):
            pass
        else:
            raise ValueError("Argumento inválido. O argumento deve ser um objeto da classe Livro")


    def excluir_livro(livro: Livro):
        if isinstance(livro, Livro):
            pass
        else:
            raise ValueError("Argumento inválido. O argumento deve ser um objeto da classe Livro")

