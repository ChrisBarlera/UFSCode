from aluno import Aluno


class AlunoPosGraduacao(Aluno):

    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        # super().__init__(self, matricula)
        self.__elaborando_tese = False
    
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