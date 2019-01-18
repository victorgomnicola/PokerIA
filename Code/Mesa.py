# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:36:16 2019

@author: victo
"""
from Baralho import Baralho
from Logger import Logger
from Verificador import Verificador

class Mesa:

    def __init__(self ,id_mesa, jogadores, big_blind = 100, raiseCaps = 5):
        
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
        self.cartas = [('b',-1),('b',-1),('b',-1),('b',-1),('b',-1)]
        self.Verificador = Verificador()


    def iniciarJogo(self):
        
        for i in range(10):

            #Game setup
            button = i%self.nJogadores
            self.baralho.iniciarBaralho()
            self.distribuirCartas(button)
            self.valorMesa = 0
            self.valorApostado = 0

            #Logger
            game_logger = Logger(self.idMesa, i)
            game_logger.log_header(self.jogadores)

            #Start game
            self.comecarJogo(button)
            game_logger.log_start(self.jogadores,button,self.bigBlind)

            #Betting starts
            playerTurn = (button +3) % self.nJogadores
            playerTurn = self.apostar(game_logger, playerTurn)
            
            #Flop
            self.flop(game_logger)
            playerTurn = self.apostar(game_logger, playerTurn)
            
            #Turn
            self.turn(game_logger)
            playerTurn = self.apostar(game_logger, playerTurn)
            
            
            #River
            self.river(game_logger)
            playerTurn = self.apostar(game_logger, playerTurn)
        
            #show results
            winners = self.Verificador.matchWinner(self.cartas, self.jogadores)
            
            for w in winners:
                self.jogadores[w].montante += self.valorMesa/len(winners)
                game_logger.log_win(self.jogadores[w], self.valorMesa/len(winners))

            self.reset_mesa()

    def distribuirCartas(self, button):
        
        for i in range(self.nJogadores):
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[0] = self.baralho.tirarCarta()
            self.jogadores[(button + 1 + i)%self.nJogadores].mao[1] = self.baralho.tirarCarta()

    def comecarJogo(self, button):
        self.jogadores[(button+1)%self.nJogadores].apostar(self.smallBlind)
        self.jogadores[(button+2)%self.nJogadores].apostar(self.bigBlind)
        self.valorApostado = self.bigBlind
        self.valorMesa = self.bigBlind+ self.smallBlind
            



    def apostar(self, logger, t):
        
        playerTurn = t
        raise_marker = (playerTurn+self.nJogadores-1)%self.nJogadores
        n_raises = 0

        while(raise_marker != playerTurn):
            
            if(self.jogadores[playerTurn].estaJogando):

                action = self.jogadores[playerTurn].getAcao({'valorMesa':self.valorMesa, 'cartas': self.cartas, 'valorApostado':self.valorApostado, 'canRaise':  n_raises< self.raiseCaps}, {'table': self.idMesa, 'game':logger.game})                
                if(action==-1):
                    ##Player folds
                    self.jogadores[playerTurn].estaJogando= False
                    logger.log_bet(self.jogadores[playerTurn], 'folds', 0)
                
                elif(action==0):
                    
                    ##Player checks or checks
                    call_dif = self.jogadores[playerTurn].call(self.valorApostado)
                    self.valorMesa += call_dif
                    if call_dif >0:
                        logger.log_bet(self.jogadores[playerTurn], 'calls', call_dif)
                    if call_dif == 0:
                        logger.log_bet(self.jogadores[playerTurn],'checks', 0)
                
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
        
        return raise_marker

    def flop(self, logger):
        self.cartas[0] = self.baralho.tirarCarta()
        self.cartas[1] = self.baralho.tirarCarta()
        self.cartas[2] = self.baralho.tirarCarta()
        logger.log_cartas_viradas('flop',self.cartas)

    def turn(self, logger):
        self.cartas[3] = self.baralho.tirarCarta()
        logger.log_cartas_viradas('turn',self.cartas)
         
    def river(self, logger):
        self.cartas[4] = self.baralho.tirarCarta()
        logger.log_cartas_viradas('river',self.cartas)

    def reset_mesa(self):
        
        self.valorMesa = 0
        self.valorApostado=0
        
        for jogador in self.jogadores:
            jogador.reset()
        self.cartas = [('b',-1),('b',-1),('b',-1),('b',-1),('b',-1)]
        self.baralho.iniciarBaralho()