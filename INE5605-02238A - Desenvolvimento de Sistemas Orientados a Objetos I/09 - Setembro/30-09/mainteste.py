from controladorChamados import ControladorChamados
from controladorPessoas import ControladorPessoas
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

tc = TipoChamado(1,1,"Bug")
print(tc.codigo,tc.descricao,tc.nome) # 1 1 Bug
c = Cliente("Cliente", 2)
print(c.nome,c.codigo) # Cliente 2
t = Tecnico("Tecnico", 2)
print(t.nome,t.codigo) # Tecnico 2
ch = Chamado(Date.today(), c, t, "titulo", "descricao", 4, tc)
print(ch.tipo.nome) # Bug

cp = ControladorPessoas()
cp.inclui_cliente(1, "cli")
cp.inclui_tecnico(1, "tec")
for c in cp.clientes: # cli
    print(c.nome)
for t in cp.tecnicos: # tec
    print(t.nome)

cc = ControladorChamados()
print(cc.total_chamados_por_tipo(tc)) # 0