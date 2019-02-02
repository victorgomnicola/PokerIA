import pygame
from Mesa import Mesa
from JogadorRandomico import JogadorRandomico
from LogParser import LogParser
import os
import subprocess

#inicializa tela
pygame.init()

#define propriedades da tela
screen_width = 800
screen_height = 600
card_scaling_factor = 0.75
screen = pygame.display.set_mode((screen_width, screen_height))

#clock eh a quantidade de frames renderizados por segundo
clock = pygame.time.Clock()

#flag para continuar renderizando o jogo
done = False

#Cria o titulo do jogo
pygame.display.set_caption('PorkarIA')

#####FONTS
WHITE = (225,225,225)
BLACK = (0,0,0)
font = pygame.font.SysFont("comicsansms", 36)
font2 = pygame.font.SysFont("comicsansms", 30)
font3 = pygame.font.SysFont("comicsansms", 20)


###BUTTONS 
check_button = font2.render("check", True, WHITE)
call_button = font2.render("call", True, WHITE)
fold_button = font2.render("fold", True, WHITE)
raise_string = "raise 100"
raise_button =  font2.render(raise_string, True, WHITE)

def render_button():

	button_x_spacing = 5
	button_y_spacing = 3
	button_external_spacing = 8
	dx  = screen.get_width()/30*13.5
	dy = screen_height/10*6
    
	#####CHECK BUTTON
	pygame.draw.rect(screen,(34,139,34), (dx, dy, check_button.get_width()+2*button_x_spacing, check_button.get_height()+2*button_y_spacing))
	screen.blit(check_button, (dx+button_x_spacing,dy+button_y_spacing))
	dy+=  check_button.get_height()+2*button_y_spacing + button_external_spacing
	
	#CALL BUTTON 
	x_correction_factor = (check_button.get_width() - call_button.get_width())/2
	pygame.draw.rect(screen,(34,139,34), (dx, dy, check_button.get_width()+2*button_x_spacing, check_button.get_height()+2*button_y_spacing))
	screen.blit(call_button, (dx+button_x_spacing + x_correction_factor,dy+button_y_spacing))
	dy+=  check_button.get_height()+2*button_y_spacing + button_external_spacing

	##### FOLD BUTTON 
	x_correction_factor = (check_button.get_width() - fold_button.get_width())/2
	pygame.draw.rect(screen,(34,139,34), (dx, dy, check_button.get_width()+2*button_x_spacing, check_button.get_height()+2*button_y_spacing))
	screen.blit(fold_button, (dx+button_x_spacing + x_correction_factor,dy+button_y_spacing))
	dy+=  check_button.get_height()+2*button_y_spacing + button_external_spacing + 8

	#### Raise Button 
	x_correction_factor = (check_button.get_width() - raise_button.get_width())/2
	enlarging_x_factor =  raise_button.get_width() -check_button.get_width()

	pygame.draw.rect(screen,(34,139,34), (dx- enlarging_x_factor/2, dy, raise_button.get_width() +2*button_x_spacing, check_button.get_height()+2*button_y_spacing))
	screen.blit(raise_button, (dx+button_x_spacing + x_correction_factor,dy+button_y_spacing))


def render_log(log):

	dx =  screen.get_width()/30*18.5
	dy = screen_height/10*6

	log_x = screen_width*0.35
	log_y = screen_height*0.27
	pygame.draw.rect(screen,(34,139,34), (dx, dy, log_x,log_y))

	screen.blit(log_label, (dx+int(log_x-log_label.get_width())/2, dy + 5))
	pygame.draw.line(screen, WHITE, (dx, dy + log_label.get_height()+10), (dx+log_x , dy + log_label.get_height()+10 ))

	dy+= log_label.get_height()+13
	log_spacing = 1
	
	for l in log:
		label = font3.render(l, True,WHITE)
		screen.blit(label, (dx+int(log_x-label.get_width())/2, dy))
		dy+=log_spacing+ log_label.get_height()

def render_cards(cards):
	
	k = load_card_sprite(cards[0])
	card_spacing = 20
	center = len(cards) * k.get_width() + 4*card_spacing
	dx = (screen.get_width() -center)/2
	dy = screen_height/10*1.5
	
	for card in cards:
		kard = load_card_sprite(card)
		screen.blit(kard, (dx, dy))
		dx += kard.get_width() + card_spacing

def render_player(cards):
	card_spacing = 20
	dx  = screen.get_width()/30*3
	dy = screen_height/10*6.2
	card_1 = load_card_sprite(cards[0])
	screen.blit(card_1, (dx,dy))
	card_2 = load_card_sprite(cards[1])
	dx+=card_spacing+ card_1.get_width()
	screen.blit(card_2, (dx,dy))

def render_table_name():
	dx =(screen_width-game_header.get_width())/20*15 
	dy = screen_height/10*0.01
	x_spacing = 30

	screen.blit(table_name, (dx,dy))
	dx += x_spacing + table_name.get_width()
	screen.blit(table_game, (dx,dy))


def render_stats():
	
	dx =(screen_width-game_header.get_width())/10
	dy = screen_height/10*4.3
	x_spacing = 30
	
	screen.blit(bet_value, (dx,dy))
	dx += x_spacing + bet_value.get_width()
	screen.blit(table_value, (dx,dy))

	dx = (screen_width- montante.get_width())/2
	dy = screen_height/10*5
	screen.blit(montante, (dx,dy))

def load_card_sprite(card):
	if(card == ('b',-1)):
		card_blank = pygame.image.load('./cards/card_back.png')
		card_blank = pygame.transform.scale(card_blank, (int(card_blank.get_width()*card_scaling_factor),int(card_blank.get_height()*card_scaling_factor)))
		return card_blank
	else:
		card = pygame.image.load('./cards/'+card[0]+'/'+str(card[1])+".png")
		card = pygame.transform.scale(card, (int(card.get_width()*card_scaling_factor),int(card.get_height()*card_scaling_factor)))
		return card

def render_info():
	dx = screen_width*0.2
	dy = screen_height*0.2
	render_info_size_x = screen_width*0.6
	render_info_size_y =screen_height*0.6

	pygame.draw.rect(screen, (230,230,250), (dx,dy, render_info_size_x, render_info_size_y))
	
	header_info = font3.render("Instruções de jogo", True,BLACK)
	screen.blit(header_info, (dx+ (render_info_size_x - header_info.get_width())/2,dy+10))

	dy+= 60
	dx+=10
	header_q = font3.render("Q: Para Instruções do jogo", True,BLACK)
	screen.blit(header_q, (dx,dy))
	dy+= 35
	header_c = font3.render("C: Para call", True,BLACK)
	screen.blit(header_c, (dx,dy))
	dy+= 35
	header_f = font3.render("F: Para fold", True,BLACK)
	screen.blit(header_f, (dx,dy))
	dy+= 35
	header_x = font3.render("X: Para check", True,BLACK)
	screen.blit(header_x, (dx,dy))
	dy+= 35
	header_r = font3.render("R: Para raise", True,BLACK)
	screen.blit(header_r, (dx,dy))
	dy+= 35
	header_r = font3.render("Ç: Para recomeçar", True,BLACK)
	screen.blit(header_r, (dx,dy))
	dy+= 35
	header_n = font3.render("Digite os numeros para aumentar a aposta", True,BLACK)
	screen.blit(header_n, (dx,dy))
	dy+= 35
	header_n = font3.render("Digite up or down para ver o log", True,BLACK)
	screen.blit(header_n, (dx,dy))


def render_message(message):

	dx = screen_width*0.30
	dy = screen_height*0.30
	render_info_size_x = screen_width*0.5
	render_info_size_y =screen_height*0.5
	pygame.draw.rect(screen, (230,230,250), (dx,dy, render_info_size_x, render_info_size_y))
	message_font = font.render(message, True, BLACK)
	screen.blit(message_font,(dx+ (render_info_size_x - message_font.get_width())/2,dy+render_info_size_y*0.4) )


### GAME VARIABLES
info_flag = False
log_head = 0
log_lenght = 4
clock_ticks = 0



#POKER ENGINE 
t_number = '42'
PokerEngine = subprocess.Popen(['python','main.py', t_number], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
######
#Waits for the log file to be created
while(len(os.listdir("./" + t_number))==0):
	pass
#####
logparser = LogParser("./" + t_number+"/0.txt")
game_number = 0
montante_player = 3000
table_cards = [('b',-1),('b',-1),('b',-1),('b',-1),('b',-1)]
player_cards = logparser.get_player_cards(0)
logg = logparser.read_log()
valor_mesa , valor_apostado  = logparser.get_stats()
game_over = False

##### INFORS
game_header = font.render("PorkaIA - a poker game", True, WHITE)
table_name = font3.render("Mesa :"+t_number, True,WHITE)
table_game = font3.render("Jogo :"+str(game_number), True,WHITE)
bet_value = font2.render("Valor apostado = "+str(valor_apostado), True,WHITE)
table_value = font2.render("Valor na mesa = "+str(valor_mesa), True,WHITE)
montante = font2.render("Montante: "+str(montante_player), True,WHITE)
log_label = font3.render("log das jogadas", True,WHITE)

def render_game():
	screen.fill((0,100,0))
	screen.blit(game_header, (((screen_width-game_header.get_width())/2, screen_height/20))) 
	render_cards(table_cards)
	render_player(player_cards)
	render_stats()
	render_button()
	render_table_name()
	render_log(logg[max(0,log_head):(log_head+log_lenght)])
	
	global game_over
	if(game_over):
		global logparser, game_number
		game_number += 1
		logparser = LogParser("./" + t_number +"/"+str(game_number)+".txt")
		game_over = False

def update_values():
	
	global valor_mesa , valor_apostado , table_cards, player_cards, logg, montante, montante_player, game_over
	valor_mesa , valor_apostado  = logparser.get_stats()
	table_cards = logparser.parse_cards_on_the_table()
	player_cards = logparser.get_player_cards(0)
	logg = logparser.read_log()
	game_over = logparser.game_over

def flush_action(actionn):
	global valor_mesa, valor_apostado, table_cards, player_cards, logg, montante, montante_player
	aa = actionn + "\n"
	PokerEngine.stdin.write(aa.encode())
	PokerEngine.stdin.flush()
	montante_player = int(PokerEngine.stdout.readline())
	montante = font2.render("Montante: " + str(montante_player), True, WHITE)
	valor_mesa , valor_apostado  = logparser.get_stats()
	table_cards = logparser.parse_cards_on_the_table()
	player_cards = logparser.get_player_cards(0)
	logg = logparser.read_log()

while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			####INFO
			if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				info_flag= not info_flag   
			####LOG EVENTS
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				log_head +=1
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				log_head -= 1
				log_head = max(log_head,0)  

			#### Player Events
			if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
				flush_action('0')

			if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
				flush_action('-1')

			if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				flush_action(raise_string.split(" ")[1])
			
			###NUMBERS
			if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
				raise_string = raise_string[0:-1]
				raise_button =  font2.render(raise_string, True,WHITE)  
			if event.type == pygame.KEYDOWN and event.key in [pygame.K_0,pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
				if event.key== pygame.K_0:
					raise_string += "0"
				if event.key== pygame.K_1:
					raise_string += "1"
				if event.key== pygame.K_2:
					raise_string += "2"
				if event.key== pygame.K_3:
					raise_string += "3"
				if event.key== pygame.K_4:
					raise_string += "4"
				if event.key== pygame.K_5:
					raise_string += "5"
				if event.key== pygame.K_6:
					raise_string += "6"
				if event.key== pygame.K_7:
					raise_string += "7"
				if event.key== pygame.K_8:
					raise_string += "8"
				if event.key== pygame.K_9:
					raise_string += "9"	
				raise_button = font2.render(raise_string, True,WHITE)
	

		render_game()

		if(info_flag):
			render_info()   
		
		pygame.display.flip()
		clock.tick(60)
		clock_ticks = (clock_ticks+1)%61
		
		if(clock_ticks == 60):
			update_values()