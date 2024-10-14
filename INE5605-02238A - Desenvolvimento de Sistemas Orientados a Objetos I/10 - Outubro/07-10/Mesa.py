from AbstractMesa import *
from Carta import *


class Mesa(AbstractMesa):

    #Construtor fornecido, nao deve ser alterado
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta):
        # Testando tipo de jogador1
        if isinstance(jogador1, Jogador):
            self.__jogador1 = jogador1
        else:
            print('Tipo inválido')

        # Testando tipo de jogador2
        if isinstance(jogador2, Jogador):
            self.__jogador2 = jogador2
        else:
            print('Tipo inválido')

        # Testando tipo de cartaJogador1
        if isinstance(cartaJogador1, Carta):
            self.__cartaJogador1 = cartaJogador1
        else:
            print('Tipo inválido')

        # Testando tipo de cartaJogador2
        if isinstance(cartaJogador2, Carta):
            self.__cartaJogador2 = cartaJogador2
        else:
            print('Tipo inválido')

    @property
    def jogador1(self) -> Jogador:
        return self.__jogador1

    @property
    def jogador2(self) -> Jogador:
        return self.__jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self.__cartaJogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self.__cartaJogador2
