matrix=[]
row=int(input("Enter the rows:"))
col=int(input("Enter the col"))
for i in range(row):
    row=[]
    for j in range(col):
        ele=input(f"input the element({i+1},{j+1}):")
        row.append(ele)
    matrix.append(row)

transposeofmatrix=[[matrix[j][i] for j in range (len(matrix))] for i in range(len(matrix[0]))]
print(matrix)
print(transposeofmatrix)