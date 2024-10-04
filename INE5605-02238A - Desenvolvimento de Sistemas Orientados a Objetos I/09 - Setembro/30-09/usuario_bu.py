class UsuarioBU:

    def __init__(self, cpf: int, dias_de_emprestimo: int):
         # Testando tipo de cpf
        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            print("Valor inválido. O valor deve ser um int")

         # Testando tipo de dias_de_emprestimo
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo

    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo: int):
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
        else:
            print("Valor inválido. O valor deve ser um int")

    def emprestar(self, titulo_livro: str) -> None:
        pass

    def devovler(self, titulo_livro: str) -> None:
        pass