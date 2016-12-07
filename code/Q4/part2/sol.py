import re

with open("input.txt") as f:
	info = f.readlines()
	info = [line.strip() for line in info]

# print(info)
names = []
def rotate(name, delta):
	ans = ""
	for pname in name:
		for ch in pname:
			ascii = ord(ch)-97
			ascii = (ascii+delta) % 26 + 97
			ans += chr(ascii)
		ans += " "
	return ans.strip()

for line in info:
	parts = line.split("-")
	name, rest = parts[:len(parts)-1], parts[len(parts)-1]
	roomid = int(rest.split("[")[0])
	match = re.search(r"\[(.*)\]", rest)
	checksum = match.group(1)
	
	s = ""
	for pname in name:
		s += pname
	
	s = sorted(s)
	freq = []
	for i in range(26):
		ascii = 97+i
		c = chr(ascii)
		count = s.count(c)
		freq.append((count, c))
	freq = sorted(freq, key = lambda x : x[1])
	freq = sorted(freq, key = lambda x : x[0], reverse = True)

	# print(freq)
	mychecksum = ""
	for f in freq:
		if f[0]:
			mychecksum += f[1]
	mychecksum = mychecksum[:5]
	# print(mychecksum)

	name = rotate(name, roomid % 26)
	if checksum == mychecksum:
		# print(name, roomid)
		names.append((name, roomid))

names.sort()
for name in names:
	if name[0] == "northpole object storage":
		print(name)