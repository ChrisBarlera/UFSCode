class Kwargs():
    def __init__(self) -> None:
        pass

    def teste(self,**coisas):
        return coisas

opa = Kwargs()


print(opa.teste(nota10=20, nota20=2))
opa.teste(nota10=20)
