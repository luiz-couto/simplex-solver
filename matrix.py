import numpy as np

def initMatrix(num_rest, num_var):
    matrix = np.zeros((1 + num_rest, num_rest + num_var + 1))
    index_of_one = 0

    for i in range(1, num_rest + 1):
        for j in range(0, num_rest):
            if j == index_of_one:
                matrix[i][j] = 1
                index_of_one += 1
                break;
