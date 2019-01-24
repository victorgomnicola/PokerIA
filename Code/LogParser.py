
class LogParser:

	def __init__(self, log_file):
		self.log_file = log_file
		self.lines=[]
		self.game_over = False
	
	def parse_cards_on_the_table(self):

		self.readz()
		cards = []
		for l in self.lines:
			if "Cartas na mesa" in l:
				cards = []
				for s in l.split(":"):
					if "(" in s:
						s =s.replace("\n","").replace("(","").replace(")","").replace("'","")
						aux = s.split(",")
						cards.append((aux[0], int(aux[1])))
		return cards

	def get_player_cards(self, player):
		self.readz()
		cards = []
		for s in self.lines[5+player].split(":"):
			if "(" in s:
				s =s.replace("\n","").replace("(","").replace(")","").replace("'","")
				aux = s.split(",")
				cards.append((aux[0], int(aux[1])))
		return cards


	def read_log(self):
		self.readz()
		number_of_players = int(self.lines[3].replace("\n","").split(":")[1])
		resp = []
		for l in self.lines[3:4]+ self.lines[5+number_of_players:]:
			if not "Cartas na mesa" in l:
				resp.append(l)
		return resp

	def get_stats(self):

		self.readz()
		mesa = 0
		aposta = 0
		for l in self.lines:
			if('smallBlind' in l):
				sb = float(l.split(":")[2])
				mesa+=sb
				aposta+=sb
			if('bigBlind' in l):
				bb = float(l.split(":")[2])
				mesa+=bb
				aposta= bb
			if('calls' in l):
				c = float(l.split(":")[2])
				mesa+= c
			if('raises' in l):
				r = float(l.split(":")[2])
				aposta+=r
				mesa += r

		return (mesa, aposta)

	def readz(self):
		with open(self.log_file,'r') as f:
			self.lines= [s.replace("\n","") for s in f.readlines()]
			
			for l in self.lines:
				if "Winner" in l:
					self.game_over = True
