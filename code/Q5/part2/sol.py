import hashlib

doorid = "reyedfim"
i = -1
ans = [ "x" for i in range(8)]

count = 0
while count < 8:
	i += 1
	s = doorid+str(i)
	md5hash = hashlib.md5(s).hexdigest()

	if md5hash.startswith("00000"):
		digit = md5hash[6]
		pos = ord(md5hash[5])-48
		if 0 <= pos < 8 and ans[pos] == 'x':
			ans[pos] = digit
			count += 1
			print("digit " + str(pos) + " found: " + digit)

print("".join(ans))