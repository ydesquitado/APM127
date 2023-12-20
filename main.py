import time
import tkinter
import customtkinter
from functions import *
import os
import sys

def confirmSize():
    matSize = int(size.get())

    if matSize >= 2 and matSize <= 8:
        print("The size is:", matSize)
        buildMatrix(matSize)
    else:
        error = customtkinter.CTkLabel(master = tLeftFrame, 
                                       text = "The digit you entered is invalid. Only numbers from 2 to 8 are allowed.\nClose the window.", 
                                       text_color = "red")
        error.pack(side = "top",
                   expand = True,
                   fill = "both")
    
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
                                             fg_color = "white", 
                                             command = lambda: solveDeterminant(matSize, matrix))
    solveMatrixBtn.pack(padx = 10, pady = 30)
    return

def displayMatrix(matSize, matrix):
    displayTitle = customtkinter.CTkLabel(master = bDisplayTitleFrame, 
                                          text = "Is this the matrix you wish to solve the determinant of?",
                                          font = ("Montserrat", 20, "bold", "italic"))
    displayTitle.pack(pady = 20, 
                      expand = True)

    if matSize > 4:
        fontSize = 40
    else:
        fontSize = 20

    for row in range(0, matSize):
        for col in range(0, matSize):
            cell = customtkinter.CTkLabel(master = bDisplayMatrixFrame, 
                                          text = f"   {matrix[row][col]}   ", 
                                          width = 30, 
                                          height = 30, 
                                          font = ("Montserrat", fontSize, "bold"))
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
    determinantTitle.pack(padx = 20, 
                          pady = 40)
    determinantValue = customtkinter.CTkLabel(master = bDeterminantValueFrame, 
                                              text = determinant, 
                                              font = ("Montserrat", 50, "bold"))
    determinantValue.pack()
    close = customtkinter.CTkButton(master = bCloseFrame, 
                                    text = "Quit", 
                                    text_color = "black", 
                                    font = ("Montserrat", 20, "bold"), 
                                    width = 100, 
                                    height = 45, 
                                    corner_radius = 5,
                                    fg_color = "red", 
                                    command = lambda: app.destroy())
    close.pack(side = "right", 
               expand = True, 
               padx = 20, 
               pady = 20)

    return

# System setting
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

# Our app frame
app = customtkinter.CTk()
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width - 100}x{height - 100}+50+50")
app.title("Determinant")
#app.resizable(width = False, height = True)

topFrame = customtkinter.CTkFrame(master = app, 
                                  fg_color = "#E9E2D6")
topFrame.pack(side = "top", 
              fill = "both", 
              expand = True)
botFrame = customtkinter.CTkFrame(master = app, 
                                  fg_color = "#E9E2D6")
botFrame.pack(side = "bottom", 
              fill = "both", 
              expand = True)
tLeftFrame = customtkinter.CTkFrame(master = topFrame, 
                                  fg_color = "#F9D4D4")
tLeftFrame.pack(side = "left", 
                fill = "both", 
                expand = True, 
                padx = 10, 
                pady = 10)
tRightFrame = customtkinter.CTkFrame(master = topFrame, 
                                  fg_color = "#F9E7D4")
tRightFrame.pack(side = "left", 
                 fill = "both", 
                 expand = True, 
                 padx = 10, 
                 pady = 10)
bLeftFrame = customtkinter.CTkFrame(master = botFrame, 
                                  fg_color = "#EAF9D4")
bLeftFrame.pack(side = "left", 
                fill = "both", 
                expand = True, 
                padx = 10, 
                pady = 10)
bRightFrame = customtkinter.CTkFrame(master = botFrame, 
                                  fg_color = "#D4F9F3")
bRightFrame.pack(side = "left", 
                 fill = "both", 
                 expand = True, 
                 padx = 10, 
                 pady = 10)
tInsertMatFrame = customtkinter.CTkFrame(master = tRightFrame, 
                                         fg_color = "#F9E7D4")
tInsertMatFrame.pack(expand = True)
tMatrixFrame = customtkinter.CTkFrame(master = tRightFrame, 
                                      fg_color = "#F9E7D4")
tMatrixFrame.pack(expand = True)
tConfirmMatrixFrame = customtkinter.CTkFrame(master = tRightFrame, 
                                             fg_color = "#F9E7D4")
tConfirmMatrixFrame.pack(expand = True)
bDisplayFrame = customtkinter.CTkFrame(master = bLeftFrame, 
                                  fg_color = "#EAF9D4")
bDisplayFrame.pack(side = "left", 
                   expand = True)
bDisplayTitleFrame = customtkinter.CTkFrame(master = bDisplayFrame, 
                                  fg_color = "#EAF9D4")
bDisplayTitleFrame.pack(expand = True)
bDisplayMatrixFrame = customtkinter.CTkFrame(master = bDisplayFrame, 
                                  fg_color = "#EAF9D4")
bDisplayMatrixFrame.pack(expand = True)
bSolveMatrixFrame = customtkinter.CTkFrame(master = bLeftFrame, 
                                  fg_color = "#EAF9D4")
bSolveMatrixFrame.pack(side = "left", 
                       expand = True)
bAnswerFrame = customtkinter.CTkFrame(master = bRightFrame, 
                                  fg_color = "#D4F9F3")
bAnswerFrame.pack(side = "left", 
                  fill = "both", 
                  expand = True)
bDeterminantTitleFrame = customtkinter.CTkFrame(master = bAnswerFrame, 
                                  fg_color = "#D4F9F3")
bDeterminantTitleFrame.pack(side = "top", 
                            fill = "both",
                            expand = True)
bDeterminantValueFrame = customtkinter.CTkFrame(master = bAnswerFrame, 
                                  fg_color = "#D4F9F3")
bDeterminantValueFrame.pack(side = "top", 
                            fill = "both", 
                            expand = True)
bCloseFrame = customtkinter.CTkFrame(master = bRightFrame, 
                                  fg_color = "#D4F9F3")
bCloseFrame.pack(side = "left", 
                 fill = "both",
                 expand = True)

# Adding UI element
title = customtkinter.CTkLabel(master = tLeftFrame, 
                               text = "Insert the size of your matrix", 
                               font = ("Montserrat", 50, "bold"),
                               text_color = "black")
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
confirmSizeBtn.pack(side = "left", 
                    expand = True, 
                    pady = 100)
resetSizeBtn = customtkinter.CTkButton(master = tLeftFrame, 
                                       text = "Close", 
                                       fg_color = "red", 
                                       font = ("Montserrat", 20, "bold"), 
                                       text_color = "black", 
                                       width = 100,
                                       height = 45,
                                       corner_radius = 5,
                                       command = lambda: app.destroy())
resetSizeBtn.pack(side = "left", 
                  expand = True, 
                  pady = 100)

# Display the Matrix entered


# Run app
app.mainloop()