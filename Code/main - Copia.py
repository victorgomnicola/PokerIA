
from Mesa import Mesa
from Jogador import Jogador
from JogadorChecador import JogadorChecador
from JogadorRandomico import JogadorRandomico
from JogadorSimples import JogadorSimples
from JogadorGamer import JogadorGamer
from JogadorAI import JogadorAI
import sys
from keras.models import load_model

n_jogadores_randomicos = 0
n_jogadores_checadores = 8
n_jogadores_simples = 3
n_jogadores_gamers = 1

#policy_nn = load_model('policy.h5')
#value_nn = load_model('value.h5')
#players = [JogadorRandomico(i) for i in range(n_jogadores_randomicos)] + [JogadorChecador(j) for j in range(n_jogadores_randomicos,n_jogadores_randomicos+n_jogadores_checadores+1)] + [JogadorSimples(j) for j in range(n_jogadores_randomicos+n_jogadores_checadores+1,n_jogadores_randomicos+n_jogadores_checadores+1+n_jogadores_simples+1)]


players = [JogadorGamer(0)]+ [JogadorChecador(i) for i in range(1,(1+n_jogadores_checadores))]
#players= [JogadorChecador(i) for i in range(1,(1+n_jogadores_checadores))]
#m = Mesa(int(sys.argv[1]), players)
m = Mesa(42, players)
m.iniciarJogo()