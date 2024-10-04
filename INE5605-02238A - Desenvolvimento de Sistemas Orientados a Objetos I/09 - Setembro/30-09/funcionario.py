from usuario_bu import UsuarioBU
from abc import ABC, abstractmethod


class Funcionario(UsuarioBU, ABC):
    
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int) -> None:
        # Testando tipo de cpf
        if isinstance(cpf, int):
            # self.__cpf = cpf
            pass
        else:
            print("Valor inválido. O valor deve ser um int")

        # Testando tipo de departamento
        if isinstance(departamento, str):
            self.__departamento = departamento
        else:
            print("Valor inválido. O valor deve ser um str")
    
    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: str):
        if isinstance(departamento, str):
            self.__departamento = departamento
        else:
            print("Valor inválido. O valor deve ser um str")