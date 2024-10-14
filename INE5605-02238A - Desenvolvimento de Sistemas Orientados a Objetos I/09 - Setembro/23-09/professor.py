from funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_do_livro: str) -> None:
        print(f'''Professor do departamento {self.departamento} pegou
              emprestado o livro {titulo_do_livro} com 
              {self.dias_de_emprestimo} dias de prazo''')
    
    def devolver(self, titulo_do_livro: str) -> None:
        return super().devolver(titulo_do_livro)