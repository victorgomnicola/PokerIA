# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:29 2019

@author: victo
"""

class Jogador:

    def __init__(self, id, montante = 3000):
        
        self.mao = []
        self.montante = montante
        self.estaJogando = True
        self.idJogador = id
        
    def getAcao(self, Estado, can_raise, Log):
        pass
    