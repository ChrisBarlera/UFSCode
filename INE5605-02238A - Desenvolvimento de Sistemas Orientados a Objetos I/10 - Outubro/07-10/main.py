from ControladorJogo import *

j1 = Jogador('ChatGPT')
j2 = Jogador('Humanidade')
mesa = Mesa(j1,j2,)
ControladorJogo().jogada()