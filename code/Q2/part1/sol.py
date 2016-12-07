with open("input.txt") as f:
	inst = f.readlines()
	inst = [line.strip() for line in inst]

# print(len(inst)) 
# print(inst)

num = {}
num[(0, 0)] = "1" 
num[(0, 1)] = "2"
num[(0, 2)] = "3"
num[(1, 0)] = "4"
num[(1, 1)] = "5"
num[(1, 2)] = "6"
num[(2, 0)] = "7"
num[(2, 1)] = "8"
num[(2, 2)] = "9"

state = (1,1)

def stateProcess(mstate, x, y):
	nx = mstate[0]+x
	ny = mstate[1]+y
	if 0 <= nx <= 2 and 0 <= ny <= 2:
		return (nx, ny)
	return mstate

def process(state, line):
	for dire in line:
		if dire == "U":
			state = stateProcess(state, -1, 0)
		if dire == "R":
			state = stateProcess(state, 0, 1)
		if dire == "D":
			state = stateProcess(state, 1, 0)
		if dire == "L":
			state = stateProcess(state, 0, -1)
		# print(num[state])
	return state
1
code = ""
for line in inst:
	state = process(state, line)
	# print("NUMBER: " + num[state])
	code += num[state]
print(code)