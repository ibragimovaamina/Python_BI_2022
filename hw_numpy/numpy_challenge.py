import numpy as np

if __name__ == "__main__":
    # Creating an array from a list(the first way):
    array1 = np.array([6, 6, 6])
    # Creating an array with arange (the second way):
    array2 = np.arange(6)
    # Creating an array of zeros (the third way):
    array3 = np.zeros(6)
    

# This function computes matrix multiplication of 2 matrices
def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

# This function checks whether multiple matrices can be multiplied
def multiplication_check(*matrices):
    for i in range(len(matrices) - 1):
        if matrices[i].shape[1] != matrices[i+1].shape[0]:
            return False
    return True

# This function computes matrix multiplication of several matrices (if possible)
def multiply_matrices(*matrices):
    if multiplication_check(*matrices):
        return np.linalg.multi_dot(matrices)
    else:
        return None
    
# This function computes distance between 2 point in 2-dimensional space     
def compute_2d_distance(array1, array2):
    return np.linalg.norm(array2 - array1)

# This function computes distance between 2 point in multidimensional space        
def compute_multidimensional_distance(array1, array2):
    return np.linalg.norm(array2 - array1)

# This function computes matrix of pair distances between rows of input matrix
def compute_pair_distances(matrix):
    dim = matrix.shape[0] # amount of rows in input matrix
    pair_distances = np.zeros((dim, dim))
    for n_row in range(dim):
        for n_col in range(dim):
            if n_row != n_col: # filling matrix of pair distances
                pair_distances[n_row, n_col] = np.linalg.norm(matrix[n_row] - matrix[n_col])
    return pair_distances
