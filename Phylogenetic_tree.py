import numpy as np

sequences=['A','B','C','D','E']
n_rows = int(input("Number of rows:"))

n_cols = int(input("Number of columns:"))

# Define the matrix

matrix = []

print("Enter the entries row-wise:",)

# for user input

for i in range(n_rows):  # A for loop for row entries

    a = []

    for j in range(n_cols):  # A for loop for column entries

        a.append(float(input()))

    matrix.append(a)
matrix = np.array(matrix)
print(matrix)
# To print the matrix




print(matrix[0])
while(len(matrix[0])>=2):#stop mergaing at two clusters
    min = 10000
    for i in range(0, n_rows, 1):
        for j in range(0, n_cols, 1):
            distance = matrix[i][j]

            if (distance <= min and distance != 0):
                min = matrix[i][j]
                index_i = i
                index_j = j
    print(min, index_i, index_j)
    print('merge cluster', index_j, "int ", index_i)
    print(matrix)
    for i in range(len(matrix[0])):
        if i != index_i and i != index_j:
            matrix[i][index_j] = float((matrix[index_j][i] + matrix[index_i][i]) / 2)
            matrix[index_j][i] = float((matrix[index_j][i] + matrix[index_i][i]) / 2 ) # calculate avg
    matrix = np.delete(matrix, index_i, 0)
    matrix = np.delete(matrix, index_i, 1)
    n_cols-=1
    n_rows -= 1
    print(matrix)
