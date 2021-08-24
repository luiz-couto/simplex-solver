import numpy as np
from matrix import *
from simplex import *

def main():
    # read file
    sizes = input().split()
    num_vertices = int(sizes[0])
    num_edges = int(sizes[1])

    weigths = input().split()

    incid_matrix = np.empty((num_vertices, num_edges)) 
    for i in range(num_vertices):
        line = input().split()
        for j in range(num_edges):
            incid_matrix[i][j] = line[j]
    
    print(incid_matrix)


if __name__ == "__main__":
    main()