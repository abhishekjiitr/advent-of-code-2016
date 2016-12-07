with open("input.txt") as f:
	inst = f.readlines()
	inst = [line.strip() for line in inst]

# print(len(inst)) 
# print(inst)

num = {}
num[(0, 2)] = "1"
num[(1, 1)] = "2"
num[(1, 2)] = "3"
num[(1, 3)] = "4"
num[(2, 0)] = "5"
num[(2, 1)] = "6"
num[(2, 2)] = "7"
num[(2, 3)] = "8"
num[(2, 4)] = "9" 
num[(3, 1)] = "A"
num[(3, 2)] = "B" 
num[(3, 3)] = "C" 
num[(4, 2)] = "D"

state = (2, 0)

def stateProcess(mstate, x, y):
	nx = mstate[0]+x
	ny = mstate[1]+y
	if   ny < 0 or nx < 0 or nx > 4 or ny > 4 or (nx == 0 and not ny == 2) or (nx == 4 and not ny == 2) or (not nx == 2 and ny == 0) or (not nx == 2 and  ny == 4):
		return mstate 
	return (nx, ny)
	
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
	return state

code = ""
for line in inst:
	state = process(state, line)
	code += num[state]
print(code)