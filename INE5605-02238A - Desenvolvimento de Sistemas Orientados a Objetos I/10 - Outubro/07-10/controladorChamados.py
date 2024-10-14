from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        contador = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                contador += 1
        return contador

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico,
                       titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado) -> Chamado:
        novo_chamado = Chamado(data,
                               cliente,
                               tecnico,
                               titulo,
                               descricao,
                               prioridade,
                               tipo)
        if len(self.__chamados) != 0:
            for chamado in self.__chamados:
                if (chamado.data == data and chamado.cliente == cliente
                    and chamado.tecnico == tecnico and chamado.tipo == tipo):
                    print('Erro: chamado já cadastrado')
                    break
                else:
                    self.__chamados.append(novo_chamado)
                    return novo_chamado
        else:
            self.__chamados.append(novo_chamado)
        return novo_chamado

    def inclui_tipochamado(self, codigo: int,
                           nome: str, descricao: str) -> TipoChamado:
        novo_tipo = TipoChamado(codigo, descricao, nome)
        if len(self.__tipos_chamados) != 0:
            for chamado in self.__tipos_chamados:
                if chamado.codigo != codigo:
                    self.__tipos_chamados.append(novo_tipo)
                    return novo_tipo
            else:
                print('Tipo de chamado já cadastrado')
        else:
            self.__tipos_chamados.append(novo_tipo)
        return novo_tipo

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados

    @property
    def chamados(self):
        return self.__chamados
