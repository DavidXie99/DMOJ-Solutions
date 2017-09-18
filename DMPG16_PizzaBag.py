from math import log 
n,k = map(int,raw_input().split())
sli = map(int,raw_input().split())
sli = ([0 for crap in xrange(k)])+sli+sli[:k]
jj = int(log(k,2))
array = [[0 for i in xrange(n+2*k)] for j in xrange(jj+1)]
array[0] = list(sli)

for i in xrange(1,n+2*k):
    array[0][i]+=array[0][i-1]
array[0] = array[0][::-1]
lel=[0 for l in xrange(jj+1)]

if len(lel)>1:
    lel[1]=1 
    for l in xrange(1,jj+1):
        lel[l]+=lel[l-1]*2
        
for j in xrange(1,jj+1):
    lm = lel[j]
    for i in xrange(n+k+k-lm):
        array[j][i]=min(array[j-1][i],array[j-1][i+lm])
        
comp = bin(k)[2:][::-1]
diff = max(0,k-(2**jj))+1
val = [array[0][o]-min(array[jj][o],array[jj][o+diff]) for o in xrange(n+k)]

print max(val)
