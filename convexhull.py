from sys import stdin
from collections import deque
from sys import setrecursionlimit
setrecursionlimit(100000)
raw_input=stdin.readline
k,n,m=map(int,raw_input().split())
adj=[[] for i in xrange(n+1)]
path=[[] for i in xrange(n+1)]
dist=[99999999999 for i in xrange(n+1)]
hull=[300 for i in xrange(n+1)]
for i in xrange(m):
  x,y,d,m=map(int,raw_input().split())
  adj[x]+=[[y,d,m]]
  adj[y]+=[[x,d,m]]
a,b=map(int,raw_input().split())
hull[a]=0
dist[a]=0
path[a]=[a]
q=deque()
app=q.append
pp=q.popleft
app(a)
while len(q):
  c=pp()
  for i in adj[c]:
    if dist[i[0]]>dist[c]+i[1]:
      if hull[c]+i[2]<k:
        dist[i[0]]=dist[c]+i[1]
        hull[i[0]]=hull[c]+i[2]
        path[i[0]]=path[c]+[i[0]]
        app(i[0])
if dist[b]!=99999999999:
  print dist[b]
else:
    def isthisdfs(paths,adj,dmg,dist,node,prev):
      ind=(node,dmg,dist)
      if ind in prev:
        return prev[ind]
      if node==b:
        prev[ind]=dist
        return dist
      dl=9999999999
      for i in adj[node]:
        if i[0] not in paths:
          if i[2]+dmg<k:
            if dist+i[1]<dl:
              paths.add(i[0])
              dl=min(dl,isthisdfs(paths,adj,dmg+i[2],dist+i[1],i[0],prev))
              paths.remove(i[0])
      prev[ind]=dl
      return prev[ind]
    prev={}
    bb=isthisdfs({a},adj,0,0,a,prev)
    if bb==9999999999:
      print -1
    else:
      print bb
