from matrix import *
from readfile import *
from simplex import *

def main():
    num_rest, num_var = readSizes()
    matrix = initMatrix(num_rest, num_var)
    readInputMatrix(matrix, num_rest, num_var)

    simplex = Simplex(matrix, num_rest, num_var)
    
    nonPos = simplex.checkForNonPositiveBs()
    if len(nonPos) == 0:
        simplex.run()
        return

    aux_num_var, aux_num_rest, aux = simplex.createAuxMatrix()
    aux_simplex = Simplex(aux, aux_num_rest, aux_num_var)
    
    for line in nonPos:
        divideLine(aux_simplex.matrix, int(line), -1)

    for line in aux_simplex.matrix[1:]:
        line_copy = np.copy(line)
        line_copy = np.multiply(line_copy,-1)
        sumLines(aux_simplex.matrix, line_copy, 0)

    aux_simplex.run('no-print')
    
    if not np.isclose(aux_simplex.getTotal(), 0):
        print("inviavel")
        printArray(aux_simplex.getCertificate())
        return

    aux_sol = aux_simplex.getCurrentSolution()

    orig_c = simplex.getCandAux()
    aux_simplex.matrix[aux_simplex.cstart[0]:aux_simplex.cend[0]+1, aux_simplex.cstart[1]:aux_simplex.cend[1]+1] = orig_c

    col_to_remove = []
    start = num_rest + num_var + num_rest
    for i in range(start, start + num_rest):
        col_to_remove.append(i)
    
    aux_simplex.matrix = np.delete(aux_simplex.matrix, col_to_remove, axis=1)
    aux_simplex.resetVero()

    idx = 0
    for x in aux_sol:
        if x > 0:
            col = aux_simplex.num_rest + idx
            line = 0
            idx_line = 1
            for i in aux_simplex.matrix[1:, col]:
                if i == 1:
                    line = idx_line
                    break
                idx_line += 1

            pivoting(aux_simplex.matrix, line, col)    

        idx += 1

    final_simplex = Simplex(aux_simplex.matrix, num_rest, num_var)
    final_simplex.run()

main()