import numpy as np

# =====Basic Numpy Operations====
print("-----Basic Numpy Operations-----")

# Creating a 1D array
arr = np.array([10, 20, 30, 40])
print("1D Array:", arr)

# Element-wise operations
print("Array + 5:", arr + 5)
print("Array squared:", arr ** 2)

# Mean, standard deviation
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Matrix Creation and Operations
print("\n-----Matrix Operations-----")

# Creating matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
print("A + B:\n", A + B)

# Matrix subtraction
print("A - B:\n", A - B)

# Element-wise multiplication
print("A * B (element-wise):\n", A * B)

# Matrix multiplication (dot product)
print("A @ B (matrix multiplication):\n", np.dot(A, B))

# Transpose of a matrix
print("Transpose of A:\n", A.T)

