from aluno import Aluno


class AlunoPosGraduacao(Aluno):

    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese
        else:
            print("Valor inválido. O valor deve ser um bool")

    def emprestar(self, titulo_livro: str):
        print(f'''Aluno de matrícula {self.matricula} pegou emprestado o livro
              {titulo_livro} com {self.dias_de_emprestimo} dias de prazo''')
        return super().emprestar(titulo_livro)