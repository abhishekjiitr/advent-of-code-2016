with open("input.txt", "r") as f:
	s = f.read().strip().split(", ")
	s = [ (move[0], int(move[1:])) for move in s]

# print(s)

current = "N"
x = 0
y = 0

visited = []
visited.append((x, y))

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

	found  = False

	if current == "N":
		for i in range(1, steps+1):
			y += 1
			if (x, y) in visited:
				found = True
				break
			visited.append((x, y))
	if current == "S":
		for i in range(1, steps+1):
			y -= 1
			if (x, y) in visited:
				found = True
				break
			visited.append((x, y))
	if current == "E":
		for i in range(1, steps+1):
			x += 1
			if (x, y) in visited:
				found = True
				break
			visited.append((x, y))
			
	if current == "W":
		for i in range(1, steps+1):
			x -= 1
			if (x, y) in visited:
				found = True
				break
			visited.append((x, y))

	if found: 
		break

blocks = abs(x) + abs(y)
# print(x, y)
print(blocks)