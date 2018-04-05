import moves
import time

algs=["R' F R' B2 R F' R' B2 R2", "R2 B2 R F R' B2 R F' R", "R2 U R2 U D R2 U' R2 U R2 U' D' R2 U R2 U2 R2",
      "R' U R U' R2 F' U' F U R F R' F' R2", "D' R2 U R' U R' U' R U' R2 U' D R' U R", "R' U' R U D' R2 U R' U R U' R U' R2 D",
      "R2 U' R U' R U R' U R2 D' U R U' R' D", "R U R' U' D R2 U' R U' R' U R' U R2 D'", "R2 U2 R U2 R2 U2 R2 U2 R U2 R2",
      "R' U L' U2 R U' R' U2 R L", "R U2 R' U' R U2 L' U R' U' L", "L U' R U2 L' U R' L U' R U2 L' U R'",
      "R' U L' U2 R U' L R' U L' U2 R U' L", "L U2 L' U2 L F' L' U' L U L F L2", "R' U2 R U2 R' F R U R' U' R' F' R2",
      "R U R' U' R' F R2 U' R' U' R U R' F'", "R2 U' R' U' R U R U R U' R", "R2 U R U R' U' R' U' R' U R'",
      "R U2 R' D R U' R U' R U R2 D R' U' R D2", "F R' F R2 U' R' U' R U R' F' R U R' U' F'",
      "R' U' R2 U R U R' U' R U R U' R U' R'", ""]


def solvepll(col):
    pre = ""
    post = ""
    flag = 0
    fullpll=""
    t=time.time()
    for x in range(4):
        tcol = [x[:] for x in col]
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
            tcol = [x[:] for x in col]
            moves.breakscram(i, tcol)
            if (tcol[3][0]==tcol[3][1]==tcol[3][2] and tcol[3][3]==tcol[3][4]==tcol[3][5] and tcol[3][6]==tcol[3][7]==tcol[3][8] and
                tcol[3][9]==tcol[3][10]==tcol[3][11]):
                for q in range(4):
                    if q==0:
                        post=""
                    if q==1:
                        post="U"
                        moves.breakscram("U", tcol)
                    if q==2:
                        post="U2"
                        moves.breakscram("U", tcol)
                    if q==3:
                        post="U'"
                        moves.breakscram("U", tcol)
                    if tcol[3][0]=="blue":
                        break
                fullpll = pre + " " + i + " " + post
                moves.breakscram(i + " " + post, col)
                print(fullpll)
                flag = 1
                break
        if flag == 1:
            break
    #print(time.time()-t)
    return fullpll
