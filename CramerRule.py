
import numpy as np
from scipy import linalg

#linalg.det determinant of a mat
#linalg.inv inverse of a mat
#linalg.pinv calculate pseudo inverse




#user input of matrix size
x = input("enter number of rows: \n")
y = input("enter number of columns: \n")
rows = int(x)
columns = int(y)

#resizing matrix to required size
A_LEs = np.zeros((rows, columns))

#intialising the matrix
print("Please initialise the matrix\n")
for i in range(rows):
    print("enter row number "+str(i+1)+": \n")
    for j in range(columns):
        A_LEs[i][j] = input()

#splitting coefficient mat and constant mat
A_const = np.zeros((rows, 1))
for i in range(rows):
    A_const[i][0] = A_LEs[i][columns-1]

A_Coeffs = np.zeros((rows, columns-1))
for i in range (rows):
    for j in range (columns-1):
        A_Coeffs[i][j] = A_LEs[i][j]

print(A_LEs)
print(A_Coeffs)
print(A_const)

#checking if matrix is invertible

#definition of a swap function for columns
def Swap(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]

detA_Coeffs = np.linalg.det(A_Coeffs)
print("coeffeicient matrix determinant: "+str(detA_Coeffs)+"\n")
if detA_Coeffs == 0:
    print("matrix is not invertible, cant compute solution")
else:
    #extracting determinant N from temp where it holds D_n matrix
    temp = A_LEs
    for i in range(columns-1):
        Swap(temp, i, -1)
        A_detn = A_Coeffs
        for j in range (rows):
            A_detn[j][i] = temp[j][i]
        print("solution for variable: "+str(i+1))
        detA_n = np.linalg.det(A_detn)

        #iffy on this 
        if i%2 != 0:
            detA_n *= -1

        solution_n = detA_n/detA_Coeffs
        print(str(solution_n))
