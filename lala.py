states={0:"Western Australia", 1:"Northern Territory", 2:"South Australia", 3:"Queensland", 4:"New South Wales", 5:"Victoria", 6:"Tasmania"}
graph={0:[1,2], 1:[0,2,3], 2:[0,1,3,4,5], 3:[1,2,4], 4:[2,3,5], 5:[2,4], 6:[]}
colors=["Red", "Green", "Blue"]
n=0
col_graph={}

def check(state, colour):
	global graph
	global col_graph
	for i in graph[state]:
		if i in col_graph and col_graph[i]==colour:
			return False
	return True

def assign(state, colour):
	global col_graph
	col_graph[state]=colour

n=0
i=0
while n<7:
	assigned=0
	for i in range(3):
		if check(n,i)==True:
			assign(n,i)
			n+=1
			assigned=1
			break
	if assigned==0:
		prevas=0
		for x in range(3):
			if check(n-1, (col_graph[n-1]+1)%3)==True:
				assign(n,(col_graph[n-1]+1)%3)
				prevas=1
				break
		if prevas==0:
			n-=1

for key, value in col_graph.items():
	print(states[key] + " : " + colors[value])
