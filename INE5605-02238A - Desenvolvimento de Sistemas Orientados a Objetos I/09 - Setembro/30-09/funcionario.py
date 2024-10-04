from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU):
    
    def __init__(self, cpf: int, departamento: str) -> None:
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