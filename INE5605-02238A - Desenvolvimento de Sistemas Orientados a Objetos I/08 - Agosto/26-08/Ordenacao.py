"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


class Ordenacao():

    # meu algoritmo
    def ordena(self, array_para_ordenar: []):
        """Realiza a ordenacao do conteudo do array recebido como parâmetro"""
        ordenado = []
        for i in range(len(array_para_ordenar)):
            menor = array_para_ordenar[0]
            for numero in array_para_ordenar:
                if numero < menor:
                    menor = numero

            ordenado.append(menor)
            array_para_ordenar.remove(menor)
        return ordenado

    # bubble sort
    # def ordena(self, array_para_ordenar:[]):
    #     for i in range(len(array_para_ordenar)):
    #         for j in range(len(array_para_ordenar)-(i+1)):
    #             if array_para_ordenar[j] > array_para_ordenar[j+1]:
    #                 # trocar [j] com [j+1]
    #                 temp = array_para_ordenar[j]
    #                 array_para_ordenar[j] = array_para_ordenar[j+1]
    #                 array_para_ordenar[j+1] = temp

    #     return array_para_ordenar

    def to_string(self, array_ordenado: []):
        """Converte o conteudo do array em String formatado
           Exemplo:
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        tamanho = len(array_ordenado)
        texto = ""
        for i in range(tamanho):
            if i == tamanho - 1:
                texto += str(array_ordenado[i])
            else:
                texto += str(array_ordenado[i]) + ','
        return texto