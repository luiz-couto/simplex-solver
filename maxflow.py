from simplex import *
import numpy as np

class MaxFlow:
    def __init__(self, num_vertices, num_edges, edge_weights, incid_matrix):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.edge_weights = edge_weights
        self.incid_matrix = incid_matrix
    
    def create_simplex_matrix(self):
        # Incid. Matrix without s and t
        matrix = self.incid_matrix[1:self.num_vertices-1, 0:self.num_edges + 1]

        # C vector
        s = self.incid_matrix[0]
        c = np.zeros((1, self.num_edges))
        for i in range (len(s)):
            if int(s[i]) == -1:
                c[0][i] = -1

        matrix = np.concatenate((c, matrix))
        
        # B vector
        b_size = 1 + self.num_vertices - 2 + self.num_edges
        b = np.zeros((1, b_size))

        w_idx = 0
        for i in range(self.num_vertices-1, self.num_vertices-1 + self.num_edges):
            b[0][i] = self.edge_weights[w_idx]
            w_idx += 1
        
        # Identity matrix below
        id = np.identity(self.num_edges)
        matrix = np.concatenate((matrix, id))
        
        # VERO
        vero_size = self.num_vertices - 2 + self.num_edges
        
        zeros = np.zeros((1, vero_size))
        vero = np.identity(vero_size)
        vero = np.concatenate((zeros, vero))

        matrix = np.concatenate((vero, matrix), axis=1)

        # Adding B to matrix
        matrix = np.concatenate((matrix, b.T), axis=1)

        return matrix

    def run(self):
        matrix = self.create_simplex_matrix()
        num_rest = self.num_vertices - 2 + self.num_edges
        num_var = self.num_edges

        simplex = Simplex(matrix, num_rest, num_var, has_slack_variables=False)
        simplex.run(printType='maxflow')