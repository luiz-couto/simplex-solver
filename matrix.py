import numpy as np
from numpy.matrixlib.defmatrix import matrix

def initMatrix(num_rest, num_var):
    matrix = np.zeros((1 + num_rest, num_rest + num_var + num_rest + 1))
    index_of_one = 0

    # filling VERO
    for i in range(1, num_rest + 1):
        for j in range(0, num_rest):
            if j == index_of_one:
                matrix[i][j] = 1
                index_of_one += 1
                break;

    return matrix

def sumLines(matrix, line, target_index):
    for j in range(0, len(line)):
        matrix[target_index][j] = matrix[target_index][j] + line[j]

def multiplyLineAndReturn(matrix, line_i, scalar):
    newLine = np.empty((0))
    for j in range(0, len(line_i)):
        newLine.append(matrix[line_i][j] * scalar)

def divideLine(matrix, line_i, scalar):
    for j in range(0, len(line_i)):
        matrix[line_i][j] = matrix[line_i][j] / scalar

def pivoting(matrix, line_i, column_j):
    elem = matrix[line_i, column_j]
    divideLine(matrix, line_i, elem)

    for i in range(0, len(matrix)):
        selected = matrix[i][column_j]
        factor = -selected/elem
        line = multiplyLineAndReturn(matrix, line_i, factor)
        sumLines(matrix, line, i)
