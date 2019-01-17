# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:16 2019

@author: victo
"""
from Baralho import Baralho
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
        self.playerTurn = 0


    def iniciarJogo(self):
        
        for i in range(1000):

            #Game setup
            button = i%self.nJogadores
            playerTurn = button + 1
            self.baralho.iniciarBaralho()
            self.distribuirCartas(self, button)
            self.valorMesa = 0
            self.valorApostado = 0

            #Logger
            game_logger = Logger(self.idMesa, i)
            game_logger.log_header(self.jogadores)

            #Start game
            self.comecarJogo()
            game_logger.log_start(self.jogadores,button,self.bigBlind)
            
            playerTurn = (playerTurn + 2)%self.jogadores
            
            #Betting starts
            self.apostar(game_logger, playerTurn)
            
            #Turn the flop
            self.flop
            
            self.valorApostado = 0
            
            #Betting restarts
            self.apostar(game_logger, playerTurn)
            
            #Turn the turn
            self.turn
            
            #reset bets
            self.valorApostado = 0
            
            #Betting restarts
            self.apostar(game_logger, playerTurn)
            
            #turn the river
            self.river
            
            #reset bets
            self.valorApostado = 0
            
            #Betting restarts again
            self.apostar(game_logger, playerTurn)
            
            
            #show results
            
    def distribuirCartas(self, button):
        
        for i in range(self.nJogadores):
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[0] = self.baralho.tirarCarta()
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[1] = self.baralho.tirarCarta()

    def comecarJogo(self, button):
        self.jogadores[(button+1)%self.nJogadores].aposta(self.smallBlind)
        self.jogadores[(button+2)%self.nJogadores].aposta(self.bigBlind)



    def apostar(self, logger, playerTurn):
        
        
        raise_marker = (playerTurn)%self.nJogadores
        n_raises = 0

        while(raise_marker != playerTurn):
            
            if(self.jogadores[playerTurn].estaJogando):

                action = self.jogadores[playerTurn].getAcao({'valorMesa':self.valorMesa, 'cartas': self.cartas, 'valorApostado':self.valorApostado, 'canRaise':  n_raises< self.raiseCaps}, {'table': self.idMesa, 'game':logger.game})                
                
                if(action==-1):
                    ##Player folds
                    self.jogadores[playerTurn].estaJogando= False
                    logger.log_bet(self.jogadores[playerTurn], 'folds', 0)
                
                elif(action==0):
                    ##Player checks
                    call_dif = self.jogadores[playerTurn].call(self.valorApostado)
                    self.valorMesa += call_dif
                    logger.log_bet(self.jogadores[playerTurn], 'calls', call_dif)

                elif(action>0):
                    ##Player raises
                    raise_dif = self.jogadores[playerTurn].call(self.valorApostado + action)
                    self.valorApostado += action
                    self.valorMesa += action
                    raise_marker = playerTurn
                    logger.log_bet(self.jogadores[playerTurn], 'raises', raise_dif)
                    n_raises = n_raises + 1

                else:
                    raise ValueError('No valid action value')

            playerTurn = (playerTurn+1)%self.nJogadores

    def flop(self, logger):
        self.cartas[0] = self.baralho.tirarCartas()
        self.cartas[1] = self.baralho.tirarCartas()
        self.cartas[2] = self.baralho.tirarCartas()
        logger.log_cartas_viradas(cartas)

    def turn(self):
         self.cartas[3] = self.baralho.tirarCartas()
         logger.log_cartas_viradas(cartas)
         
    def river(self):
         self.cartas[4] = self.baralho.tirarCartas()
         logger.log_cartas_viradas(cartas)