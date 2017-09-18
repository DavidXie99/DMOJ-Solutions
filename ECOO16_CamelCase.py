from sys import stdin
from bisect import bisect                                                               #importing functions required for binary search
raw_input=stdin.readline                                                                #input optimization

def camel(start,string,dic,lens,prev,left):                                             #defining recursive function
    if start in prev:
        return prev[start]
    m=999999
    for x in xrange(bisect(lens,left)):                                                 #binary search comparing number of letters left in word and lengths array
        if string[start:start+lens[x]] in dic:
            m=min(1+camel(start+lens[x],string,dic,lens,prev,left-lens[x]),m)
    prev[start]=m 
    return m

dic=set()
lens=set()
dicadd=dic.add
lensadd=lens.add

for x in xrange(int(raw_input())):
  a=raw_input().strip()
  dicadd(a)
  lensadd(len(a))                                                                       #word dictionary length <=2*10^5, unique string lengths likely to be
                                                                                        #exponentially smaller
lens=list(lens)
lens.sort()



for y in xrange(10):
  string=raw_input().strip()                                                            #remove endline character in input
  prev={len(string):0}                                                                  #defining and initializing prev dictionary
  print camel(0,string,dic,lens,prev,len(string))-1
