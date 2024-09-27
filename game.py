#import modules
import pygame
from pygame.locals import *

pygame.init()

height = 501
width = 501
line = 6
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')

#define colours
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 225,0)
white = (225, 225, 255)

#define font
font = pygame.font.SysFont(None, 40)

#define variables
clicked = False
player = 1
pos = (0,0)
markers = []
game_over = False
winner = 0

#setup a rectangle for "Play Again" Option
again_rect = Rect(width // 2 - 80,height // 2, 160, 50)

#create empty list representing tic-tac-toe grid 
for x in range (3):
	row = [0] * 3
	markers.append(row)

def draw_grid():
	bg = (0,0,0)
	grid = (255,255,255)
	screen.fill(bg)
	for x in range(1,3):
		pygame.draw.line(screen, grid, (0, 167 * x), (width,167 * x), line)
		pygame.draw.line(screen, grid, (167 * x, 0), (167 * x, height), line)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 167 + 45, y_pos * 167 + 45), (x_pos * 167 + 122, y_pos * 167 + 122), 30)
				pygame.draw.line(screen, red, (x_pos * 167 + 122, y_pos * 167 + 45), (x_pos * 167 + 45, y_pos * 167 + 122), 30)
			if y == -1:
				pygame.draw.circle(screen, green, (x_pos * 167 + 84, y_pos * 167 + 84), 45, 30)
			y_pos += 1
		x_pos += 1	


def check_game_over():
	global game_over
	global winner

	x_pos = 0
	for x in markers:

		#check columns for win condition
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True
			
		#check rows for win condition
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			winner = 2
			game_over = True
		x_pos += 1

	#check diagonals for win condition 
	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		winner = 2
		game_over = True

	#Check for Draw
	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		if tie == True:
			game_over = True
			winner = 0



def draw_game_over(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = font.render(end_text, True, white)
	pygame.draw.rect(screen, black, (width // 2 - 250,height // 2 - 250, 501,501))
	screen.blit(end_img, (width // 2 - 100, height // 2 - 50))

	again_text = 'Play Again?'
	again_img = font.render(again_text, True, white)
	screen.blit(again_img, (width // 2 - 80, height // 2 + 10))

run = True
while run:

	#Define Markers and Grid on Screen
	draw_grid()
	draw_markers()

	#Events Managed 
	for event in pygame.event.get():

		#Exit Game
		if event.type == pygame.QUIT:
			run = False
		if game_over == False:

			#check for Mouseclick
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // 167
				cell_y = pos[1] // 167
				if markers[cell_x][cell_y] == 0:
					markers[cell_x][cell_y] = player
					player *= -1
					check_game_over()

	#Check for Win-Case
	if game_over == True:
		draw_game_over(winner)

		#check for Mouse Input in Game Over Screen
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):

				#reset variables
				game_over = False
				player = 1
				pos = (0,0)
				markers = []
				winner = 0

				#create empty 3 x 3 list to represent the grid
				for x in range (3):
					row = [0] * 3
					markers.append(row)
	pygame.display.update()

pygame.quit()
