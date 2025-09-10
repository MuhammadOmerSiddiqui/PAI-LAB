rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
matrix = []
matrix2 = []
result = []
print("Enter Values for 1 matrix:")
for i in range(0,rows):
    temp_list = []
    for j in range(0,columns):
        temp_list.append(int(input(f"Enter Value for row {i+1} and column {j+1}:")))
    matrix.append(temp_list)

print("Enter Values for 2 matrix:")
for i in range(0,rows):
    temp_list = []
    for j in range(0,columns):
        temp_list.append(int(input(f"Enter Value for row {i+1} and column {j+1}:")))
    matrix2.append(temp_list)

print("Matrix 1 Before Operation:")
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[i][j],"\t",end="")
    print()

print("Matrix 2 Before Operation:")
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix2[i][j],"\t",end="")
    print()

for i in range(0,rows):
    temp_list = []
    for j in range(0,columns):
        temp_list.append(matrix[i][j]+matrix2[i][j])
    result.append(temp_list)

print("Result After Addition:")
for i in range(0,rows):
    for j in range(0,columns):
        print(result[i][j],"\t",end="")
    print()