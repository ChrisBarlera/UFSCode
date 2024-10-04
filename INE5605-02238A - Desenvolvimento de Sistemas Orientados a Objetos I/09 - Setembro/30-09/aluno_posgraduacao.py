from aluno import Aluno


class AlunoPosGraduacao(Aluno):

    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    @property
    def elaborando_teste(self):
        return self.__elaborando_tese

    @elaborando_teste.setter
    def elaborando_teste(self, elaborando_tese: bool):
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese
        else:
            print("Valor inválido. O valor deve ser um bool")

    def emprestar(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            pass
            # self.__titulo_livro = titulo_livro
        else:
            print("Valor inválido. O valor deve ser um str")