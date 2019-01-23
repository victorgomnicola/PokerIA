# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:31:16 2019

@author: victo
"""
from itertools import combinations

class Verificador:	 

	def contaIguais(self, mao):
		highest_card = mao[0][1]
		count = 0
		two_pairs= False
		
		for i in range(len(mao)):

			count_aux = 0
			for j in range(i, len(mao)):
				if (mao[i][1] == mao[j][1]):
					count_aux+=1
			
			if (count_aux==count and count==2 and mao[i][1]!= highest_card):
				two_pairs= True
			
			if(count_aux== count and mao[i][1]>highest_card):
				highest_card = mao[i][1]

			if(count_aux> count):
				count = count_aux
				highest_card = mao[i][1]

		ordered_hand = [card for card in mao if card[1]==highest_card]+ sorted([card for card in mao if card[1]!=highest_card], key =lambda x:x[1])
		
		if (two_pairs):
			rest_hand = sorted([card for card in mao if card[1]!=highest_card], key =lambda x:x[1])
			aux_count =1
			aux_value = rest_hand[0][1]
			
			for card in rest_hand:
				if card[1] == aux_value:
					aux_count+=1
			
			if(aux_count==2):
				ordered_hand = [card for card in mao if card[1]==highest_card]+ sorted([card for card in mao if card[1]!=highest_card], key =lambda x:x[1], reverse= True)
							
			else :
				ordered_hand = [card for card in mao if card[1]==highest_card]+ sorted([card for card in mao if card[1]!=highest_card], key =lambda x:x[1])
			
		return (count, ordered_hand, two_pairs)

	def verificaFullHouse(self, hand):
		if hand[-1][1]==hand[-2][1]:
			return True
		return False 
	
	def verificaFlush(self, hand):
		
		suit = hand[0][0]
		
		for card in hand:	
			if card[0] != suit:
				return False
		return True
	
	def verificaStraight(self, hand):
		
		sorted_hand = sorted(hand, key = lambda x: x[1], reverse = True)
		for i in range(len(hand)-1):
			if sorted_hand[i][1]-sorted_hand[i+1][1]!= 1:
				return False
		return True

	def verificaMao(self, hand):

		sorted_hand = sorted(hand, key = lambda x: x[1], reverse = True)
		flush = self.verificaFlush(sorted_hand)
		straight = self.verificaStraight(sorted_hand)
		
		if (flush and straight and sorted_hand[0][1] ==13):
			## Royal Flush
			return (10, sorted_hand)
		
		elif (flush and straight):
			## Straight flush
			return (9, sorted_hand)

		count , count_hand, two_pairs = self.contaIguais(hand)
		if (count ==4):
			## Four of a kind
			return (8, count_hand)

		elif (count ==3 and self.verificaFullHouse(count_hand)):
			## Full House
			return (7, count_hand)
		
		elif (flush):
			## Flush
			return (6, sorted_hand)
		
		elif (straight):
			## Straight
			return (5, sorted_hand)

		elif(count ==3):
			## Three of a kind
			return (4 , count_hand)
		
		elif (two_pairs):
			## Two pairs
			return(3, count_hand)
		
		else:
			#One pair or less
			return (count, count_hand)

	def playerResults(self, result):
		best_score = 1
		best_hand = [('b',-1)]

		for hand in combinations(result, 5):
			score, h = self.verificaMao(hand)
			if(score> best_score):
				best_score = score
				best_hand= h
			if( score == best_score and best_hand[0][1]< h[0][1]):
				best_hand = h


		return (best_score, best_hand)

	def matchWinner(self, table_cards, players):
		playerz = [p[1] for p in players]
		player_scores = [self.playerResults(table_cards+player.mao) for player in playerz]
		winner_score = 0
		#################
		# for p in player_scores:
			# print(p)
		################
		for score in player_scores:
			if (score[0]> winner_score):
				winner_score = score[0]

		potential_winners = []
		
		for s in range(len(player_scores)):
			if player_scores[s][0]== winner_score:
				potential_winners.append(s)
		
		if(len(potential_winners)>1):
			#Tie
			flag = True
			while(flag):
				flag = False

				
				## Checks for multiple ties
				for s in range(len(potential_winners)-1):
					if(self.breakTie(player_scores[potential_winners[s]], player_scores[potential_winners[s+1]])!=0):
						flag = True
						break

				## Pops out the losers
				for s in range(1,len(potential_winners)):
					#print('listt', [player_scores[p] for p in potential_winners])
					#print('candidates',potential_winners[0], potential_winners[s])
					if(self.breakTie(player_scores[potential_winners[0]], player_scores[potential_winners[s]]) == -1):
						potential_winners.pop(s)
						break
					elif(self.breakTie(player_scores[potential_winners[0]], player_scores[potential_winners[s]]) ==1):
						potential_winners.pop(0)
						break

		return [players[p][0] for p in potential_winners]		


	def breakTie(self, score1, score2):
		hand1 = [h[1] for h in score1[1]]
		hand2 = [h[1] for h in score2[1]]
		merged_hands =[hand1[i] - hand2[i] for i in range(len(hand1))]
		if score1[0] in [3,7]:
			
			if score1[0] == 3:
				hand1[-1] = 0
				hand2[-1] = 0

			for i in range(len(hand1)):
				if(merged_hands[i]>0):
					return -1
				if(merged_hands[i]<0):
					return 1
			return 0
		
		else:
			if hand1[1]> hand2[1]:
				return -1
			elif hand1[1]== hand2[1]:
				return 0
			else:
				return 1