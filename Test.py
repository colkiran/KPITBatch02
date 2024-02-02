mat = list()
mat = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        print(mat[i][j],end=" ")
    print("\n")
print ('**********Transposed matrix**********')
for i in range(3):
    for j in range(3):
        print(mat[j][i],end=" ")
    print("\n")