#Input optimization
from sys import stdin
raw_input = stdin.readline

n = int(raw_input())

#Initializing adjacency array (node numbering starts at 1)
adj = [[] for i in xrange(n+1)] 

#Inputs for tree (into adjacency array)
for i in xrange(n-1):
	a,b = map(int,raw_input().strip().split())
	adj[a]+=[b]
	adj[b]+=[a]
	
"""
Root the tree at an arbitrary node
@the first node with more than one connection
or default to node 1 (in a two node tree)
"""
root = 1
for i in xrange(n+1):
	if len(adj[i]) > 1:
		root = i
		break

"""  
Initialize dictionary for tracking number of ways
to form a certain cyclical pathway of length L-1
"""
cycles={1:1}

"""
Recursive (dfs) function to find longest path and
number of ways to form that path

prev represents previous node (0 if there are none) used to avoid
    repeating paths (travelling upstream the tree if you will)
root represents current node (breaks down task of larger tree
    into subtasks of smaller trees, rooted at current node)

output of the function comes in tuples (l,p)
where l is the maximum length of the task/subtask tree
and p is the number of ways to form that path
"""
def LHC(prev,root):
        #Base case at terminal node
        #or tree of two nodes
	if len(adj[root])==1:
		return (0,1)
        
	"""STAGE 1 OF PROCESSING"""
        #Tracks paths of all lengths (downstream from current node) and
        #number of ways to form those paths. Groups by lengths.
	numLengths = {}

        #Tracks (lengths,num_paths) pairs per node (maximized based on their respective subtasks)
        #similar to numLengths but avoids grouping by lengths
	perNode = []

        #Boolean dictionary to see if multiple nodes have the same (maximum) length
	repeat = {}


        #Iterates through list of nodes adjacent to current node
	for node in adj[root]:
                #avoids previous node (travelling "upstream")
		if node!=prev:
                        #recursive call
			dist,ways = LHC(root,node)
			dist += 1

			#checks if path of length dist has occurred before
			if dist in numLengths:
				numLengths[dist] += ways
				repeat[dist] = True
			else:
				numLengths[dist] = ways
				repeat[dist] = False
			#appends to perNode
			perNode+=[(dist,ways)]

        #Print statements to see results of stage 1 of processing
	"""
	print "Prev_node:",prev,", Cur_node:",root
	print "numLengths:",numLengths
	print "perNode:",perNode
	print "repeat:",repeat
        """


	"""STAGE 2 OF PROCESSING"""
	ml=-1                       #max length of potential cycle
	mways = 0                   #ways to form max length
	Y = len(perNode)            #number of adjacent nodes - 1 (no including prev node)
	Largest = max(numLengths)   #Largest "half" length ("half" of potential cycle)
	LW = numLengths[Largest]    #number of ways for Largest "half" length
	SecondLargest = 0           #Second Largest "half" length

	#Mathematical optimization when Largest == 1
        #implies that the rest of the nodes (if any) must also have max length of 1
	if Largest == 1:
		ml = 2
		if Y%2:
			mways = Y*((Y-1)/2)
		else:
			mways = (Y/2)*(Y-1)
	#otherwise
	else:
                #Case 1: Largest "half" length occurs multiple times
                #ie Second Largest == Largest
		if repeat[Largest]:
			SecondLargest = Largest

		#Case 2: More than one, non-upstream (previous) node
		elif len(numLengths)-1:
			del numLengths[Largest]
			SecondLargest = max(numLengths)
			mways = numLengths[SecondLargest]*LW

		#Case 3 (otherwise): only one, non-upstream (previous) node
		#implies Second Largest == 0, or non-existent
	        #conditional not needed as variable is initialized as 0
		
		ml = Largest + SecondLargest

		"""
                Perform O(n^2) operation for Case 1 if
                ml is the largest cycle of all seen cycles thus far
                """
		if ml>=max(cycles) and Largest == SecondLargest:
			for i in xrange(Y):
				if perNode[i][0]==Largest:
					for j in xrange(i+1,Y):
						if perNode[j][0] == Largest:
							mways += perNode[j][1]*perNode[i][1]
	#Memoization
	if ml in cycles:
		cycles[ml] += mways
	else:
		cycles[ml] = mways
	return (Largest,LW)
	
LHC(0,root)
mlen = max(cycles)
print mlen+1,cycles[mlen]
