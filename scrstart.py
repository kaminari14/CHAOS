from graphics import *
import moves
import cross
import f2l
import oll
import pll
import time

win= GraphWin("my win", 600, 600)

col=[["" for i in range(12)] for j in range(9)]     #9x12 array that reresents the state of the cube


#reset


for i in range(0, 9):                   #setting the state to completely solved
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


scramble= input("enter scramble")         #input scramble algorithm here
moves.breakscram(scramble, col)           #does a scramble on the solved state of the cube to get unsolved state

t=time.time()
cross.makecross(col)               #solves cross
f2l.dof2l(col)                     #solves f2l
oll.solveoll(col)                  #solves oll
pll.solvepll(col)                  #slves pll

print(time.time()-t)

p=-1
for j in range(10, 270, 30):            #use the 9*12 array with your graphic library to print out the solved state
    p+=1
    q=-1
    for i in range (10,360, 30):
        q+=1
        if p<3 and (q<6 or q>8):
            continue
        if p>5 and (q<6 or q>8):
            continue
        rect=Rectangle(Point(i,j),Point(i+20,j+20))
        rect.setFill(col[p][q])
        rect.draw(win)



win.getMouse()
win.close()