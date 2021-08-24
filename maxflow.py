import simplex
import numpy as np

class MaxFlow:
    def __init__(self, num_vertices, num_edges, edge_weights, incid_matrix):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.edge_weights = edge_weights
        self.incid_matrix = incid_matrix
    
    def create_simplex_matrix(self):
        pass