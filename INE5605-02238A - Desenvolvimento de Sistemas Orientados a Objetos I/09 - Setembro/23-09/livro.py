from editora import Editora
from autor import Autor

class Livro:

    def __init__(self, codigo: int, titulo: str,
                 ano: int, editora: Editora, autor: Autor,
                 numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autor = autor
        self.__numero_capitulo = numero_capitulo
        self.__titulo_capitulo = titulo_capitulo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            raise ValueError("Valor inválido. O valor deve ser um str")

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            raise ValueError("Argumento inválido. O argumento deve ser um objeto da classe Editora")
    
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        if isinstance(autor, Autor):
            self.__autor = autor
        else:
            raise ValueError("Argumento inválido. O argumento deve ser um objeto da classe Autor")
    @property
    def numero_capitulo(self):
        return self.__numero_capitulo

    @numero_capitulo.setter
    def numero_capitulo(self, numero_capitulo: int):
        if isinstance(numero_capitulo, int):
            self.__numero_capitulo = numero_capitulo
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")
    
    @property
    def titulo_capitulo(self):
        return self.__titulo_capitulo

    @titulo_capitulo.setter
    def titulo_capitulo(self, titulo_capitulo: str):
        if isinstance(titulo_capitulo, str):
            self.__titulo_capitulo = titulo_capitulo
        else:
            raise ValueError("Valor inválido. O valor deve ser um str")
