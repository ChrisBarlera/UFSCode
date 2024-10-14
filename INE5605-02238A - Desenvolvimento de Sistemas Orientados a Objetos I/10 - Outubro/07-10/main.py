from ControladorJogo import *

j1 = Jogador('ChatGPT')
tipo1 = Tipo('ar')
personagemA = Personagem(20,20,20,20,tipo1)
carta1 = Carta(personagemA)

j2 = Jogador('Humanidade')
tipo2 = Tipo('fogo')
personagemB = Personagem(10,20,20,20,tipo2)
carta2 = Carta(personagemB)

mesa = Mesa(j1,j2,carta1,carta2)

ControladorJogo().jogada(mesa)