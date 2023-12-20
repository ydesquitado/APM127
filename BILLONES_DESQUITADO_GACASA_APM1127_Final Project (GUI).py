import tkinter
import customtkinter
from functions import *
import os

def restart():
    app.destroy()
    os.startfile("BILLONES_DESQUITADO_GACASA_APM1127_Final Project (GUI).py")

def confirmSize():
    matSize = int(size.get())

    if matSize >= 2 and matSize <= 8:
        print("The size is:", matSize)
        buildMatrix(matSize)
    else:
        print("Wrong value!")
        raise Exception("Sorry. Only numbers from 2 to 8 are allowed.")
    
    return

def resetDet():
    for widgets in tInsertMatFrame.winfo_children():
        widgets.destroy()
    for widgets in tMatrixFrame.winfo_children():
        widgets.destroy()
    for widgets in tConfirmMatrixFrame.winfo_children():
        widgets.destroy()
    for widgets in bDisplayFrame.winfo_children():
        widgets.destroy()
    for widgets in bSolveMatrixFrame.winfo_children():
        widgets.destroy()
    for widgets in bSolveMatrixFrame.winfo_children():
        widgets.destroy()
    for widgets in bDeterminantTitleFrame.winfo_children():
        widgets.destroy()
    for widgets in bDeterminantValueFrame.winfo_children():
        widgets.destroy()
    return

def buildMatrix(matSize):
    inputMatrix = customtkinter.CTkLabel(master = tInsertMatFrame, 
                                         text = "Insert the matrix here", 
                                         font = ("Montserrat", 50, "bold"))
    inputMatrix.pack(expand = True)
    
    matrixElements = []
    for row in range(0, matSize):
        for col in range(0, matSize):
            element = tkinter.IntVar()
            elementValue = customtkinter.CTkEntry(master = tMatrixFrame, 
                                                  height = 50, 
                                                  width = 50, 
                                                  font = ("Montserrat", 20, "bold"), 
                                                  textvariable = element)
            elementValue.grid(row = row, column = col)
            matrixElements.append(element)
    
    print("The matrixElements before confirm =", matrixElements)
    confirmMatrixBtn = customtkinter.CTkButton(master = tConfirmMatrixFrame, 
                                               text = "Confirm", 
                                               text_color = "black", 
                                               font = ("Montserrat", 20, "bold"),
                                               width = 100,
                                               height = 45,
                                               corner_radius = 5,
                                               command = lambda: confirmMatrix(matSize, matrixElements))
    confirmMatrixBtn.pack(padx = 10, pady = 30)

def confirmMatrix(matSize, matrixElements):
    matrix = []
    n = 0
    for row in range(0, matSize):
        rowMat = []
        for col in range(0, matSize):
            cellValue = matrixElements[n].get()
            rowMat.append(cellValue)
            n += 1
        matrix.append(rowMat)
    
    displayMatrix(matSize, matrix)

    solveMatrixBtn = customtkinter.CTkButton(master = bSolveMatrixFrame, 
                                             text = "Solve", 
                                             text_color = "black", 
                                             font = ("Montserrat", 20, "bold"), 
                                             width = 100, 
                                             height = 45, 
                                             corner_radius = 5,
                                             command = lambda: solveDeterminant(matSize, matrix))
    solveMatrixBtn.pack(padx = 10, pady = 30)
    return

def displayMatrix(matSize, matrix):
    displayTitle = customtkinter.CTkLabel(master = bDisplayTitleFrame, 
                                          text = "Is this the matrix you wish to solve for?",
                                          font = ("Montserrat", 20, "bold", "italic"))
    displayTitle.pack(expand = True)
    for row in range(0, matSize):
        for col in range(0, matSize):
            cell = customtkinter.CTkLabel(master = bDisplayMatrixFrame, 
                                          text = f"{matrix[row][col]}", 
                                          width = 30, 
                                          height = 30, 
                                          font = ("Montserrat", 20, "bold"))
            cell.grid(row = row, column = col)
    return

def solveDeterminant(matSize, matrix):
    if matSize == 2:
        determinant = det2(matrix)
    elif matSize == 3:
        determinant = det3(matrix)
    elif matSize == 4:
        determinant = det4(matrix)
    elif matSize == 5:
        determinant = det5(matrix)
    elif matSize == 6:
        determinant = det6(matrix)
    elif matSize == 7:
        determinant = det7(matrix)
    elif matSize == 8:
        determinant = det8(matrix)

    determinantTitle = customtkinter.CTkLabel(master = bDeterminantTitleFrame, 
                                              text = f"The determinant of this {matSize} by {matSize} matrix is:", 
                                              font = ("Montserrat", 20, "bold"))
    determinantTitle.pack()
    determinantValue = customtkinter.CTkLabel(master = bDeterminantValueFrame, 
                                              text = determinant, 
                                              font = ("Montserrat", 50, "bold"))
    determinantValue.pack()

    return

# System setting
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

# Our app frame
app = customtkinter.CTk()
app.geometry("1080x720")
app.title("Determinant")
#app.resizable(width = False, height = True)

topFrame = customtkinter.CTkFrame(master = app, 
                                  fg_color = "blue")
topFrame.pack(side = "top", 
              fill = "both", 
              expand = True)
botFrame = customtkinter.CTkFrame(master = app, 
                                  fg_color = "red")
botFrame.pack(side = "bottom", 
              fill = "both", 
              expand = True)
tLeftFrame = customtkinter.CTkFrame(master = topFrame, 
                                    fg_color = "green", 
                                    corner_radius = 15)
tLeftFrame.pack(side = "left", 
                fill = "both", 
                expand = True, 
                padx = 10, 
                pady = 10)
tRightFrame = customtkinter.CTkFrame(master = topFrame, 
                                     fg_color = "yellow", 
                                     corner_radius = 15)
tRightFrame.pack(side = "left", 
                 fill = "both", 
                 expand = True, 
                 padx = 10, 
                 pady = 10)
bLeftFrame = customtkinter.CTkFrame(master = botFrame, 
                                    fg_color = "pink", 
                                    corner_radius = 15)
bLeftFrame.pack(side = "left", 
                fill = "both", 
                expand = True, 
                padx = 10, 
                pady = 10)
bRightFrame = customtkinter.CTkFrame(master = botFrame, 
                                     fg_color = "purple", 
                                     corner_radius = 15)
bRightFrame.pack(side = "left", 
                 fill = "both", 
                 expand = True, 
                 padx = 10, 
                 pady = 10)
tInsertMatFrame = customtkinter.CTkFrame(master = tRightFrame, 
                                         fg_color = "gray")
tInsertMatFrame.pack(expand = True)
tMatrixFrame = customtkinter.CTkFrame(master = tRightFrame, 
                                      fg_color = "white")
tMatrixFrame.pack(expand = True)
tConfirmMatrixFrame = customtkinter.CTkFrame(master = tRightFrame, 
                                             fg_color = "gray")
tConfirmMatrixFrame.pack(expand = True)
bDisplayFrame = customtkinter.CTkFrame(master = bLeftFrame, 
                                       fg_color = "magenta")
bDisplayFrame.pack(side = "left", 
                   expand = True)
bDisplayTitleFrame = customtkinter.CTkFrame(master = bDisplayFrame, 
                                            fg_color = "magenta")
bDisplayTitleFrame.pack(expand = True)
bDisplayMatrixFrame = customtkinter.CTkFrame(master = bDisplayFrame, 
                                             fg_color = "magenta")
bDisplayMatrixFrame.pack(expand = True)
bSolveMatrixFrame = customtkinter.CTkFrame(master = bLeftFrame, 
                                           fg_color = "indigo")
bSolveMatrixFrame.pack(side = "left", 
                       expand = True)
bDeterminantTitleFrame = customtkinter.CTkFrame(master = bRightFrame, 
                                                fg_color = "light gray")
bDeterminantTitleFrame.pack(side = "top", 
                            fill = "both",
                            expand = True)
bDeterminantValueFrame = customtkinter.CTkFrame(master = bRightFrame, 
                                                fg_color = "dark gray")
bDeterminantValueFrame.pack(side = "top", 
                            fill = "both", 
                            expand = True)

# Adding UI element
title = customtkinter.CTkLabel(master = tLeftFrame, 
                               text = "Insert the size of your matrix", 
                               font = ("Montserrat", 50, "bold"), 
                               bg_color = "white")
title.pack(expand = True)

# Size input
sizeInput = tkinter.IntVar()
size = customtkinter.CTkEntry(master = tLeftFrame, 
                              width = 60, 
                              height = 60, 
                              font = ("Montserrat", 20, "bold"), 
                              textvariable = sizeInput)
size.pack(expand = True)

# Confirm button
confirmSizeBtn = customtkinter.CTkButton(master = tLeftFrame, 
                                         text = "Confirm", 
                                         font = ("Montserrat", 20, "bold"), 
                                         text_color = "black", 
                                         width = 100,
                                         height = 45,
                                         corner_radius = 5,
                                         command = confirmSize)
confirmSizeBtn.pack(side = "left", expand = True, pady = 100)
resetSizeBtn = customtkinter.CTkButton(master = tLeftFrame, 
                                       text = "Reset", 
                                       font = ("Montserrat", 20, "bold"), 
                                       text_color = "black", 
                                       width = 100,
                                       height = 45,
                                       corner_radius = 5,
                                       command = restart)
resetSizeBtn.pack(side = "left", expand = True, pady = 100)

# Display the Matrix entered


# Run app
app.mainloop()