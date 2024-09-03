class Pessoa:
    def __init__(self, nome:str):
        self.__nome = nome
    
    # def get_nome(self):
    #     return self.__nome
    #
    # def set_nome(self, nome:str):
    #     if isinstance(nome, str):
    #         self.__nome = nome
    #     else:
    #         raise ValueError("Valor inválido. O valor deve ser um str")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome:str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Valor inválido. O valor deve ser um str")