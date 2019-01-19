
from Jogador import Jogador
import random

class JogadorChecador(Jogador):
	
	def __init__(self, id, montante = 3000):
		
		Jogador.__init__(self,id, montante = 3000)

	def getAcao(self, estado, Log):
		
		if(self.canCall(estado['valorApostado'])):
			return 0
		else:
			return -1