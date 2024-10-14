from AbstractPersonagem import *

class Tipo(Enum):

    ar = "ar"
    terra = "terra"
    fogo = "fogo"
    agua = "agua"

class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        # Testando tipo de energia
        if isinstance(energia, int):
            self.__energia = energia
        else:
            print('Tipo inválido')

        # Testando tipo de habilidade
        if isinstance(habilidade, int):
            self.__habilidade = habilidade
        else:
            print('Tipo inválido')

        # Testando tipo de velocidade
        if isinstance(velocidade, int):
            self.__velocidade = velocidade
        else:
            print('Tipo inválido')

        # Testando tipo de resistencia
        if isinstance(resistencia, int):
            self.__resistencia = resistencia
        else:
            print('Tipo inválido')

        # Testando tipo de tipo
        if isinstance(tipo, Tipo):
            self.__tipo = tipo
        else:
            print('Tipo inválido')

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @property
    def energia(self) -> int:
        return self.__energia

    @property
    def habilidade(self) -> int:
        return self.__habilidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def resistencia(self) -> int:
        return self.__resistencia
