with open("input.txt", "r") as f:
	s = f.read().strip().split(", ")
	s = [ (move[0], int(move[1:])) for move in s]

# print(s)

current = "N"
x = 0
y = 0

for move in s:
	direction = move[0]
	steps = move[1]
	
	if current == "N":
		if direction == "L":
			current = "W"
		if direction == "R":
			current = "E"
	
	elif current == "S":
		if direction == "L":
			current = "E"
		if direction == "R":
			current = "W"
	
	elif current == "E":
		if direction == "L":
			current = "N"
		if direction == "R":
			current = "S"

	elif current == "W":
		if direction == "L":
			current = "S"
		if direction == "R":
			current = "N"

	if current == "N":
		y += steps
	if current == "S":
		y -= steps
	if current == "E":
		x += steps
	if current == "W":
		x -= steps

blocks = abs(x) + abs(y)
# print(x, y)
print(blocks)		