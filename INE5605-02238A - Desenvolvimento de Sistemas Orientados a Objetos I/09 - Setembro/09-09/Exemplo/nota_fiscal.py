from cliente import Cliente

class NotaFiscal:
    def __init__(self, numero:int, cliente:Cliente):
        self.__numero = int()
        self.__cliente = Cliente

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            raise ValueError("Valor inválido. O valor deve ser uma instância de Cliente")
