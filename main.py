from matrix import *
from readfile import *

def main():
    num_rest, num_var = readSizes()
    matrix = initMatrix(num_rest, num_var)
    readInputMatrix(matrix, num_rest, num_var)
    print(matrix)

main()