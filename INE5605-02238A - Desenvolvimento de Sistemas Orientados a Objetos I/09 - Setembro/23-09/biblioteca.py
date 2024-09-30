from livro import Livro


class Biblioteca:

    def __init__(self):
        self.__livros = []

    @property
    def livros(self):
        return self.__livros

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            if livro not in self.__livros:
                self.__livros.append(livro)
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Livro
                """
            )

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            if livro in self.__livros:
                self.__livros.remove(livro)
            else:
                print("Erro: Livro não está registrado nesta biblioteca")
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Livro
                """
            )
