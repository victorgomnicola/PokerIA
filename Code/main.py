
from Mesa import Mesa
from Jogador import Jogador
from JogadorChecador import JogadorChecador
from JogadorRandomico import JogadorRandomico
from JogadorSimples import JogadorSimples
from JogadorGamer import JogadorGamer
from JogadorAI import JogadorAI
import sys
from keras.models import load_model

n_jogadores_randomicos = 7
n_jogadores_checadores = 7
n_jogadores_simples = 2

policy_nn = load_model('policy.h5')
value_nn = load_model('value.h5')
#players = [JogadorRandomico(i) for i in range(n_jogadores_randomicos)] + [JogadorChecador(j) for j in range(n_jogadores_randomicos,n_jogadores_randomicos+n_jogadores_checadores+1)] + [JogadorSimples(j) for j in range(n_jogadores_randomicos+n_jogadores_checadores+1,n_jogadores_randomicos+n_jogadores_checadores+1+n_jogadores_simples+1)]
players = [JogadorAI(0, policy_nn, value_nn)]+ [JogadorChecador(i) for i in range(1,(1+n_jogadores_checadores))]
#players= [JogadorChecador(i) for i in range(1,(1+n_jogadores_checadores))]
m = Mesa(int(sys.argv[1]), players)
m.iniciarJogo()