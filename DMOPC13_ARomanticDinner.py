#Solution method is an extrapolation of the 1D knapsack problem
#Reduces number of dimensions required by 1
#Original memory requirement U*M*R
#Solution saves large amounts of memory, and is slightly more time efficient

m,u,r = map(int,raw_input().split())

dp = [[0 for i in xrange(u+1)] for j in xrange(m+1)]                        #Initialize 2D dp array

for x in xrange(r):
    val,t,f = map(int,raw_input().split())
    for i in xrange(m, t-1, -1):
        for j in xrange(u, f-1, -1):                                        #Iterate backwards to avoid overlap
            dp[i][j] = max(dp[i][j], val+dp[i-t][j-f])

print dp[m][u]
