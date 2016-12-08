with open("input.txt") as f:
	s = f.readlines()
	s = [line.strip() for line in s]

r = 6
c = 50

grid = [ [0 for j in range(c)] for i in range(r) ]

def printgrid():
	for i in range(r):
		for j in range(c):
			if grid[i][j] == 0:
				grid[i][j] = " "
			else:
				grid[i][j] = "*"
	for i in range(r):
			print(" ".join(grid[i]))
	print("")
def rotatecolumn(y):
	global grid
	temp = grid[r-1][y]
	for i in range(r):
		grid[r-i-1][y] = grid[r-i-2][y]
	grid[0][y] = temp

def rotaterow(x):
	global grid
	temp = grid[x][c-1]
	for j in range(c):
		grid[x][c-1-j] = grid[x][c-2-j]
	grid[x][0] = temp

for inst in s:
	parts = inst.split()	
	n = len(parts)

	if n == 2:
		# light up
		A, B = list(map(int, parts[1].split("x")))
		for i in range(B):
			for j in range(A):
				grid[i][j] = 1
	else:
		# rotate
		by = int(parts[n-1])
		info = int(parts[2].split("=")[1])
		if parts[1] == "column":
			y = info
			by = by % r
			for i in range(by):
				rotatecolumn(y)
		else:
			x = info
			by = by % c
			for j in range(by):
				rotaterow(x)

l = [sum(grid[i]) for i in range(r)]
print("total lit pixels: " + str(sum(l)) + "\n")
printgrid()