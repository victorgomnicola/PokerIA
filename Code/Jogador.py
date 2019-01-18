# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:29 2019

@author: victo
"""

class Jogador:

    def __init__(self, id, montante = 3000):
        
        self.mao = [('b',-1),('b',-1)]
        self.montante = montante
        self.aposta = 0
        self.estaJogando = True
        self.idJogador = id

    def aposta(self, x):
    	self.montante-=x
    	self.aposta+=x
    
    def call(self, mesa_aposta):
    	dif = mesa_aposta - self.aposta
    	self.montante-= dif
    	return dif
        
    def getAcao(self, Estado, Log):
        pass
    