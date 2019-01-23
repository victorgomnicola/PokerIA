
from Mesa import Mesa
from Jogador import Jogador
from JogadorChecador import JogadorChecador
from JogadorRandomico import JogadorRandomico
from JogadorSimples import JogadorSimples
from JogadorGamer import JogadorGamer
import sys

n_jogadores_randomicos = 7
n_jogadores_checadores = 7
n_jogadores_simples = 2

#players = [JogadorRandomico(i) for i in range(n_jogadores_randomicos)] + [JogadorChecador(j) for j in range(n_jogadores_randomicos,n_jogadores_randomicos+n_jogadores_checadores+1)] + [JogadorSimples(j) for j in range(n_jogadores_randomicos+n_jogadores_checadores+1,n_jogadores_randomicos+n_jogadores_checadores+1+n_jogadores_simples+1)]
players = [JogadorGamer(0)]+ [JogadorChecador(i) for i in range(1,(1+n_jogadores_checadores))]
#players= [JogadorChecador(i) for i in range(1,(1+n_jogadores_randomicos))]
m = Mesa(int(sys.argv[1]), players)
m.iniciarJogo()