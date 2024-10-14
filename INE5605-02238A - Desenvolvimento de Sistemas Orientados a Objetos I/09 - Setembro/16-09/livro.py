from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:

    def __init__(self, codigo: int, titulo: str,
                 ano: int, editora: Editora, autor: Autor,
                 numero_capitulo: int, titulo_capitulo: str):
        # Testando tipo de codigo
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valor inválido. O valor deve ser um int")

        # Testando tipo de titulo
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor inválido. O valor deve ser um str")

        # Testando tipo de ano
        if isinstance(ano, int):
            self.__ano = ano
        else:
            print("Valor inválido. O valor deve ser um int")

        # Testando tipo editora
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Editora
                """
            )

        # Testando tipo autor
        if isinstance(autor, Autor):
            self.__autor = autor
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Autor
                """
            )

        # Testando tipo numero_capitulo
        if isinstance(numero_capitulo, int):
            self.__numero_capitulo = numero_capitulo
        else:
            print("Valor inválido. O valor deve ser um int")

        # Testando tipo de titulo_capitulo
        if isinstance(titulo_capitulo, str):
            self.__titulo_capitulo = titulo_capitulo
        else:
            print("Valor inválido. O valor deve ser um str")

        self.__autores = [self.__autor]
        self.__capitulos = [
            Capitulo(self.__numero_capitulo, self.__titulo_capitulo)
        ]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            print("Valor inválido. O valor deve ser um str")

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano
        else:
            print("Valor inválido. O valor deve ser um int")

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Editora
                """
            )

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        if isinstance(autor, Autor):
            self.__autor = autor
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Autor
                """
            )

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor not in self.__autores:
                self.__autores.append(autor)
            else:
                print("Erro: Autor já está registrado neste livro")
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Autor
                """
            )

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor in self.__autores:
                self.__autores.remove(autor)
            else:
                print("Erro: Autor não está registrado neste livro")
        else:
            print(
                """
                Argumento inválido.
                O argumento deve ser um objeto da classe Autor
                """
            )

    def incluir_capitulo(self, numero: int, titulo: str):
        if isinstance(numero, int) and isinstance(titulo, str):
            if self.find_capitulo_by_titulo(titulo) is None:
                self.__capitulos.append(Capitulo(numero, titulo))
            else:
                print("Capítulo já inserido neste livro.")
        else:
            print(
                """
                Valor(es) inválido(s).
                Os valores devem ser do tipo int e str, respectivamente
                """
            )

    def excluir_capitulo(self, titulo: str):
        if isinstance(titulo, str):
            capitulo_obj = self.find_capitulo_by_titulo(titulo)
            self.__capitulos.remove(capitulo_obj)
        else:
            print("Valor inválido. O valor deve ser do tipo str")

    def find_capitulo_by_titulo(self, titulo: str) -> Capitulo:
        if isinstance(titulo, str):
            for capitulo in self.__capitulos:
                if capitulo.titulo == titulo:
                    return capitulo
            else:
                print("Capítulo não encontrado")
        else:
            print("Valor inválido. O valor deve ser um str")
