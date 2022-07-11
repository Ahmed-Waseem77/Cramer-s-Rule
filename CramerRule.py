
import numpy as np
from scipy import linalg

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

#checking if matrix is invertible
detA_Coeffs = np.linalg.det(A_Coeffs)
print("coeffeicient matrix determinant: "+str(detA_Coeffs)+"\n")
if detA_Coeffs == 0:
    print("matrix is not invertible, cant compute solution")

#if det is not zero compute determinants for each Dx, Dy, .. Dn
else:
    #double loop to replace A_detn columns with constant column

    for i in range(columns-1):
        A_detn = np.copy(A_Coeffs)
        for j in range(rows):
            A_detn[j][i] = A_const[j][0]

        #finding and printing solutions
        print("solution for variable: "+str(i+1))
        detA_n = np.linalg.det(A_detn)
        print(A_detn)

        solution_n = detA_n/detA_Coeffs
        print(str(solution_n))
