# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:16 2019

@author: victo
"""
class Mesa:
    def __initi__(self):
        self.jogadores = []
        self.smallBlind = bigBlind/2
        self.bigBlind = 100
        self.idMesa = 42
        self.baralho
        
    def iniciarJogo(self):
        for i in range(1,1000):
            
            logRodada = 'PokerIA Hand #' + str(self.idMesa) '\00'+ str(i) + ':  Holdem No Limit (50/100) - data/hora' + str(self.jogadores.__len__())
            
            distribuirCartas(self, button)
            
            #Laco para construir o cabecalho do log com cartas dos jogadores
            for j in range(0, self.jogadores.__len__()-1):
                logRodada += '\nJogador'+ str(self.jogadores[j].idJogador) + str(self.jogadores[j].montante)
        
            #Laco para construir o cabecalho do log com fichas dos jogadores
            
            
    def distribuirCartas(self, button):
        aux = button + 1
        for i in range(0, self.jogadores.__len__()-1):
            self.jogadores[i]
    
    def gravarLog(self, logRodada):
        pass
    