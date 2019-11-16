#from graphics import *
import moves
import cross
import f2l
import oll
import pll
import time

#logs = open("/tmp/logf.txt", "a")

#win= GraphWin("my win", 600, 600)

col=[["" for i in range(12)] for j in range(9)]


#reset


for i in range(0, 9):
    for j in range(0,12):
        if j>5 and j<9 and i<3:
            col[i][j]="yellow"
        if i>2 and i<6:
            if j<3:
                col[i][j]="blue"
            if j>2 and j<6:
                col[i][j]="red"
            if j>5 and j<9:
                col[i][j]="green"
            if j>8 and j<12:
                col[i][j]="orange"
        if j > 5 and j < 9 and i > 5:
            col[i][j] = "white"


scramble= input("enter scramble")
moves.breakscram(scramble, col)
#logs.write(str(col))

t=time.time()
cr=cross.makecross(col)
f2=f2l.dof2l(col)
ol=oll.solveoll(col)
pl=pll.solvepll(col)

print("cross", cr)
print("f2l", f2)
print("oll", ol)
print("pll", pl)
fullsol=cr+" "+f2+" "+ol+" "+pl

print("------------------")

fullsol = fullsol.replace("R R'", "")
fullsol = fullsol.replace("L L'", "")
fullsol = fullsol.replace("F F'", "")
fullsol = fullsol.replace("D D'", "")
fullsol = fullsol.replace("B B'", "")
fullsol = fullsol.replace("U U'", "")
fullsol = fullsol.replace("R' R ", "")
fullsol = fullsol.replace("L' L ", "")
fullsol = fullsol.replace("F' F ", "")
fullsol = fullsol.replace("D' D ", "")
fullsol = fullsol.replace("B' B ", "")
fullsol = fullsol.replace("U' U ", "")
fullsol = fullsol.replace("U U ", "U2")
fullsol = fullsol.replace("F F ", "F2")
fullsol = fullsol.replace("D D ", "D2")
fullsol = fullsol.replace("B B ", "B2")
fullsol = fullsol.replace("L L ", "L2")
fullsol = fullsol.replace("R R ", "R2")
fullsol = fullsol.replace("U' U'", "U2")
fullsol = fullsol.replace("F' F'", "F2")
fullsol = fullsol.replace("D' D'", "D2")
fullsol = fullsol.replace("B' B'", "B2")
fullsol = fullsol.replace("L' L'", "L2")
fullsol = fullsol.replace("R' R'", "R2")
fullsol = fullsol.replace("U2 U ", "U'")
fullsol = fullsol.replace("F2 F ", "F'")
fullsol = fullsol.replace("D2 D ", "D'")
fullsol = fullsol.replace("B2 B ", "B'")
fullsol = fullsol.replace("L2 L ", "L'")
fullsol = fullsol.replace("R2 R ", "R'")
fullsol = fullsol.replace("U2 U'", "U")
fullsol = fullsol.replace("F2 F'", "F")
fullsol = fullsol.replace("D2 D'", "D")
fullsol = fullsol.replace("B2 B'", "B")
fullsol = fullsol.replace("L2 L'", "L")
fullsol = fullsol.replace("R2 R'", "R")
fullsol = fullsol.replace("U U2", "U'")
fullsol = fullsol.replace("F F2", "F'")
fullsol = fullsol.replace("D D2", "D'")
fullsol = fullsol.replace("B B2", "B'")
fullsol = fullsol.replace("L L2", "L'")
fullsol = fullsol.replace("R R2", "R'")
fullsol = fullsol.replace("U' U2", "U")
fullsol = fullsol.replace("F' F2", "F")
fullsol = fullsol.replace("D' D2", "D")
fullsol = fullsol.replace("B' B2", "B")
fullsol = fullsol.replace("L' L2", "L")
fullsol = fullsol.replace("R' R2", "R")

print("full solution:", fullsol)
print("solution length:", len(fullsol.split(" ")))

print(time.time()-t)
