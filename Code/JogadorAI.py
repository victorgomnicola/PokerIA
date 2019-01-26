from Jogador import Jogador
from Verificador import Verificador
import random
import numpy as np
import keras
import tensorflow as tf
from keras import backend as K


class JogadorAI(Jogador):

	def __init__(self, id, montante = 3000, policy_nn, value_nn):
		
		Jogador.__init__(self,id, montante = 3000)
		self.Verificador = Verificador()
		self.policy_nn = policy_nn
		self.value_nn = value_nn

	def getAcao(self, estado, Log):
		
		cartas_na_mesa = estado['cartas']
		cartas = [self.parse_card(card).reshape(shape = (1, card.shape[0])) for card in cartas_na_mesa +self.mao]
		vetor_de_entrada_rede = cartas[0]

		for i in range(1,len(cartas)):
			vetor_de_entrada_rede = np.concatenate((vetor_de_entrada_rede, cartas[i]), axis =1)

		vetor_de_entrada_rede = np.concatenate((vetor_de_entrada_rede, np.array([[estado['valorMesa'], estado['valorApostado'], self.montante]])), axis=1)

		if(estado['valorApostado'] == 0):
			actionz = [-1, 0, 1, 2, 3]
			entrada_rede = np.array([np.concatenate((vetor_de_entrada_rede, np.array([[a]])), axis =1) for a in actionz])
			
			saida = self.policy_nn.predict(entrada_rede).reshape(shape = (len(actionz), ))
			saida = np.exp(saida)
			saida = saida/saida.sum()

			chosen_action = 0
			p = np.random.uniform(0,1)
			
			for i in range(len(actionz)):
				p-= saida[i]
				if p <0:
					chosen_action = i
					break
			
			if actionz[chosen_action] not in [-1, 0]:
				return actionz[chosen_action]*self.big_Blind
			
			else:
				return actionz[chosen_action]


		else:
			actionz = [-1, 1, 1.5, 2, 3]
			entrada_rede = np.array([np.concatenate((vetor_de_entrada_rede, np.array([[a]])), axis =1) for a in actionz])

		self.policy_nn.predict([[1,2,34,6,5,7,8,9,3,4,54,23,42,34,23,42]])

	def parse_card(self,card):

		if(card[0]=='o'):
			return np.array([0,card[1]])
		elif(card[0]=='e'):
			return np.array([1,card[1]])
		elif(card[0]=='c'):
			return np.array([2,card[1]])
		elif(card[0]=='p'):
			return np.array([3,card[1]])
		else:
			return np.array([-1,card[1]])