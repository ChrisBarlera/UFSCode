from aluno import Aluno


class AlunoPosGraduacao(Aluno):

    def __init__(self, matricula: int, elaborando_tese: bool) -> None:
        super().__init__(self, matricula)
        # Testando tipo de elaborando_tese
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese
        else:
            print("Valor inválido. O valor deve ser um bool")
    
    @property
    def elaborando_teste(self):
        return self.__elaborando_teste

    @elaborando_teste.setter
    def elaborando_teste(self, elaborando_teste: bool):
        if isinstance(elaborando_teste, bool):
            self.__elaborando_teste = elaborando_teste
        else:
            print("Valor inválido. O valor deve ser um bool")

    def emprestar(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            pass
            # self.__titulo_livro = titulo_livro
        else:
            print("Valor inválido. O valor deve ser um str")