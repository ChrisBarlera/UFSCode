from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        # Testando tipo de personagem
        if isinstance(personagem, Personagem):
            self.__personagem = personagem
        else:
            print('Tipo inválido')

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        total = (self.__personagem.energia + self.__personagem.habilidade +
                self.__personagem.velocidade + self.__personagem.resistencia)
        return total

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
