import time
import tkinter
from tkinter import font

"""The n queens puzzle."""
class NQueens:
	"""Generate all valid solutions for the n queens puzzle"""
	def __init__(self, size, how_to_show, delay):
		# Store the puzzle (problem) size and the number of valid solutions
		self.root = tkinter.Tk()
		self.frame = tkinter.Frame(self.root, height=640, width=640)
		self.frame.pack()
		self.queen_font = font.Font(family='Helvetica', size=10, weight='bold')
		self.size = size
		self.delay = delay
		self.how_to_show = how_to_show
		self.board = self.built_chess_board()
		self.solutions = 0
		self.solve()

	def solve(self):
		"""Solve the n queens puzzle and print the number of solutions"""
		positions = [-1] * self.size
		self.put_queen(positions, 0)
		print("Found", self.solutions, "solutions.")

	def put_queen(self, positions, target_row):
		"""
		Try to place a queen on target_row by checking all N possible cases.
		If a valid place is found the function calls itself trying to place a queen
		on the next row until all N queens are placed on the NxN board.
		"""
		# Base (stop) case - all N rows are occupied
		if target_row == self.size:
			self.select(self.how_to_show, positions)
			self.solutions += 1
		else:
			# For all N columns positions try to place a queen
			for column in range(self.size):
				# Reject all invalid positions
				if self.check_place(positions, target_row, column):
					positions[target_row] = column
					self.put_queen(positions, target_row + 1)

	def check_place(self, positions, ocuppied_rows, column):
		"""
		Check if a given position is under attack from any of
		the previously placed queens (check column and diagonal positions)
		"""
		for i in range(ocuppied_rows):
			if positions[i] == column or \
				positions[i] - i == column - ocuppied_rows or \
				positions[i] + i == column + ocuppied_rows:

				return False
		return True

	def show_just_number(self, positions):
		pass

	def show_short_board(self, positions):
		"""
		Show the queens positions on the board in compressed form,
		each number represent the occupied column position in the corresponding row.
		"""
		line = ""
		for i in range(self.size):
			line += str(positions[i]) + " "
		print(line)
		time.sleep(self.delay)

	def show_full_board(self, positions):
		"""Show the full NxN board"""
		for row in range(self.size):
			line = ""
			for column in range(self.size):
				if positions[row] == column:
					line += "Q "
				else:
					line += ". "
			print(line)
		print("\n")
		time.sleep(self.delay)

	def show_graphical_board(self, positions):
		for row, i in zip(self.board, range(self.size)):
			for column, j in zip(row, range(self.size)):
				if column == "W":
					if positions[i] == j:
						b = tkinter.Button(self.frame, text = "♛", fg = "black", bg = "white", state = "disabled", height = 2, width = 2, font = self.queen_font)
						b.grid(row = i, column = j)
					else:
						b = tkinter.Button(self.frame, bg = "white", state = "disabled", height = 2, width = 2, font = self.queen_font)
						b.grid(row = i, column = j)
				elif column == "B":
					if positions[i] == j:
						b = tkinter.Button(self.frame, text = "♕", fg = "white", bg = "black", state = "disabled", height = 2, width = 2, font = self.queen_font)
						b.grid(row = i, column = j)
					else:
						b = tkinter.Button(self.frame, bg = "black", state = "disabled", height = 2, width = 2, font = self.queen_font)
						b.grid(row = i, column = j)
		self.root.update()
		time.sleep(self.delay)

	def built_chess_board(self):
		board = [["BW"[(i+j+self.size%2+1) % 2] for i in range(self.size)] for j in range(self.size)]
		return board

	def select(self, how_to_show, positions):
		switcher = {
			1: self.show_just_number,
			2: self.show_short_board,
			3: self.show_full_board,
			4: self.show_graphical_board
		}
		func = switcher.get(how_to_show, "Nothing")
		return func(positions)

def main():
	"""Initialize and solve the n queens puzzle"""
	size = 0
	while not size > 0:
		size = int(input("What is your board size (>0)? "))
	how_to_show = 0
	while not how_to_show in range(1,5):
		how_to_show = int(input("How do you want see the result?\n"
								"1- See how possible solutions.\n"
								"2- See Queen's Place every step.\n"
								"3- See Queen's Place in CommandLine as Marix\n"
								"4- See Queen's Place in GUI\n"))
	delay = -1
	while not delay >= 0:
		delay = int(input("How many time i should wait per each step (>=0)? "))
	NQueens(size, how_to_show, delay)

if __name__ == "__main__":
	# execute only if run as a script
	main()
