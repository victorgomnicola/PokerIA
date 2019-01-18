
from Jogador import Jogador

class Logger:
    
    def __init__(self, table, game):
        self.table = table
        self.game = game
        self.log_hyperstring = "./"+str(table)+"/"+str(game)+".txt"

    def log_header(self, players):

        with open(self.log_hyperstring, 'w+') as f:
            f.write("PokerIA game \n")
            f.write("Table:"+ str(self.table)+"\n")
            f.write("Game:" + str(self.game)+"\n")
            f.write("Players cards\n")
            f.writelines(["Jogador"+str(player.idJogador) + ":" + str(player.mao[0]) + "/"+str(player.mao[1]) + "\n" for player in players])
            f.write("Players chips\n")
            f.writelines(["Jogador" + str(player.idJogador) + ":" + str(player.montante) + "\n" for player in players])
            
        ##prints
        print("PokerIA game ")
        print("Table:"+ str(self.table))
        print("Game:" + str(self.game))
        print("Players chips")
        for l in ["Jogador" + str(player.idJogador) + ":" + str(player.montante)  for player in players]:
            print(l)


    def log_start(self, jogadores, button, big_blind):

        with open(self.log_hyperstring,'a') as f:
            f.write("*******Starting Game*******\n")
            f.write('Jogador' + str(jogadores[(button+1)%len(jogadores)].idJogador) + ':posts_smallBlind:' + str(big_blind/2) + "\n")
            f.write('Jogador' + str(jogadores[(button+2)%len(jogadores)].idJogador) + ':posts_bigBlind:' + str(big_blind) + "\n")

        print("*******Starting Game*******")
        print('Jogador' + str(jogadores[(button+1)%len(jogadores)].idJogador) + ':posts_smallBlind:' + str(big_blind/2) )
        print('Jogador' + str(jogadores[(button+2)%len(jogadores)].idJogador) + ':posts_bigBlind:' + str(big_blind))


    def log_bet(self, player, bet, value):

        with open(self.log_hyperstring,'a') as f:
            f.write('Jogador' + str(player.idJogador)+":" + bet + ":" + str(value)+"\n")
        
        print('Jogador' + str(player.idJogador)+":" + bet + ":" + str(value))
    
    
    def log_cartas_viradas(self, turn_name,cartas):
        with open(self.log_hyperstring,'a') as f:
            f.write("*******"+turn_name+"*******\n")
            f.write("Cartas na mesa:" + str(cartas[0]) + ":" + str(cartas[1]) + ":" + str(cartas[2]) + ":" + str(cartas[3]) + ":" + str(cartas[4]) +"\n")

        print("*******"+turn_name+"*******\n")
        print("Cartas na mesa:" + str(cartas[0]) + ":" + str(cartas[1]) + ":" + str(cartas[2]) + ":" + str(cartas[3]) + ":" + str(cartas[4]))

    def log_win(self, player, amount):
        with open(self.log_hyperstring,'a') as f:
            f.write("*******Winner*******\n")
            f.write("Jogador"+str(player.idJogador)+":won:"+str(amount)+"\n")
        
        print("*******Winner*******\n")
        print("Jogador"+str(player.idJogador)+":won:"+str(amount)+"\n")