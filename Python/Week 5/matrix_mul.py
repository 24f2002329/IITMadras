# matrix multiplication using numpy
import numpy
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,1],[6,2,3],[4,2,1]]

X = numpy.matrix(A)
Y = numpy.matrix(B)
C = X*Y
print("Matrix from numpy: \n",C)

# ------------------------------------------------------------------------------------

# matrix multiplication using functions

# initialize matrix to zero
# we need to consider two matrices A and B
# we need to find the dot product of the two lists
# we need to pick the i_th row and j_th column in the matrix
# Asumming both the matrices to be the square matrices

def initialize_matrix(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C
 +
def dot_product(u: list,v: list):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans += (u[i]*v[i])
    return ans

def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l

def column(M,j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l

def matrix_mul(A,B):
    dim = len(A)     # Provided A and B always square matrices
    C = initialize_matrix(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i),column(B,j))
    return C

print("Matrix using Functions: \n",matrix_mul(A,B))

# ------------------------------------------------------------------------------------