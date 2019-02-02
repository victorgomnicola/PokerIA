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
        self.cartas = [('b',-1), ('b',-1), ('b',-1), ('b',-1), ('b',-1)]
        self.Verificador = Verificador()


    def eliminate_poor(self):
        for p in self.jogadores:
            if p.montante < 100:
                p.shut_down()
                self.jogadores.remove(p)
        self.nJogadores = len(self.jogadores)

    def iniciarJogo(self):
        
        for i in range(1000):

            #Game setup
            self.eliminate_poor()
            print(i)
            button = (i + self.nJogadores)%self.nJogadores
            
            while not self.jogadores[button].estaJogando:
                button -= 1

            self.baralho.iniciarBaralho()
            self.distribuirCartas(button)
            self.valorMesa = 0
            self.valorApostado = 0

            #Logger
            game_logger = Logger(self.idMesa, i)
            game_logger.log_header(self.jogadores)

            #Start game
            self.comecarJogo(button)
            game_logger.log_start(self.jogadores, button, self.bigBlind)

            #Betting starts
            self.apostar(game_logger, (button +3)%self.nJogadores)

            #Flop
            playerTurn = (button + 1)%self.nJogadores
            self.flop(game_logger)
            self.apostar(game_logger, playerTurn)
            
            #Turn
            self.turn(game_logger)
            self.apostar(game_logger, playerTurn)
            
            #River
            self.river(game_logger)
            self.apostar(game_logger, playerTurn)
        
            #show results
            winners = self.Verificador.matchWinner(self.cartas, [jogador for jogador in enumerate(self.jogadores) if jogador[1].estaJogando])
            
            for w in winners:
                self.jogadores[w].reward(self.valorMesa/len(winners))
                game_logger.log_win(self.jogadores[w], self.valorMesa/len(winners))

            self.reset_mesa()

        for p in self.jogadores:
            p.shut_down()

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
        
        while not self.jogadores[raise_marker].estaJogando:
            raise_marker = (raiz_marker-1+self.nJogadores)%nJogadores

        n_raises = 0

        while(True):
            
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
                
                if raise_marker == playerTurn:
                    break

            playerTurn = (playerTurn+1)%self.nJogadores



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

