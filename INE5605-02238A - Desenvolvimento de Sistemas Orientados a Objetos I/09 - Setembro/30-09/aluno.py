from usuario_bu import UsuarioBU


class Aluno(UsuarioBU):
    
    def __init__(self, matricula: int) -> None:
        # Testando tipo de matricula
        if isinstance(matricula, int):
            self.__matricula = matricula
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        if isinstance(matricula, int):
            self.__matricula = matricula
        else:
            print("Valor inválido. O valor deve ser um int")

    def emprestar(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            pass
            # self.__titulo_livro = titulo_livro
        else:
            print("Valor inválido. O valor deve ser um str")