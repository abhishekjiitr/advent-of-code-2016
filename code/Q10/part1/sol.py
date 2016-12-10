with open("input.txt", "r") as f:
	s = f.readlines()
	s = [line.strip() for line in s]

ans = -1
index = -1

# print(s)

MAX = 300	
BOT = [list() for i in range(MAX)]    # stores current chips in bots
rules = [list() for i in range(MAX)]  # stores the rules i.e. where to put its low and high chips
OUTPUT = [list() for i in range(MAX)] # stores output

for line in s:
	parts = line.split()
	# print(parts)
	bot = -1
	if parts[0] == 'value':
		bot = int(parts[len(parts)-1])
		val = int(parts[1])
		BOT[bot].append(val)
	else:
		bot = int(parts[1])
		lo = int(parts[6])
		hi = int(parts[len(parts)-1])
		t1 = parts[5]			      # for low, BOT or OUTPUT
		t2 = parts[10]				  # for high, BOT or OUTPUT
		rules[bot].append(lo)
		rules[bot].append(hi)
		if t1 == "output":
			rules[bot].append(1)
		else:
			rules[bot].append(0)
		if t2 == "output":
			rules[bot].append(1)
		else:
			rules[bot].append(0)
def check(): # check for bot with 2 chips
	global index
	global BOT
	for i, val in enumerate(BOT):
		if len(val) > 1:
			index = i  	# if found update index to point to this bot
			return
	index = -1    		# indicate no such bot found

def process(i):			# process bot with 2 chips, i is index of that bot
	global rules, ans, BOT
	mybot = BOT[i]
	mybot.sort()
	lo_val = mybot[0]
	hi_val = mybot[1]
	if lo_val == 17 and hi_val == 61:
		ans = i
	lo = rules[i][0]
	hi = rules[i][1]
	BOT[i] = []
	if rules[i][2]:						# if low chip given to OUTPUT
		OUTPUT[lo].append(lo_val)
	else:								# if given to other BOT
		BOT[lo].append(lo_val)
		if len(BOT[lo]) > 1:			# if target bot has 2 chips process it too
			process(lo)

	if rules[i][3]:						# if high chip given to OUTPUT
		OUTPUT[hi].append(hi_val)
	else:								# if given to other BOT
		BOT[hi].append(hi_val)
		if len(BOT[hi]) > 1:			# if target bot has 2 chips process it too
			process(hi)
while True:			# Loop	while there remains a bot with 2 chips
	check()			
	if index < 0:   # if no bot found break loop
		break
	process(index)  # process that bot

print(ans)	
print(OUTPUT[0][0] * OUTPUT[1][0] * OUTPUT[2][0])