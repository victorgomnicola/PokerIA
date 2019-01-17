
from Jogador import Jogador

class Logger:
	
	def __init__(self, table, game):
		self.table = table
		self.game = game
		self.log_hyperstring = str(table)+"_"+str(game)+".vic"

	def log_header(self, players):

		with f as open(self.log_hyperstring, 'w+'):
			f.write("PokerIA game \n")
			f.write("Table:"+ str(table)+"\n")
			f.write("Game:"+str(game)+"\n")
			f.write("Players cards\n")
			f.writelines(["Jogador"+str(player.idJogador)+":"+player.mao[0]+"/"+player.mao[1]+"\n" for player in players])
			f.write("Players chips\n")
			f.writelines(["Jogador"+str(player.idJogador)+":"+str(player.montante)+"\n" for player in players])



	def log_start(self, jogadores, button, big_blind):

		with f as open(self.log_hyperstring,'a'):
			f.write("*******Starting Game*******\n")
			f.write('Jogador' + str(self.jogadores[(button+1)%len(jogadores)].idJogador) + ':posts_smallBlind:' + str(big_blind/2)+"\n")
			f.write('Jogador' + str(self.jogadores[(button+2)%len(jogadores)].idJogador) + ':posts_bigBlind:' + str(big_blind)+"\n")

	def log_bet(self, player, bet, value):

		with f as open(self.log_hyperstring,'a'):
			f.write('Jogador'+str(player.idJogador)+":"+bet+":"+str(value))