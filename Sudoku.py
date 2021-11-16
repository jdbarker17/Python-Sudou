# Jons Python Project Practice
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
#print(sudokuBoard[1])

zero_locations = []
def print_board(array):
	for ii in range(0, len(array)):
		print(array[ii])

def find_zero_locations(array):
	zero_locations_index = 0
	#zero_locations = []
	for ii in range(0, len(array)):
		for jj in range(0 , len(array[ii])):
			if array[ii][jj] == 0:
			
				zero_locations.append([ii,jj])

def reset_zeros(sudoku_array):
		for ii in range(0, len(zero_locations)):
			index1 = zero_locations[ii][0]
			index2 = zero_locations[ii][1]
			sudoku_array[index1][index2] = 0

def place(board,pos,val):
	board[pos[0]][pos[1]] = val

def check_position(board,pos, val):

		#Check Rows
		for ii in range(0,len(board)):
			#if board[pos[0]][ii] == board[pos[0]][pos[1]] & ii != pos[0]:
			if board[pos[0]][ii] == val:
			#if val == board[pos[0]][pos[1]] & ii != pos[1]:
				print("Invalid solution - Row")
				return -1 


		for ii in range(0,len(board)):
			#if board[pos[0]][ii] == board[pos[0]][pos[1]] & ii != pos[0]:
			if board[ii][pos[1]] == val:
			#if val == board[pos[0]][pos[1]] & ii != pos[1]:
				print("Invalid solution - Column")
				return -1 

		#Square Checks

		#Square 1
		if pos[0] < 3 & pos[1] < 3:
			for ii in range(0,3):
				for jj in range(0,3):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 


		#Square 2
		if  pos[0] < 3 & pos[1] > 2 & pos[1] <  6:
			for ii in range(0,3):
				for jj in range(3,6):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 

		#Square 3
		if  pos[0] < 3 & pos[1] > 5:
			for ii in range(0,3):
				for jj in range(6,9):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 

		#Square 4
		if pos[0] > 2 & pos[0] <  6 & pos[1] < 3:
			for ii in range(3,6):
				for jj in range(0,3):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 

		#Square 5
		if pos[0] > 2 & pos[0] <  6 & pos[1] > 2 & pos[1] <  6:
			for ii in range(3,6):
				for jj in range(3,6):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 

		#Square 6
		if pos[0] > 2 & pos[0] <  6 & pos[1] > 5:
			for ii in range(3,6):
				for jj in range(6,9):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 
		
		#Square 7
		if pos[0] > 5 & pos[1] < 3:
			for ii in range(6,9):
				for jj in range(0,3):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 

		#Square 8
		if pos[0] > 5 & pos[1] > 2 & pos[1] <  6:
			for ii in range(6,9):
				for jj in range(3,6):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 

		#Square 9
		if pos[0] > 5 & pos[1] > 5:
			for ii in range(6,9):
				for jj in range(6,9):
					if board[ii][jj] ==  val:
						print("Invalid solution - Box")
						return -1 
		else:
			print("Valid Option")
			return 1

def find_empty(sudokuBoard):
	for ii in range(0, len(sudokuBoard)):
		for jj in range(0,len(sudokuBoard)):
			if sudokuBoard[ii][jj] == 0:
				return [ii,jj]

def solve(sudokuBoard, zero_locations):
	zero_loc = find_empty(sudokuBoard)
	if not zero_loc:
		return True
	else:
		zero_loc = find_empty(sudokuBoard)
		#if 
		for number in range(1,10):
			if check_position(sudokuBoard,zero_loc, number) == 1:
				place(sudokuBoard,zero_loc,number)
				print_board(sudokuBoard)
			#else:
				if solve(sudokuBoard,zero_locations):
					return True
			
			place(sudokuBoard,zero_loc,0) 

		return False
	



def main():
	#print_board(sudokuBoard)
	find_zero_locations(sudokuBoard)
	#reset_zeros(sudokuBoard)

	print_board(sudokuBoard)
	#place(sudokuBoard,[1,1], 100)
	#check_position(sudokuBoard,[7,2],8)
	solve(sudokuBoard,zero_locations)
	#print_board(sudokuBoard)
	#check_position()


main()
