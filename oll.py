import moves
import time
algs=["R U B' R B R2 U' R' F R F'", "F R U R' U' F' U2 F U R U' R' F'", "F U R U' R' F' U F R U R' U' F'",
      "F U R U' R' F' U' F R U R' U' F'", "L' U' L2 F' L' F2 U' F'", " R U R2 F R F2 U F", "L' U2 L U2 L F' L' F",
      "R U2 R' U2 R' F R F'", "R U R' U' R' F R2 U R' U' F'", "R U R' U R' F R F' R U2 R'", "F' L' U' L U F U F R U R' U' F'",
      "F R U R' U' F' U F R U R' U' F'", "F U R U2 R' U' R U R' F'", "R' F R U R' F' R F U' F'", "R' F' R L' U' L U R' F R",
      "L F L' R U R' U' L F' L'", "R U R' U R' F R F' U2 R' F R F'", "L F R U2 R' U2 R U2 R' F' L'", "R' U2 F R U R' U' F2 U2 F R",
      "F U R U' R' F' U2 R' U' R' F R F' U R", "R U R' U R U' R' U R U2 R'", "R U2 R2 U' R2 U' R2 U2 R", "R2 D R' U2 R D' R' U2 R'",
      "L F R' F' L' F R F'", "R' F R B' R' F' R B", "R' U' R U' R' U2 R", "R U R' U R U2 R'", "F R U R' U' F2 L' U' L U F",
      "R U R' U' R U' R' F' U' F R U R'", "F R' F R2 U' R' U' R U R' F2", "R' U' F U R U' R' F' R", "R U B' U' R' U R B R'",
      "R U R' U' R' F R F'", "R U R' U' B' R' F R F' B", "R U2 R2 F R F' R U2 R'", "L' U' L U' L' U L U L F' L' F",
      "F R' F' R U R U' R'", " R U R' U R U' R' U' R' F R F'", "R B' R' U' R U B U' R'", "R' F R U R' U' F' U R",
      "F U R2 D R' U' R D' R2 F'", "R' U' R U' R' U2 R F R U R' U' F'", "F' U' L' U L F", "F U R U' R' F'", "F R U R' U' F'",
      "R' U' R' F R F' U R", "F' L' U' L U L' U' L U F", "F R U R' U' R U R' U' F'","R B' R2 F R2 B R2 F' R", "R' F R2 B' R2 F' R2 B R'",
      "F U R U' R' U R U' R' F'", "R' U' R U' R' U F' U F R", "F' L F L' U2 F2 R' F' R F'", "F' L' U' L U L' U L U' L' U' L F",
      "R U2 R2 U' R U' R' U2 F R F'", "F R U R' U' R F' L F R' F' L'", "R U R' U' R' L F R F' L'",""]

def solveoll(col):
    pre = ""
    flag = 0
    fulloll=""
    t=time.time()
    for x in range(4):
        tcol = [y[:] for y in col]
        if x==0:
            pre=""
        if x==1:
            pre="U"
            moves.breakscram("U",col)
        if x==2:
            pre="U2"
            moves.breakscram("U", col)
        if x==3:
            pre="U'"
            moves.breakscram("U", col)
        for i in algs:
            tcol = [y[:] for y in col]
            moves.breakscram(i, tcol)
            if (tcol[0][6]=="yellow" and tcol[0][7]=="yellow" and tcol[0][8]=="yellow" and tcol[1][6]=="yellow" and
            tcol[1][7] == "yellow" and tcol[1][8]=="yellow" and tcol[2][6]=="yellow" and tcol[2][7]=="yellow" and tcol[2][8]=="yellow"):
                fulloll=pre + " " + i
                moves.breakscram(i, col)
                print(fulloll)
                flag=1
                break
        if flag == 1:
            break
    #print(time.time()-t)
    return fulloll
