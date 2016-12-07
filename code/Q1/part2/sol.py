with open("input.txt", "r") as f:
	s = f.read().strip().split(", ")
	s = [ (move[0], int(move[1:])) for move in s]

direction = 0
# NORTH = 0
# EAST = 1
# WEST =

print(-1%4)