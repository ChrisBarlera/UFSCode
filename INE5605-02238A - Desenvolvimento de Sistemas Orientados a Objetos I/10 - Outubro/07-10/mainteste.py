from controladorChamados import ControladorChamados
from chamado import Chamado
from cliente import Cliente
from tecnico import Tecnico
from tipoChamado import TipoChamado
from datetime import date as Date

datateste = Date(2024,12,21)
clienteteste = Cliente('Fulano', 123)
tecnicoteste = Tecnico('Técnico', 321)
tipoteste = TipoChamado(1,'Um tipo de chamado', 'Tipo 1')

controlador_chamados = ControladorChamados()
controlador_chamados.inclui_chamado(datateste,
                                    clienteteste,
                                    tecnicoteste,
                                    'pane no sistema',
                                    'alguém me desconfigurou',
                                    2,
                                    tipoteste)

controlador_chamados.inclui_chamado(datateste,
                                    clienteteste,
                                    tecnicoteste,
                                    'pane no sistema',
                                    'alguém me desconfigurou',
                                    2,
                                    tipoteste)

controlador_chamados.inclui_tipochamado(1,
                                        'Pane',
                                        'Tem pane no sistema')
controlador_chamados.inclui_tipochamado(1,
                                        'Pane',
                                        'Tem pane no sistema')

print(controlador_chamados.chamados)
print(controlador_chamados.tipos_chamados)