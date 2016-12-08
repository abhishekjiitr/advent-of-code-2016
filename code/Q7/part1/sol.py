import re
with open("input.txt") as f:
	s = f.readlines()
	s = [line.strip() for line in s]

# print(s)

def ABBA(s):
	n = len(s)
	for i in range(n-3):
		if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
			return True
	return False

def check(tuples):
	for s in tuples:
		if ABBA(s):
			return True
	return False

ip = 0

for line in s:
	# print(line)
	tuples = re.findall(r'\[(\w+)\]', line)
	tuples2 = re.sub(r'\[(\w+)\]', r' ',line).split()
	
	if check(tuples2) and not check(tuples):
		ip += 1

print(ip)