def readSizes():
    sizes = input().split()
    num_rest = int(sizes[0])
    num_var = int(sizes[1])

    return num_rest, num_var

def readInputMatrix(matrix, num_rest, num_var):
    start = num_rest

    c_vector = input().split()
    index = 0

    # filling C
    for i in range(start, num_var + start):
        curr = c_vector[index]
        index += 1
        matrix[0][i] = -1 * int(curr)

    # adding restriction as well as aux variables
    one_index = 0
    for i in range(1, num_rest+1):
        rest = input().split()
        for k in range(0, len(rest)):
            rest[k] = int(rest[k])

        bi = rest[num_var]
        rest.pop()
        
        for k in range(0, num_rest):
            if (k == one_index):
                rest.append(1)
            else:
                rest.append(0)
        
        one_index += 1
        rest.append(bi)

        rest_index = 0
        for j in range(num_rest, num_var + num_rest + num_rest + 1):
            matrix[i][j] = rest[rest_index]
            rest_index += 1

def printArray(arr):
    for item in arr:
        print( ('%f' % round(item, 7)).rstrip('0').rstrip('.'), end=" ")
    print()

def printNumber(num):
    print( ('%f' % round(num, 7)).rstrip('0').rstrip('.'), end=" ")
    print()