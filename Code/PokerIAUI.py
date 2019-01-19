import pygame

pygame.init()
screen_width = 800
screen_height = 600
card_scaling_factor = 0.75
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("comicsansms", 36)
font2 = pygame.font.SysFont("comicsansms", 30)
font3 = pygame.font.SysFont("comicsansms", 20)
game_header = font.render("POKERIA a poker game", True, (220,20,60))
table_name = font3.render("Mesa :42", True,(220,20,60))
table_game = font3.render("Jogo :42", True,(220,20,60))
bet_value = font2.render("Valor apostado = 123412", True,(220,20,60))
table_value = font2.render("Valor na mesa = 123412", True,(220,20,60))
card_blank = pygame.image.load('cardBack_blue1.png')
card_blank = pygame.transform.scale(card_blank, (int(card_blank.get_width()*card_scaling_factor),int(card_blank.get_height()*card_scaling_factor)))

def render_cards(cards):
	
	card_spacing = 20
	center = len(cards) * card_blank.get_width() + 4*card_spacing
	dx = (screen.get_width() -center)/2
	dy = screen_height/10*2
	
	for card in cards:
		screen.blit(card_blank, (dx, dy))
		dx += card_blank.get_width() + card_spacing

def render_table_name():
	dx =(screen_width-game_header.get_width())/20*15 
	dy = screen_height/10*0.01
	x_spacing = 30

	screen.blit(table_name, (dx,dy))
	dx += x_spacing + table_name.get_width()
	screen.blit(table_game, (dx,dy))


def render_stats():
	
	dx =(screen_width-game_header.get_width())/10
	dy = screen_height/10*5
	x_spacing = 30
	
	screen.blit(bet_value, (dx,dy))
	dx += x_spacing + bet_value.get_width()
	screen.blit(table_value, (dx,dy))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((50,205,50))
        screen.blit(game_header, (((screen_width-game_header.get_width())/2, screen_height/20))) 
        render_cards([1,2,3,4,5])
        render_stats()
        render_table_name()
        pygame.display.flip()
        clock.tick(60)