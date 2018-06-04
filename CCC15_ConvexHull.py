#Imports
from sys import stdin               #For input optimization
from collections import deque       #For optimal datastructures
from sys import setrecursionlimit   #To subvert python's recursion limit

#Increase recursion limit
setrecursionlimit(100000)

#Input optimization
raw_input=stdin.readline

#DFS (with memoization)
def dfs(paths,dmg,dist,node):
  #index for memoization
  ind=(node,dmg,dist)

  #memoization access
  if ind in prev:
    return prev[ind]

  #base case destination
  if node==b:
    prev[ind]=dist
    return dist
  
  """
  dfs through adjacent nodes:
    set max distance to infinity (assume destination can't be reached)
    check that the node has not been visited in this path (to avoid cycles to reduce iterations)
    check that the damage does not destroy hull
    (preemptive) check that the distance to any next node is not greater than current shortest
  """
  dl=9999999999
  for i in adj[node]:
    if i[0] not in paths:
      if i[2]+dmg<k:
        if dist+i[1]<dl:
          paths.add(i[0])
          dl=min(dl,dfs(paths,dmg+i[2],dist+i[1],i[0]))
          paths.remove(i[0])

  #memoize and return
  prev[ind]=dl
  return prev[ind]

#Inputs and data formatting (largely for BFS)
k,n,m=map(int,raw_input().split())

adj=[[] for i in xrange(n+1)]             #initialize adjacency array
dist=[99999999999 for i in xrange(n+1)]   #initialize distance value array
hull=[300 for i in xrange(n+1)]           #initialize hull value array

for i in xrange(m):
  x,y,d,m=map(int,raw_input().split())
  adj[x]+=[[y,d,m]]
  adj[y]+=[[x,d,m]]
a,b=map(int,raw_input().split())

#Set up for BFS
hull[a]=0
dist[a]=0

#initialize deque and deque optimizations
q=deque()
app=q.append
pp=q.popleft

#BFS using distance as primary heuristic,
# and damage to hull as secondary heuristic
app(a)
while len(q):
  c=pp()
  for i in adj[c]:
    if dist[i[0]]>dist[c]+i[1]:
      if hull[c]+i[2]<k:
        dist[i[0]]=dist[c]+i[1]
        hull[i[0]]=hull[c]+i[2]
        app(i[0])
if dist[b]!=99999999999:
  print dist[b]

#if result is "infinity", double check answer with DFS
else:
    prev={}
    bb=dfs({a},0,0,a)
    if bb==9999999999:
      print -1
    else:
      print bb
