from readfile_simplex import printArray, printNumber
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
        self.astart = [1, num_rest]
        self.aend = [num_rest, self.total[1] - 1]
        self.vmstart = [1,0]
        self.vmend = [num_rest, num_rest - 1]

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
            return -1, selected_column

        return pivot_line, selected_column

    def getCurrentSolution(self):
        solution = np.zeros((0))
        for j in range(self.cstart[1], self.cend[1] + 1):
            if self.matrix[0][j] == 0:
                sol, _ = self.getVariableValue(j)
                solution = np.append(solution, sol)
            else:
                solution = np.append(solution, 0)
        
        return solution

    def getVariableValue(self, column_j):
        column = self.matrix[1:, column_j]
        one_line_i = 0
        index = 1
        for item in column:
            if item != 0 and item != 1:
                return 0, 0
            if item == 1:
                if one_line_i == 0:
                    one_line_i = index
                    index += 1
                    continue
                else:
                    return 0, 0
            index += 1
        
        return self.matrix[one_line_i, self.total[1]], one_line_i

    def checkForNonPositiveBs(self):
        nonPositve = []
        for i in range(self.bstart[0], self.bend[0] + 1):
            if (self.matrix[i][self.total[1]] < 0):
                nonPositve = np.append(nonPositve, i)
        
        return nonPositve

    def createAuxMatrix(self):
        aux = self.matrix[self.bstart[0]:self.bend[0]+1, self.cstart[1]:self.cend[1]+self.num_rest+1]
        zer = np.zeros((1, self.num_var + self.num_rest))
        aux = np.concatenate((zer, aux))

        ones = np.full((1, self.num_rest), 1)
        id = np.identity(self.num_rest)
        id = np.concatenate((ones,id))

        aux = np.concatenate((aux,id),axis=1)

        b = self.matrix[self.bstart[0]-1:self.bend[0]+1, self.bstart[1]:self.bend[1]+1]
        aux = np.concatenate((aux, b), axis=1)

        id = np.identity(self.num_rest)
        zer = np.zeros((1, self.num_rest))
        id = np.concatenate((zer, id))

        aux = np.concatenate((id, aux), axis=1)

        num_var = self.num_var + self.num_rest
        num_rest = self.num_rest

        return num_var, num_rest, aux

    def getUnboundedCertificate(self, column):
        c_column = column - self.num_rest
        d = np.zeros(self.num_var + self.num_rest)
        d[c_column] = 1

        idx = 0
        for j in range(self.cstart[1], self.cend[1] + 1):
            if idx == c_column:
                idx += 1
                continue

            if self.matrix[0][j] == 0:
                _, one_line_i = self.getVariableValue(j)
                val = self.matrix[one_line_i][column] * -1
                d[idx] = val
            else:
                d[idx] = 0

            idx += 1
        
        d = d[:self.num_var]
        printArray(d)
        return d


    def resetVero(self):
        for j in range(self.verostart[1], self.veroend[1]+1):
            self.matrix[0][j] = 0

    def multiplyVero(self, factor):
        for j in range(self.verostart[1], self.veroend[1]+1):
            self.matrix[0][j] = self.matrix[0][j] * factor

    def getCandAux(self):
        aux = self.matrix[self.cstart[0]:self.cend[0]+1, self.cstart[1]:self.cend[1] + self.num_rest + 1]
        return aux

    def getCertificate(self):
        return self.matrix[self.verostart[0]:self.veroend[0]+1, self.verostart[1]:self.veroend[1]+1][0]

    def getA(self):
        return self.matrix[self.astart[0]:self.aend[0]+1, self.astart[1]:self.aend[1]+1]
    
    def getB(self):
        return self.matrix[self.bstart[0]:self.bend[0]+1, self.bstart[1]]

    def getC(self):
        return self.matrix[self.cstart[0]:self.cend[0]+1, self.cstart[1]:self.cend[1]+1][0]
    
    def getTotal(self):
        return self.matrix[self.total[0]][self.total[1]]

    def getVero(self):
        return self.matrix[self.vmstart[0]:self.vmend[0]+1, self.vmstart[1]:self.vmend[1]+1]

    def getAllC(self):
        return self.matrix[self.cstart[0]:self.cend[0]+1, self.cstart[1]:self.cend[1] + self.num_rest + 1][0]

    def printMatrix(self):
        print_slack_form(self.getVero(), self.getCertificate(), self.getA(), self.getB(), self.getAllC(), self.getTotal())

    def run(self, printType = 'print'):
        if self.checkIfCIsPositive():
            if printType == 'print':
                print('otima')
                printNumber(self.getTotal())
                printArray(self.getCurrentSolution())
                printArray(self.getCertificate())
            return
        
        pivot_line, pivot_column = self.selectPivot()
        if pivot_line == -1:
            if printType == 'print':
                print("ilimitada")
                printArray(self.getCurrentSolution())
                self.getUnboundedCertificate(pivot_column)
            return

        pivoting(self.matrix, pivot_line, pivot_column)

        self.run(printType)
                    

