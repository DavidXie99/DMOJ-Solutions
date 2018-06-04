#Input optimization
from sys import stdin
raw_input= stdin.readline

"""
Solution involves precalculations using a modified
sieve to count number of unique prime divisors
"""

#Set up modified sieve array with
#   divisibility by two precalculated
array=[(i-1)%2 for i in xrange(10000001)]

#Modified sieve
for x in xrange(3,10000001,2):
    if array[x]==0:
        for y in xrange(x,10000001,x):
            array[y]+=1

#Output
for j in xrange(1,int(raw_input())+1):
    a,b,k=map(int,raw_input().split())
    tot=0
    for o in xrange(a,b+1):
        if array[o]==k:
            tot+=1
    print "Case #"+str(j)+":",tot
