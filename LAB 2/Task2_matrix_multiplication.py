rows = int(input("Enter the number of rows for 1 matrix:"))
columns = int(input("Enter the number of columns for 1 matrix:"))
rows2 = int(input("Enter the number of rows for 2 matrix:"))
columns2 = int(input("Enter the number of columns for 2 matrix:"))
while(columns!=rows2):
    print("Columns for 1 matrix must be equal to rows of 2 matrix! Enter Again:")
    columns = int(input("Enter the number of columns for 1 matrix:"))
    rows2 = int(input("Enter the number of rows for 2 matrix:"))
matrix = []
matrix2 = []
result_matrix = []
print("Enter Values for 1 matrix:")
for i in range(0,rows):
    temp_list = []
    for j in range(0,columns):
        temp_list.append(int(input(f"Enter Value for row {i+1} and column {j+1}:")))
    matrix.append(temp_list)

print("Enter Values for 2 matrix:")
for i in range(0,rows2):
    temp_list = []
    for j in range(0,columns2):
        temp_list.append(int(input(f"Enter Value for row {i+1} and column {j+1}:")))
    matrix2.append(temp_list)

print("Matrix 1 Before Operation:")
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[i][j],"\t",end="")
    print()

print("Matrix 2 Before Operation:")
for i in range(0,rows2):
    for j in range(0,columns2):
        print(matrix2[i][j],"\t",end="")
    print()

for i in range(0,rows):
    temp_list = [] 
    for j in range(0,columns2):
        result = 0
        for k in range(0,columns):
            result += matrix[i][k]*matrix2[k][j]
        temp_list.append(result)
    result_matrix.append(temp_list)

print("Result After Multiplication:")
for i in range(0,rows):
    for j in range(0,columns2):
        print(result_matrix[i][j],"\t",end="")
    print()