with open("input.txt", "r") as f:
	s = f.readlines()
	s = [map(int, line.strip().split()) for line in s]

print(s)

counter = 0

n = len(s)
for j in range(3):
	for i in range(0, n-2, 3):
		a = s[i][j]
		b = s[i+1][j]
		c = s[i+2][j]
		if a+b > c and a+c > b and b+c > a:
				counter += 1

print(counter)