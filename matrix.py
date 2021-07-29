import numpy as np

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
    newLine = np.array([])
    for j in range(0, len(matrix[line_i])):
        newLine = np.append(newLine, matrix[line_i][j] * scalar)
    return newLine

def divideLine(matrix, line_i, scalar):
    for j in range(0, len(matrix[line_i])):
        matrix[line_i][j] = matrix[line_i][j] / scalar

def pivoting(matrix, line_i, column_j):
    elem = matrix[line_i, column_j]
    divideLine(matrix, line_i, elem)
    elem = matrix[line_i, column_j]

    for i in range(0, len(matrix)):
        selected = matrix[i][column_j]
        if i == line_i or selected == 0:
            continue
        factor = -selected/elem
        line = multiplyLineAndReturn(matrix, line_i, factor)
        sumLines(matrix, line, i)


def print_slack_form(vero, certificate, A, b, c, v):
    for j in range(len(certificate)):
        print('{:4}'.format(round(certificate[j],2)), end=" ")
    
    print('{:4}'.format(""), end="")
    
    for j in range(len(c)):
        print('{:4}'.format(round(c[j],2)), end=" ")
    print('{:4}'.format("="), end=" ")
    
    print('{:4}'.format(round(v,2)), end="")
    
    print()
    for j in range((len(certificate) + len(c))*2 + 2):
        print("---", end="")
    print()

    for i in range(A.shape[0]):
        for j in range(vero.shape[1]):
            print('{:4}'.format(round(vero[i][j],2)), end=" ")
        print('{:4}'.format(""), end="")
        for j in range(A.shape[1]):
            print('{:4}'.format(round(A[i][j],2)), end=" ")
        print('{:4}'.format("="), end=" ")
        print('{:4}'.format(round(b[i],2)))
    
    print()
    print()