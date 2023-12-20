from tkinter import *

def cofac(matrix):
    size = len(matrix)
    subMatrices = []

    for cof in range(0, size):
        minorMat = []
        for row in range(1, size):
            minor = []
            for col in range(0, size):
                if cof != col:
                    element = matrix[row][col]
                    minor.append(element)    
            minorMat.append(minor)
        subMatrices.append(minorMat)

    for x in subMatrices:
        for y in range(0, len(x)):
            print(x[y])
        print("")
    
    return subMatrices

def det2(matrix):
    determinant = ((matrix[0][0] * matrix[1][1]) - 
                   (matrix[0][1] * matrix[1][0]))
    return determinant

def det3(matrix):
    determinant = ((matrix[0][0] * matrix[1][1] * matrix[2][2] + 
                    matrix[0][1] * matrix[1][2] * matrix[2][0] + 
                    matrix[0][2] * matrix[1][0] * matrix[2][1]) - (
                    matrix[0][2] * matrix[1][1] * matrix[2][0] + 
                    matrix[0][1] * matrix[1][0] * matrix[2][2] + 
                    matrix[0][0] * matrix[1][2] * matrix[2][1]))
    return determinant

def det4(matrix):
    subMat = cofac(matrix)
    determinant = 0

    for mat in range(0, len(subMat)):
        major = det3(subMat[mat])    
        if mat % 2 != 0:
            major = -major
        cofactor = matrix[0][mat] * major
        determinant = determinant + cofactor
    return determinant

def det5(matrix):
    subMat = cofac(matrix)
    determinant = 0

    for mat in range(0, len(subMat)):
        major = det4(subMat[mat])    
        if mat % 2 != 0:
            major = -major
        cofactor = matrix[0][mat] * major
        determinant = determinant + cofactor
    return determinant

def det6(matrix):
    subMat = cofac(matrix)
    determinant = 0

    for mat in range(0, len(subMat)):
        major = det5(subMat[mat])    
        if mat % 2 != 0:
            major = -major
        cofactor = matrix[0][mat] * major
        determinant = determinant + cofactor
    return determinant

def det7(matrix):
    subMat = cofac(matrix)
    determinant = 0

    for mat in range(0, len(subMat)):
        major = det6(subMat[mat])    
        if mat % 2 != 0:
            major = -major
        cofactor = matrix[0][mat] * major
        determinant = determinant + cofactor
    return determinant

def det8(matrix):
    subMat = cofac(matrix)
    determinant = 0

    for mat in range(0, len(subMat)):
        major = det7(subMat[mat])    
        if mat % 2 != 0:
            major = -major
        cofactor = matrix[0][mat] * major
        determinant = determinant + cofactor
    return determinant

# Identify what matrix
size = int(input("What is the size of your matrix?: "))

print("The size of your matrix is %d by %d" % (size, size), ". \n", sep = "")

for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(str(row) + str(col), end = " ")
    print("")

# Enter the matrix
matrix = []
for row in range(0, size):
    matRow = []
    for col in range(0, size):
        matCol = int(input(f"Input the element for cell {row + 1}{col + 1}: "))
        matRow.append(matCol)
    matrix.append(matRow)

for row in matrix:
    for col in row:
        print(col, end = "\t")
    print("")

if size == 2:
    print(det2(matrix))

elif size == 3:
    print(det3(matrix))

elif size == 4:
    print(det4(matrix))

elif size == 5:
    print(det5(matrix))

elif size == 6:
    print(det6(matrix))
    
elif size == 7:
    print(det7(matrix))
    
elif size == 8:
    print(det8(matrix))
    
else:
    print("HEPS BAWAL IYAN")