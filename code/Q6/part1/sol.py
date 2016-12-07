with open("input.txt") as f:
	msg = f.readlines()
	msg = [line.strip() for line in msg]

r = len(msg)
c = len(msg[0])

print(r, c)
print(msg)

ans = ""

for j in range(c):
	freq = [0 for a in range(26)]
	for i in range(r):
		ch = ord(msg[i][j])-97
		freq[ch] += 1
	index = 0
	for i in range(26):
		if freq[i] > freq[index]:
			index = i
	ans += chr(index+97)

print(ans)