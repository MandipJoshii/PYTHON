import numpy as np

plot_1 = np.array(
    [
        [1,2],
        [3,4]
    ]
    )

plot_2 = np.array(
    [
        [5,6],
        [7,8]
    ]
)
print("<-------------------------DOT & MATMUL--------------------------------------->")
plot_dot = np.dot(plot_1,plot_2)
matrix_multiply = np.matmul(plot_1,plot_2)


print(plot_dot) #strickly made to work with 1D(1 DIMENTIONAL) array but can also work in 2D
print(matrix_multiply) #strickly made to work with 2D array and cannot work on 1D

print("<-------------------------INVERSE & DETERMINATION--------------------------------------->")

inverse = np.linalg.inv(plot_1)

print(inverse) # yo watch this to know how to find inverse -> https://youtube.com/shorts/kmbgfE-7NHY?si=p5bzTObyqadfkOPc

detemination = np.linalg.det(plot_2)

print(detemination)


print("<-------------------------EIGEN VALUE AND VECTOR & SINGULAR VALUE DECOMPOSITION------------------------------------->")


# tomorrow
# task solve a eigen, inverse, determination, 
# np.linalg.svd(A) → Singular Value Decomposition.
# Breaks a matrix into three parts: U, S, Vt.
# Useful in compression (like image compression).

# A = np.array([[1, 2],
#               [3, 4]])

# eigvals, eigvecs = np.linalg.eig(A)
# print("Eigenvalues:", eigvals)
# print("Eigenvectors:\n", eigvecs)

# U, S, Vt = np.linalg.svd(A)
# print("U:\n", U)
# print("S:", S)
# print("Vt:\n", Vt)

for_eigen = np.array([
    [8,-3,8],
    [-3,8,-3],
    [8,-3,8]
])
eigen_value, eigen_vector = np.linalg.eig(for_eigen)

print("EIGEN VALUE = ",eigen_value)
print("EIGEN VECTOR = ",eigen_vector)






# np.linalg.norm()

# Finds the norm (length or magnitude) of a vector or matrix.

# ✅ Example:

# v = np.array([3, 4])
# print(np.linalg.norm(v))    length of vector (3,4)


# 👉 Output:

# 5.0    (like Pythagoras: sqrt(3^2 + 4^2))







# np.linalg.solve()

# Solves a system of linear equations of the form:
# Ax = b

# ✅ Example:
# Suppose we want to solve:

# 2x + y = 5
# x + 3y = 6


# Matrix form:

# A = [[2, 1],
#      [1, 3]]

# b = [5, 6]


# Code:

# A = np.array([[2, 1],
#               [1, 3]])
# b = np.array([5, 6])

# x = np.linalg.solve(A, b)
# print(x)