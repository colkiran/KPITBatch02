# Q3.  Transpose of matrix, matrix can be any shape for example
#
# input
#
# 1  2  3		1  2  3
# 4  5  6		4  5  6
# 7  8  9
#
# output
#
# 1  4  7 	1  4
# 2  5  8		2  5
# 3  6  9		3  6


def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed
# here we are taking input
rows = int(input("Enter the number of rows: ")) # row
cols = int(input("Enter the number of columns: ")) # coloum

matrix = [] # making  empty matrix

print("Enter the elements of the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Original matrix:")
for row in matrix:
    print(row)

transpose= transpose(matrix)
print("Transposed matrix:")
for row in transpose:
    print(row)