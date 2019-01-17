# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:16 2019

@author: victo
"""
from Baralho import Baralho
from Jogador import Jogador
from Logger import Logger

class Mesa:

    def __init__(self, jogadores, id_mesa, big_blind = 100, raiseCaps = 5):
        
        #####Player attributes
        self.jogadores = jogadores
        self.nJogadores = len(self.jogadores)

        #####Betting atributes
        self.bigBlind = big_blind
        self.smallBlind = self.bigBlind/2
        
        #####Table attributes
        self.idMesa = id_mesa
        self.baralho = Baralho()
        self.raiseCaps = raiseCaps
        self.valorMesa = 0
        self.valorApostado = 0
        self.cartas = ['b','b','b','b','b']


    def iniciarJogo(self):
        
        for i in range(1000):

            #Game setup
            button = i%self.nJogadores
            self.baralho.iniciarBaralho()
            distribuirCartas(self, button)
            self.valorMesa = 0
            self.valorApostado = 0

            #Logger
            game_logger = Logger(self.idMesa, i)
            game_logger.log_header(self.jogadores)

            #Start game
            self.comecarJogo()
            game_logger.log_start(self.jogadores,button,self.bigBlind)

            #Betting starts
            self.apostar(game_logger)
            
    def distribuirCartas(self, button):
        
        for i in range(self.nJogadores):
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[0] = baralho.tirarCarta()
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[1] = baralho.tirarCarta()

    def comecarJogo(self, button):
        self.jogadores[(button+1)%self.nJogadores].aposta(smallBlind)
        self.jogadores[(button+2)%self.nJogadores].aposta(bigBlind)



    def apostar(self, logger):
        
        t = (button+3)%self.nJogadores
        raise_marker = (button+2)%self.nJogadores
        n_raises = 0 

        while(raise_marker!=t):
            
            if(self.jogadores[t].estaJogando):

                action = self.jogadores[t].getAcao({'valorMesa':self.valorMesa, 'cartas': self.cartas, 'valorApostado':valorApostado}, n_raises< self.raiseCaps, {'table': self.idMesa, 'game':i})                
                if(action==-1):
                    ##Player folds
                    self.jogadores[t].estaJogando= False
                    logger.log_bet(self.jogadores[t], 'folds', 0)
                
                elif(action==0):
                    ##Player checks
                    check_dif = self.jogadores[t].check(self.valorApostado)
                    self.valorMesa += check_dif
                    logger.log_bet(self.jogadores[t], 'checks', check_dif)

                elif(action>0):
                    ##Player raises
                    raise_dif = self.jogadores[t].check(self.valorApostado+ action)
                    self.valorApostado+= action
                    logger.log_bet(self.jogadores[t], 'raises', raise_dif)

                else:
                    raise ValueError('No valid action value')

            t = (t+1)%self.nJogadores