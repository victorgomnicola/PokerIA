from Jogador import Jogador
from Verificador import Verificador
import random
import numpy as np
import keras
import tensorflow as tf
from keras import backend as K
import pickle

class JogadorAI(Jogador):

    def __init__(self, id,  policy_nn, value_nn, montante = 3000):
        
        Jogador.__init__(self,id, montante = 3000)
        self.Verificador = Verificador()
        self.policy_nn = policy_nn
        self.value_nn = value_nn
        self.log_action = [[]]

    def getAcao(self, estado, Log):
        
        cartas_na_mesa = estado['cartas']
        cartas = [self.parse_card(card) for card in cartas_na_mesa +self.mao]
        cartas = np.array(cartas, dtype = np.float32).reshape((1, len(cartas_na_mesa +self.mao)*2))
        vetor_de_entrada_rede = cartas
        vetor_de_entrada_rede = np.concatenate((vetor_de_entrada_rede, np.array([[estado['valorMesa'], estado['valorApostado'], self.montante]])), axis=1)

        if(estado['valorApostado'] == 0):
            actionz = [-1, 0, 1, 2, 3]
            entrada_rede = np.array([np.concatenate((vetor_de_entrada_rede, np.array([[a]])), axis =1) for a in actionz]).reshape((len(actionz), len(vetor_de_entrada_rede)))
            print(entrada_rede.shape())
            saida = self.policy_nn.predict(entrada_rede).reshape((len(actionz), ))
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

                self.log_action[-1]+=[vetor_de_entrada_rede,actionz[chosen_action], actionz[chosen_action]*self.big_Blind ]
                return actionz[chosen_action]*self.big_Blind 
            else:
                if actionz[chosen_action]==-1:
                    self.log_action[-1]+=[vetor_de_entrada_rede,actionz[chosen_action],0, np.zeros(17)]
                    self.log_action.append([])
                if actionz[chosen_action] ==0:
                    self.log_action[-1]+=[vetor_de_entrada_rede,actionz[chosen_action],0]
                return actionz[chosen_action]


        else:
            actionz = [-1, 1, 1.5, 2, 3]
            entrada_rede = np.array([np.concatenate((vetor_de_entrada_rede, np.array([[a]])), axis =1) for a in actionz]).reshape((len(actionz), vetor_de_entrada_rede.shape[1]+1))
            print(entrada_rede.shape)
            print(entrada_rede)
            saida = self.policy_nn.predict(entrada_rede).reshape((len(actionz), ))
            print(saida)
            saida = np.exp(saida)
            print(saida)
            saida = saida/saida.sum()
            print(saida)

            chosen_action = 0
            p = np.random.uniform(0,1)
            
            for i in range(len(actionz)):
                p-= saida[i]
                if p <0:
                    chosen_action = i
                    break

            
            if actionz[chosen_action] not in [-1, 1]:

                self.log_action[-1]+=[vetor_de_entrada_rede,actionz[chosen_action], actionz[chosen_action]*self.big_Blind ]
                return actionz[chosen_action]*(estado['valorApostado'])
            else:
                if actionz[chosen_action]==-1:
                    self.log_action[-1]+=[vetor_de_entrada_rede,actionz[chosen_action],0, np.zeros(17)]
                    self.log_action.append([])
                if actionz[chosen_action] ==1:
                    self.log_action[-1]+=[vetor_de_entrada_rede,actionz[chosen_action],0]
                return actionz[chosen_action]

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

    def reward(self, amount):

        self.log_action[-1]+=[amount, np.zeros(17)]
        self.log_action.append([])
        self.montante+=amount
    
    def shut_down(self):

        pickle.dump(self.log_action, open("LogFile_"+str(self.id), "wb"))