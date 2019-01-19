
from Jogador import Jogador
import random

class JogadorRandomico(Jogador):
	
	def __init__(self, id, fold_prob = 0.25, call_prob= 0.25, montante = 3000):
		
		Jogador.__init__(self,id, montante = 3000)
		self.fold_prob = fold_prob
		self.call_prob = call_prob

	def getAcao(self, estado, Log):
		p = random.uniform(0,1)
		p-= self.fold_prob
		if(p<0 or not self.canCall(estado['valorApostado'])):
			return -1
		p-= self.call_prob
		if(p<0):
			return 0
		return random.randint(1,self.montante+1)