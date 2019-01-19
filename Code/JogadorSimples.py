

from Jogador import Jogador
from Verificador import Verificador
import random

class JogadorSimples(Jogador):
	
	def __init__(self, id, montante = 3000):
		
		Jogador.__init__(self,id, montante = 3000)
		self.Verificador = Verificador()

	def getAcao(self, estado, Log):
		
		if(estado['cartas'] ==  [('b',-1),('b',-1),('b',-1),('b',-1),('b',-1)]):
			return 0
		
		evaluation = self.Verificador.playerResults(self.mao+ [carta for carta in estado['cartas'] if carta!=('b',-1)])
		if(self.canCall(estado['valorApostado']) and evaluation[0]>=2):
			return 0
		else:
			return -1
		