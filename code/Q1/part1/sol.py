with open("input.txt", "r") as f:
	moves = f.read().strip().split(", ")
	moves = [ (move[0], int(move[1:])) for move in moves]

x = 0
y = 0
current = 0 # current direction
# NORTH = 0, EAST = 1
# WEST = 2, SOUTH = 4

for move in moves:
	direction = move[0]
	steps = move[1]

	if direction == "L":
		current  = ( current-1 )% 4
	if direction == "R":
		current  = ( current+1 )% 4

	if current == 0: # NORTH
		for i in range(steps):
			y += 1
	if current == 1: # EAST
		for i in range(steps):
			x += 1
	if current == 2: # SOUTH
		for i in range(steps):
			y -= 1
	if current == 3: # WEST
		for i in range(steps):
			x -= 1


blocks = abs(x) + abs(y)
print(blocks)
					