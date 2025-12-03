def matric_Multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    result = [[0 for i in range(cols_B)] for i in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    
    return result

A = [[1, 2, 3], [4, 5, 6]]
B = [[ 7,  8], [ 9, 10], [11, 12]]

print(matric_Multiplication(A,B))
