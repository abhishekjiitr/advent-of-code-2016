with open("input.txt") as f:
	s = f.read()
	s.replace(" ", "")

n = len(s)
print(s)
i = 0

ans = ""
while i < n:
	ch = s[i]
	if ch != "(":
		ans += ch
		i += 1
	else:
		op = ""
		i += 1
		while s[i] != ')':
			op += s[i]
			i += 1
		m, times = map(int, op.split("x"))
		# print(m, times)
		i += 1
		string = s[i:i+m]
		ans += string * times
		i += m

# print(ans)
print(len(ans))