from funcionario import Funcionario


class Administrativo(Funcionario):
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_livro: str) -> None:
        return super().emprestar(titulo_livro)

    def devovler(self, titulo_livro: str) -> None:
        return super().devovler(titulo_livro)
