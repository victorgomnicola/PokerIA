

from Jogador import Jogador
from Verificador import Verificador
import random

class JogadorSimples(Jogador):
	
	def __init__(self, id, montante = 3000):
		
		Jogador.__init__(self,id, montante = 3000)
		self.Verificador = Verificador()

	def getAcao(self, estado, Log):
		
		if(self.canCall(estado['valorApostado']) and self.Verificador.playerResults(self.mao+ estado['cartas'])[0]>3):
			return 0
		else:
			return -1
		