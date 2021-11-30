#Pygame
import sys
import pygame
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0
offset = 65
#screen  = pygame.display.set_mode(size)
#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()
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
		self.columns = columns
		self.cubes = [[Cube(self.sudokuBoard[i][j], i, j, width, height) for j in range(columns)] for i in range(rows)] 
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
			if ii % 3 == 0:
				thickness = 4
			else: 
				thickness =  1

			#Modification to give edges and make it look cleaner
			pygame.draw.line(win, (0,0,0), (offset, ii*gap_distance+offset), (self.width  + offset, ii *gap_distance + offset), thickness)
			pygame.draw.line(win, (0,0,0), (ii * gap_distance + offset , offset), (ii* gap_distance + offset, self.height + offset), thickness)
		

		for i in range(self.rows):
			for j in range(self.columns):
				self.cubes[i][j].draw(win)
			#Original to the size of the board
			#pygame.draw.line(win, (0,0,0), (0, ii*gap_distance), (self.width, ii *gap_distance), thickness)
			#pygame.draw.line(win, (0,0,0), (ii * gap_distance, 0), (ii* gap_distance, self.height), thickness)
	   		#pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)
	   		#Apparently this is where the cubes are drawn?

	   	#for i in range(self.rows):
	   	#	for j in range(self.columns):
	   	#		self.cubes[i][j].draw(win)
	
	def get_square(self, position):
	   	#print(position)
	   	gap_distance = self.width/9

	   	#Returns the indexes of the squares
	   	if position[0]  < self.width + offset and position[1] < self.height + offset:
	   		x = (position[0] - offset) // gap_distance
	   		y = (position[1] - offset) // gap_distance
	   		
	   		if x >= 0 and y >= 0:
	   			#print (x,y)
	   			return (x,y)

	   	

	def select(self, column, row):
		for i in range(self.rows):
			for j in range(self.columns):
				self.cubes[i][j].selected = False

		#print("row = ", row)
		#print("Column = ", column)
		xrow = int(row)
		ycol = int(column)
		if xrow >=0 and ycol >= 0 :
			self.cubes[xrow][ycol].selected = True
			self.selected = (xrow, ycol)
		#self.cubes[row][column].selected = True
	   	#self.selected = (row,column)



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
		x = self.column * gap + 65
		y = self.row * gap + 65

		if self.temp != 0 and self.value ==0:
			text = fnt.render(str(self.temp),1,(128,128,128))
			win.blit(text, (x+5), (y+5))
		elif not(self.value == 0):
			text = fnt.render(str(self.value),1,(0,0,0))
			win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

		if self.selected:
			rect = pygame.draw.rect(win, (255,0,0), (x,y,gap,gap),width = 3)
			#rect.fill((255,0,0))
			#win.fill((0,0,0))

class Button:

    def __init__(self, pushed, xpos,ypos, width, height):
        self.pushed = False
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

    def press_button(self):
        self.pushed = True

    def print_button(self,win):
   		pygame.draw.rect(win, (57,115,115),(self.xpos, self.ypos, self.width, self.height), width = 4)



def redraw_window(win,board,time,strikes):
		win.fill((200,200,200))
		#win.blit(text, (540 - 160, 560))
		#board.draw(win)	


			



def main():
	#print()
	win = pygame.display.set_mode((630,700))
	win.fill((200,200,200))
	#win.blit(text, (540 - 160, 560))
	pygame.display.set_caption("Jon's Sudoku GUI")
	sudokuBoard = Grid(9,9,500,500)
	#print("Before Loop")
	solve_button = Button(False,400,600,165,50)
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			sudokuBoard.draw_board(win)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				square = sudokuBoard.get_square(position)
				if square != None:
					sudokuBoard.select(square[0],square[1])

			#pygame.draw.rect(win, (255,0,0),(600, 600, 30, 30), width = 2)
			#print_button(solve_button,win, 550, 600)
			redraw_window(win,1,1,1)
			#pygame.draw.rect(win, (255,0,0),(600, 600, 30, 30), width = 2)
			solve_button.print_button(win)



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
