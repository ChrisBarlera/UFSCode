class Capitulo:

    def __init__(self, numero: int, titulo: str):
        # Testando tipo de numero
        if isinstance(numero, int):
            self.__numero = numero
        else:
            print("Valor inválido. O valor deve ser um int")

        # Testando tipo de titulo
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor inválido. O valor deve ser um str")

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor inválido. O valor deve ser um str")
