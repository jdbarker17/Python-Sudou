#Pygame
import sys
import pygame
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

screen  = pygame.display.set_mode(size)
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
#pygame.mouse.set_visible(True)


def __init__(self, rows,columns,width,height):
	self.rows = rows
	self.colums = columns
	self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)] 
	self.width = width
    self.height = height
    self.model = None
    self.selected = None


while 1:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT: sys.exit()
		buttons = pygame.mouse.get_pressed(num_buttons = 3)
		#print(buttons[0])
		pygame.mouse.set_visible(True)


	#pygame.mouse.set_visible(True)
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
