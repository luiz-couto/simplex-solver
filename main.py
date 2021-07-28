from matrix import *
from readfile import *
from simplex import *

def main():
    num_rest, num_var = readSizes()
    matrix = initMatrix(num_rest, num_var)
    readInputMatrix(matrix, num_rest, num_var)
    print(matrix)

    simplex = Simplex(matrix, num_rest, num_var)
    
    nonPos = simplex.checkForNonPositiveBs()
    if len(nonPos) == 0:
        simplex.run()
        return

    for line in nonPos:
        divideLine(simplex.matrix, line, -1)

    print(simplex.matrix)

main()