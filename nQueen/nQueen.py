#!/usr/bin/python3

class nQueen():
	def __init__(self):
		self.count = 0

	def canFit(self,arena,size,row,col):
		for i in range(size):
			if (arena[row][i] == 'Q'):
				return False

		for j in range(size):
			if (arena[j][col] == 'Q'):
				return False

		x_pos,y_pos = row,col

		while (x_pos>=0 and y_pos>=0):
			if (arena[x_pos][y_pos] == 'Q'):
				return False
			x_pos -=1
			y_pos -=1

		x_pos,y_pos = row,col

		while (x_pos>=0 and y_pos<size):
			if (arena[x_pos][y_pos] == 'Q'):
				return False
			x_pos -=1
			y_pos +=1

		return True


	def solve(self,arena,size,row):
		if (row == size):
			self.count +=1
			for i in range(size):
				print(list(map(str,arena[i])))
			print()
			return

		for col in range(size):
			if (self.canFit(arena,size,row,col)):
				arena[row][col] = 'Q'
				if self.solve(arena,size,row+1):
					return True
				arena[row][col] = 0
		return False



def main():
	n = int(input("nQueen Size?"))
	arena = [[0 for i in range(n)] for j in range(n)]
	queen = nQueen()
	queen.solve(arena,n,0)
	print(queen.count)


if __name__ == '__main__':
	main()
