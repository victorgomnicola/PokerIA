
from Mesa import Mesa
from Jogador import Jogador

players = [Jogador(i) for i in range(5)]
m = Mesa(42, players)
m.iniciarJogo()