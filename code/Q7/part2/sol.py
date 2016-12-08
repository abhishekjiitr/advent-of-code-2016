import re
with open("input.txt") as f:
	s = f.readlines()
	s = [line.strip() for line in s]

SSL = 0

def process(tuples):
	# print(tuples)
	ABA = set()
	for t in tuples:
		n = len(t)
		for i in range(n-2):
			s = t[i:i+3]
			ans = ["0", "0", "0"]
			# print(s)
			ans[0] = s[1]
			ans[1] = s[0]
			ans[2] = s[1]
			ans = "".join(ans)
			# print(ans)
			ABA.add(ans)
	return ABA

for line in s:
	# print(line)
	tuples = re.findall(r'\[(\w+)\]', line)
	tuples2 = re.sub(r'\[(\w+)\]', r' ',line).split()
	print(tuples)
	print(tuples2)
	ABA = process(tuples)
	# print(ABA)
	flag = False
	for t in tuples2:
		n = len(t)
		for i in range(n-2):
			word = t[i:i+3]
			print(word)
			if word in ABA:
				flag = True
	if flag:
		SSL += 1

print(SSL)