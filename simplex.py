import numpy as np
from matrix import *

class Simplex:
    def __init__(self, matrix, num_rest, num_var):
        self.matrix = matrix
        self.num_rest = num_rest
        self.num_var = num_var
        self.num_lines = num_rest + 1
        self.num_columns = num_rest + num_var + num_rest + 1
        self.verostart = [0, 0]
        self.veroend = [0, num_rest - 1]
        self.cstart = [0, num_rest]
        self.cend = [0, num_rest + num_var - 1]
        self.total = [0, num_rest + num_var + num_rest]
        self.bstart = [1, self.total[1]]
        self.bend = [num_rest, self.total[1]]

    def checkIfCIsPositive(self):
        c = self.matrix[self.cstart[0]:self.cend[0]+1, self.cstart[1]:self.total[1]]
        for item in c[0]:
            if item < 0:
                return False
        
        return True

    def selectPivot(self):
        selected_column = 0
        for c in range(self.cstart[1], self.total[1]):
            if self.matrix[0][c] < 0:
                selected_column = c
                break

        min_ratio = 1000
        pivot_line = 0
        for i in range(1, self.num_lines):
            if self.matrix[i][selected_column] > 0 and self.matrix[i,self.total[1]]/self.matrix[i][selected_column] < min_ratio:
                min_ratio = self.matrix[i,self.total[1]]/self.matrix[i][selected_column]
                pivot_line = i
        
        if pivot_line == 0:
            return -1, -1

        return pivot_line, selected_column

    def getCurrentSolution(self):
        solution = np.zeros((0))
        for j in range(self.cstart[1], self.cend[1] + 1):
            if self.matrix[0][j] == 0:
                solution = np.append(solution, self.getVariableValue(j))
            else:
                solution = np.append(solution, 0)
        
        return solution

    def getVariableValue(self, column_j):
        column = self.matrix[1:, column_j]
        one_line_i = 0
        index = 1
        for item in column:
            if item != 0 and item != 1:
                return 0
            if item == 1:
                if one_line_i == 0:
                    one_line_i = index
                    index += 1
                    continue
                else:
                    return 0
            index += 1
        
        return self.matrix[one_line_i, self.total[1]]

    def run(self):
        if self.checkIfCIsPositive():
            np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
            print(self.getCurrentSolution())
            print(self.matrix)
            return
        
        pivot_line, pivot_column = self.selectPivot()
        if pivot_line == -1:
            print("Ilimitada")
            return

        pivoting(self.matrix, pivot_line, pivot_column)

        self.run()
                    

