# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:16 2019

@author: victo
"""
from Baralho import Baralho
from Jogador import Jogador
class Mesa:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.bigBlind = 100
        self.smallBlind = self.bigBlind/2
        self.idMesa = 42
        self.baralho = Baralho()
        self.nJogadores = len(self.jogadores)
        self.logFinal
        
    def iniciarJogo(self):
        button = random.randint(1, self.nJogadores)
        valorMesa = 0
        valorApostado = 0
        raiseCaps = 5
        for i in range(1,1000):
            estado = {}
            logRodada = 'PokerIA Hand #' + str(self.idMesa) + '-'+ str(i) + ':  Holdem No Limit (50/100) - data/hora' + str(self.nJogadores)
            baralho.embaralhar()
            distribuirCartas(self, button)
            
            #Laco para construir o cabecalho do log com cartas dos jogadores
            for j in range(0, len(self.jogadores)):
                logRodada += '\nJogador'+ str(self.jogadores[j].idJogador) + ': ' + self.jogadores[j].cartas[0] + ' ' + self.jogadores[j].cartas[1]
        
            #Laco para construir o cabecalho do log com fichas dos jogadores
            for j in range(0, len(self.jogadores)):
                logRodada += '\nJogador'+ str(self.jogadores[j].idJogador) + ': ' + str(self.jogadores[j].montante)
                

            logRodada += '\n**********Starting the Game**********'
            
            jogadorDaVez = button + 1
            turn = 0
            betsRaised = 0
            
            #jogador inicial paga o small blind
            self.jogadores[jogadorDaVez].montante -= self.smallBlind
            
            #grava no log da rodada
            logRodada += '\nJogador' + str(self.jogadores[jogadorDaVez].idJogador) + 'posts smallBlind: ' + str(self.smallBlind)
            
            #atualiza o valor apostado e incrementa o montante da mesa
            valorApostado = self.smallBlind
            valorMesa += valorApostado
            
            #atualiza turno
            jogadorDaVez = (jogadorDaVez+1)%self.nJogadores
            
            #jogador paga o big blind
            self.jogadores[jogadorDaVez].montante -= self.bigBlind
            
            #grava no log da rodada
            logRodada += '\nJogador' + str(self.jogadores[jogadorDaVez].idJogador) + 'posts bigBlind: ' + str(self.bigBlind)
            
            #atualiza o valor apostado e incrementa o montante da mesa
            valorApostado = self.bigBlind
            valorMesa += valorApostado
            
             #atualiza turno do jogador
            jogadorDaVez = (jogadorDaVez+1)%self.jogadores
            
            self.jogadores[jogadorDaVez].getAcao(self, Estado, logAtual, self.logFinal)
            
            
            
            
            self.jogadores[button+1]
                
                
                
                
                
            (button + 1)%self.nJogadores
            
    def distribuirCartas(self, button):
        
        for i in range(0, self.nJogadores):
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[].append(baralho.tirarCarta())
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[].append(baralho.tirarCarta())
    
    def gravarLog(self, logRodada):
        pass
    