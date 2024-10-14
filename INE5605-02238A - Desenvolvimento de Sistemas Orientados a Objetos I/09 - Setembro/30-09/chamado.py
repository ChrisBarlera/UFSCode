from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):

        # Testando tipo de data
        if isinstance(data, Date):
            self.__data = data
        else:
            print("Valor inválido. O valor deve ser do tipo Date")

        # Testando tipo de cliente
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            print("Valor inválido. O valor deve ser do tipo Cliente")

        # Testando tipo de tecnico
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
        else:
            print("Valor inválido. O valor deve ser do tipo Tecnico")

        # Testando tipo de titulo
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor inválido. O valor deve ser do tipo str")

        # Testando tipo de descricao
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            print("Valor inválido. O valor deve ser do tipo str")

        # Testando tipo de prioridade
        if isinstance(prioridade, int):
            self.__prioridade = prioridade
        else:
            print("Valor inválido. O valor deve ser do tipo int")

        # Testando tipo de tipo
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo
        else:
            print("Valor inválido. O valor deve ser do tipo TipoChamado")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data
        else:
            print("Valor inválido. O valor deve ser um Date")

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            print("Valor inválido. O valor deve ser um Cliente")

    @property
    def tecnico(self):
        return self.__tecnico

    @tecnico.setter
    def tecnico(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
        else:
            print("Valor inválido. O valor deve ser um Tecnico")

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor inválido. O valor deve ser um str")

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
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        if isinstance(prioridade, int):
            self.__prioridade = prioridade
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoChamado):
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo
        else:
            print("Valor inválido. O valor deve ser um TipoChamado")
