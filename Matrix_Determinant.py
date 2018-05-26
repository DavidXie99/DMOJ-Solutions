##Input optimisation
from sys import stdin
raw_input = stdin.readline

##Inputs
n = int(raw_input())
matrix = [map(int,raw_input().split()) for i in xrange(n)]

##Global variables to be used later
mod = 1000000007
rows = [i for i in xrange(n)]       #array used for matrix row indexing

"""
These variables need to be kept track of separately
in order to take advantage of modulus properties
(without running into precision errors along the way)
and the guarantee that the answer will be an integer
"""
swaps = 0                           #keeps track of number of occurences of operations that require negating final answer
                                        #ie row-swaps, column-swaps, negations
ans = 1                             #final answer
div = 1                             #divisor variable

#Performing row operations to arrive to a triangular form
for row in xrange(n):
	rownum = rows[row]

        """
	Row swapping process for when the entry at the important diagonal index
        (ie matrix[i][i], 0<=i<=n, n= number of rows)
	is equal to 0. For example:
	[[0,2,1],
	 [0,0,6],
	 [4,5,6]]
	A matrix row indexing array is used to avoid copying entire rows but
        rather swapping the order in which they are processed
        Reduces (worst case) time complexity of row swapping from O(n^2) to O(n)
        Memory complexity increase of this method is O(n)
	"""
	if not matrix[rownum][row]:                         
		counter = row
		while counter < n:                          #Finds row at which the value
			if matrix[rows[counter]][row]:
				break
			counter +=1
			
		if counter == n:                            #This implies that in the triangular form, there exists
			ans = 0                             #a 0 in the diagonal, meaning the determinant is 0 regardless
			break
		    
		temp = rows[counter]                        #performs row-swap  
		rows[counter] = rownum
		rows[row] = temp
		
		rownum = temp
		swaps +=1
		
	m1 = matrix[rownum][row]

	"""
        Performs row operations on subsequent rows
        based on scalar ratios of the value in the column concerned
        """
	for j in xrange(row+1,n):
	    
		if matrix[rows[j]][row]:
			multiple = matrix[rows[j]][row]
			for i in xrange(row,n):
                                ##Taking advantage of modulus properties
				matrix[rows[j]][i]=(((matrix[rows[j]][i]*m1)%mod-
                                                     (multiple*matrix[rownum][i])%mod)+mod)%mod
			if m1<0:
				swaps +=1 
			div *=abs(m1)
			div%=mod
#Only performs the following operations if the answer is not 0
    #(this is to reduce number of unnecessary operations)
if ans:
        #Processing answer, using modulus properties to avoid
        #overflow and decrease number of operations
	for i in xrange(n):
		ans*= abs(matrix[rows[i]][i])
		if matrix[rows[i]][i]<0:
			swaps +=1
		ans%= mod
	
	ans%= mod
	div = pow(div,mod-2,mod)
	ans *= div
	ans %= mod
	
	#Checks if answer needs to be negated
	if swaps%2:
		ans*= -1
print ans%mod
