with open("input.txt", "r") as f:
	s = f.readlines()
	s = [map(int, line.strip().split()) for line in s]

print(s)

counter = 0

for t in s:
	a = t[0]
	b = t[1]
	c = t[2]
	if a+b > c and a+c > b and b+c > a:
		counter += 1

print(counter)