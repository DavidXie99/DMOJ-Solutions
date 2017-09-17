from sys import stdin
from heapq import heappush,heappop          #importing optimal datastructure & relevant functions
raw_input=stdin.readline                    #input optimization

v = int(raw_input())

adj = [[] for i in xrange(v+1)]             #adjacency arraylist initialization
times = [999999999 for i in xrange(v+1)]    #distance/time array initialization
prevnode = [-1 for i in xrange(v+1)]        #node tracking array initialization

for i in xrange(int(raw_input())):
    a,b,dist,spd = map(int,raw_input().split())
    time = dist/float(spd)
    adj[a].append([b,time])                 #appending the connection node b and the corresponding distance/time to adjacency arraylist at index a
    adj[b].append([a,time])                 #repeat for opposite direction (all paths are bidirectional)

q = []
heappush(q,(0,1))                           #initializing heap array and adding origin point and distance/time
times[1] = 0

while len(q):                               #standard bfs, djikstra variance
    t,c = heappop(q)
    for i in adj[c]:
        if times[i[0]]>t+i[1]:
            prevnode[i[0]]=c                #track (optimal) pathway
            times[i[0]]=t+i[1]
            heappush(q,(times[i[0]],i[0]))
            
n = v 
blimp = -1
while n != -1:                              #reiterate through (optimal) pathway to determine length of pathway and number of blimps needed
    blimp += 1
    n = prevnode[n]

print blimp
print int(round(times[v]*20,0))
