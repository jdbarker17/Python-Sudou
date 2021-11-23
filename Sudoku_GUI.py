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

class Grid: 
	sudokuBoard = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0 ],
	[6, 0, 0, 0, 7, 5, 0, 0, 9 ],
	[0, 0, 0, 6, 0, 1, 0, 7, 8 ],
	[0, 0, 7, 0, 4, 0, 2, 6, 0 ],
	[0, 0, 1, 0, 5, 0, 9, 3, 0 ],
	[9, 0, 4, 0, 6, 0, 0, 0, 5 ],
	[0, 7, 0, 3, 0, 0, 0, 1, 2 ],
	[1, 2, 0, 0, 0, 7, 4, 0, 0 ],
	[0, 4, 9, 2, 0, 6, 0, 0, 7 ]
	]


	def __init__(self, rows,columns,width,height):
		self.rows = rows
		self.colums = columns
		#self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(columns)] for i in range(rows)] 
		self.width = width
		self.height = height
		self.model = None
		self.selected = None


	def sketch(self, val):
		row = self.selected[0]
		column = self.selected[1]


	def draw_board(self, win):
		#Modification
		#gap_distance = (self.width - 100) / 9
		#Original
		gap_distance = self.width / 9
		for ii in range(self.rows + 1):
			if ii % 3 == 0 and ii != 0:
				thickness = 4
			else: 
				thickness =  1

			#Modification to give edges and make it look cleaner
			pygame.draw.line(win, (0,0,0), (50, ii*gap_distance), (self.width -50, ii *gap_distance), thickness)
			#pygame.draw.line(win, (0,0,0), (ii * gap_distance + 50 , 50), (ii* gap_distance +50, self.height + 50), thickness)
			
			#Original to the size of the board
			#pygame.draw.line(win, (0,0,0), (0, ii*gap_distance), (self.width, ii *gap_distance), thickness)
			#pygame.draw.line(win, (0,0,0), (ii * gap_distance, 0), (ii* gap_distance, self.height), thickness)
	   		#pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)



class Cube:
	rows = 9
	columns = 9

	def __init__ (self, value, row, column, width, height):
		self.value = value
		self.temp = 0
		self.row = row
		self.column = column
		self.width = width
		self.height = height
		self.selected = False

	def draw(self,win):
		fnt = pygame.font.SysFont("comicsans", 40)

		gap = self.width/9
		x = self.column * gap
		y = self.roy * gap 

		if self.temp != 0 and self.value ==0:
			text = fnt.render(str(self.temp),1,(128,128,128))
			win.blit(text, (x+5), (y+5))
		elif not(self.value == 0):
			text = fnt.render(str(self.value),1,(0,0,0))
			win.blit(text, (x + (gap/2 - text.get_width()/2, y + (gap/2 - text.get_height()/2))))

		if self.selected:
			pygame.draw.rect(win, (255,0,0), (x,y,gap,gap),3)

	def redraw_window(win,board,time,strikes):
		win.fill((255,255,255))
		win.blit(text, (540 - 160, 560))
		board.draw(win)

		
			



def main():
	#print()
	win = pygame.display.set_mode((720,800))
	win.fill((100,100,100))
	#win.blit(text, (540 - 160, 560))
	pygame.display.set_caption("Jon's Sudoku GUI")
	sudokuBoard = Grid(9,9,620,620)
	#print("Before Loop")
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			sudokuBoard.draw_board(win)
			pygame.display.update()

			position = pygame.mouse.get_pos()
			#clicked = pygame.







	#	print("In loop")

main()




#while 1:
#	for event in pygame.event.get():
#		if event.type ==pygame.QUIT: sys.exit()
#		buttons = pygame.mouse.get_pressed(num_buttons = 3)
#		#print(buttons[0])
#		pygame.mouse.set_visible(True)
#
#
#	#pygame.mouse.set_visible(True)
#	ballrect = ballrect.move(speed)
#	if ballrect.left < 0 or ballrect.right > width:
#		speed[0] = -speed[0]
#	if ballrect.top < 0 or ballrect.bottom > height:
#		speed[1] = -speed[1]
#	screen.fill(black)
#	screen.blit(ball, ballrect)
#	pygame.display.flip()
