import hashlib

doorid = "abc"
i = -1
ans = ""

for j in range(8):
	while True:
		# print(i)
		i += 1
		s = doorid+str(i)
		md5hash = hashlib.md5(s).hexdigest()

		if md5hash.startswith("00000"):
			ans += md5hash[5]
			# print(md5hash)
			break 
	print("digit " + str(j) + " found")
print(ans)