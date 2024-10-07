from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU, ABC):
    
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
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
        
        # Testando tipo de matricula
        if isinstance(matricula, int):
            self.__matricula = matricula
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

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula
        else:
            print("Valor inválido. O valor deve ser um int")

    @abstractmethod
    def emprestar(self, titulo_do_livro: str):
        pass

    def devolver(self, titulo_do_livro: str):
        print(f'''
        Aluno de matricula {self.matricula} 
        devolveu o livro: {titulo_do_livro}''')