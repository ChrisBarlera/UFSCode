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
            raise ValueError("Valor inválido. O valor deve ser um int")
       
        # Testando tipo de titulo
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            raise ValueError("Valor inválido. O valor deve ser um str")
        
        # Testando tipo de ano
        if isinstance(ano, int):
            self.__ano = ano
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")
        
        # Testando tipo editora
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            raise ValueError("Argumento inválido. O argumento deve ser um objeto da classe Editora")

        # Testando tipo autor
        if isinstance(autor, Autor):
            self.__autor = autor
        else:
            raise ValueError("Argumento inválido. O argumento deve ser um objeto da classe Editora")

        # Testando tipo numero_capitulo
        if isinstance(numero_capitulo, int):
            self.__numero_capitulo = numero_capitulo
        else:
            raise ValueError("Valor inválido. O valor deve ser um int")        
        
        # Testando tipo de  de ano
        if isinstance(titulo_capitulo, str):
            self.__titulo_capitulo = titulo_capitulo
        else:
            raise ValueError("Valor inválido. O valor deve ser um str")
        self.__autores = [self.__autor]

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

    def find_capitulo_by_titulo(titulo: str) -> Capitulo:
        if isinstance(titulo, str):
            pass
        else:
            raise ValueError("Valor inválido. O valor deve ser um str")
