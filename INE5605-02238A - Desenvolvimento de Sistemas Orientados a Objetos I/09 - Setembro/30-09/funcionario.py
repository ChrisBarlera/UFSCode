from usuario_bu import UsuarioBU
from abc import ABC, abstractmethod
from abc import ABC, abstractmethod


class Funcionario(UsuarioBU, ABC):
class Funcionario(UsuarioBU, ABC):
    
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf=cpf, dias_de_emprestimo=dias_de_emprestimo)

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