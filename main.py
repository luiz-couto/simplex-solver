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
        divideLine(simplex.matrix, int(line), -1)

    aux_num_var, aux_num_rest, aux = simplex.createAuxMatrix()
    aux_simplex = Simplex(aux, aux_num_rest, aux_num_var)
    aux_simplex.run()

main()