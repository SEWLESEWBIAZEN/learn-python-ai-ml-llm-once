import numpy as np

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def invert_matrix(matrix):
    return np.linalg.inv(matrix)
def dot_product(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

add_matrices_result = add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
subtract_matrices_result = subtract_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
multiply_matrices_result = multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
transpose_matrix_result = transpose_matrix([[1, 2], [3, 4]])
invert_matrix_result = invert_matrix([[1, 2], [3, 4]])
dot_product_result = dot_product([[1, 2], [3, 4]], [[5, 6], [7, 8]])

print("Addition Result:\n", add_matrices_result)
print("Subtraction Result:\n", subtract_matrices_result)
print("Multiplication Result:\n", multiply_matrices_result)
print("Transpose Result:\n", transpose_matrix_result)
print("Inverse Result:\n", invert_matrix_result)
print("Dot Product Result:\n", dot_product_result)
print("Matrix Calculator Operations Completed Successfully.")