from matrix import *
from readfile import *
from simplex import *

def main():
    num_rest, num_var = readSizes()
    matrix = initMatrix(num_rest, num_var)
    readInputMatrix(matrix, num_rest, num_var)
    print(matrix)

    simplex = Simplex(matrix, num_rest, num_var)
    simplex.run()

main()