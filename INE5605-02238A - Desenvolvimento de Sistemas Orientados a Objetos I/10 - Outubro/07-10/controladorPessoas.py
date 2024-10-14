from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        novo_cliente = Cliente(nome, codigo)
        if len(self.__clientes) != 0:
            for cliente in self.__clientes:
                if cliente.codigo != codigo:
                    self.__clientes.append(novo_cliente)
                    return novo_cliente
        else:
            self.__clientes.append(novo_cliente)
        return novo_cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        if len(self.__tecnicos) != 0:
            for tecnico in self.__tecnicos:
                if tecnico.codigo != codigo:
                    novo_tecnico = Tecnico(nome, codigo)
                    self.__tecnicos.append(novo_tecnico)
                    return novo_tecnico
        else:
            novo_tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(novo_tecnico)
            return novo_tecnico
