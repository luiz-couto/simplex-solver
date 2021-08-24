import numpy as np
from matrix import *
from simplex import *
import maxflow

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
    
    
    # creating and running max flow
    max_flow = maxflow.MaxFlow(num_vertices, num_edges, weigths, incid_matrix)
    max_flow.run()


if __name__ == "__main__":
    main()