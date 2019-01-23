from Jogador import Jogador
from Verificador import Verificador
import random

class JogadorGamer(Jogador):
	
	def __init__(self, id, montante = 3000):
		
		Jogador.__init__(self,id, montante = 3000)
		self.Verificador = Verificador()

	def getAcao(self, estado, Log):
		
		action = input()
		print(self.montante)
		return int(action)