class Cliente:
    def __init__(self, codigo:int, endereco:str):
        self.__codigo = int()
        self.__endereco = str()

        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(endereco, str):
            self.__endereco = endereco



    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo:int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,endereco:str):
        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")