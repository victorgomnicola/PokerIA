
from Mesa import Mesa
from Jogador import Jogador
from JogadorChecador import JogadorChecador
from JogadorRandomico import JogadorRandomico
from JogadorSimples import JogadorSimples

n_jogadores_randomicos = 2
n_jogadores_checadores = 2
n_jogadores_simples = 2

players = [JogadorRandomico(i) for i in range(n_jogadores_randomicos)] + [JogadorChecador(j) for j in range(n_jogadores_randomicos,n_jogadores_randomicos+n_jogadores_checadores+1)] + [JogadorSimples(j) for j in range(n_jogadores_randomicos+n_jogadores_checadores+1,n_jogadores_randomicos+n_jogadores_checadores+1+n_jogadores_simples+1)]
m = Mesa(42, players)
m.iniciarJogo()