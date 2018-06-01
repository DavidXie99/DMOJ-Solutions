#Modulus constant
mod = 10**9

#Matrix multiplication
def matrixMult(A,B):
	return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod,
                 (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
                [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod,
                 (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]]

#Fast matrix exponentiation,
    #using the matrix fibonacci principle
def fib(n):
	if n == 1:
		return [[1,1],[1,0]]
	A = fib(n//2)
	AA = matrixMult(A,A)
	if n%2:
		AA = matrixMult(AA,[[1,1],[1,0]])
	return AA

#Input
a,b,n = map(int,raw_input().split())

"""
Generalization of fibonacci sequence is done through
multiplying original 1,1 based fibonacci matrix
with a matrix describing the modified sequence
"""
if n:
	print matrixMult([[b,a],[a,b-a]],fib(n))[0][1]
else:
	print a
