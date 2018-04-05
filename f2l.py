import time
import crawl
import moves


def dof2l(col):
    t=time.time()
    max=0
    fsol=""
    while(max<100):
        max=0
        maxi = ""
        for i in crawl.crawl:
            tcol = [x[:] for x in col]
            moves.breakscram(i,tcol)
            hap=happiness(tcol, i)
            #if i==" R' U R":
            #    print("------", hap)
            if hap>= max:
                max=hap
                maxi=i
        print(maxi, max)
        fsol=fsol+maxi
        moves.breakscram(maxi, col)
    u=time.time()
    #print(u-t)
    return fsol


def happiness(col,scram):
    meter=0
    if ((col[6][7]=="white" and col[5][7]=="green") and
    (col[7][6]=="white" and col[5][4]=="red") and
    (col[7][8]=="white" and col[5][10]=="orange")
    and (col[8][7] == "white" and col[5][1] == "blue")):
        meter= meter+60
    if (col[6][6]=="white" and col[5][5]=="red" and col[4][5]=="red" and col[4][6]=="green" and col[5][6]=="green"):
        meter=meter+10
    if (col[6][8]=="white" and col[5][8]=="green" and col[4][8]=="green" and col[5][9]=="orange" and col[4][9]=="orange"):
        meter=meter+10
    if (col[8][8]=="white" and col[4][0]=="blue" and col[5][0]=="blue" and col[4][11]=="orange" and col[5][11]=="orange"):
        meter=meter+10
    if (col[8][6]=="white" and col[5][2]=="blue" and col[4][2]=="blue" and col[5][3]=="red" and col[4][3]=="red"):
        meter=meter+10


    if (col[3][3]=="white"):
        if((col[0][6]==col[2][7] and col[3][2]==col[3][7]) or
        (col[0][6]==col[1][8] and col[3][2]==col[3][10])):
            if (col[6][6]=="white" and col[5][5]=="red" and col[4][5]=="red"
                and col[4][6]=="green" and col[5][6]=="green"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if(col[0][6]==col[1][6] and col[3][2]==col[3][4]):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter=meter+0.0001
            else:
                meter=meter+0.0005
        if ((col[3][1] == col[3][2]) and (col[0][6] == col[0][7])):
            if col[0][7] == "blue":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[0][6]==col[3][7] and col[3][2]==col[2][7]):
            if col[3][2]=="blue":
                meter=meter+3
            else:
                meter=meter+1
        if ((col[0][6]==col[3][10] and col[3][2]==col[1][8]) or
        (col[0][6]==col[3][1] and col[3][2]==col[0][7])):
            if (col[6][6]=="white" and col[5][5]=="red" and col[4][5]=="red"
                and col[4][6]=="green" and col[5][6]=="green"):
                meter=meter+0.01
            else:
                meter= meter+0.05
        if (col[0][6]==col[3][4] and col[3][2]==col[1][6]):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter=meter+0.0001
            else:
                meter=meter+0.0005


    if (col[3][0] == "white"):
        if ((col[0][8] == col[2][7] and col[3][11] == col[3][7]) or
        (col[0][8] == col[1][6] and col[3][11] == col[3][4])):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][3] == "red"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[0][8] == col[0][7] and col[3][11] == col[3][1]):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[0][8] == col[1][8]) and (col[3][10] == col[3][11])):
            if col[1][8] == "orange":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[0][8]==col[3][4] and col[3][11]==col[1][6]):
            if col[3][11]=="orange":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[0][8]==col[3][7] and col[3][11]==col[2][7]) or
        (col[0][8]==col[3][10] and col[3][11]==col[1][8])):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[0][8]==col[3][1] and col[3][11]==col[0][7]):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005


    if (col[3][2]=="white"):
        if ((col[0][6]==col[2][7] and col[3][3]==col[3][7]) or
        (col[0][6]==col[1][8] and col[3][3]==col[3][10])):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if(col[0][6]==col[0][7] and col[3][1]==col[3][3]):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[3][3] == col[3][4]) and (col[0][6] == col[1][6])):
            if col[1][6] == "red":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[0][6]==col[3][10] and col[3][3]==col[1][8]):
            if col[3][3]=="red":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[0][6]==col[3][7] and col[3][3]==col[2][7]) or
        (col[0][6]==col[3][4] and col[3][3]==col[1][6])):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[0][6]==col[3][1] and col[3][3]==col[0][7]):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005


    if (col[3][5]=="white"):
        if ((col[2][6]==col[0][7] and col[3][6]==col[3][1]) or
        (col[2][6]==col[1][8] and col[3][6]==col[3][10])):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][3] == "red"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if (col[2][6]==col[1][6] and col[3][6]==col[3][4]):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[3][6] == col[3][7]) and (col[2][6] == col[2][7])):
            if col[2][7] == "green":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[2][6]==col[3][1] and col[3][6]==col[0][7]):
            if col[3][6]=="green":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[2][6]==col[3][10] and col[3][6]==col[1][8]) or
        (col[2][6]==col[3][7] and col[3][6]==col[2][7])):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[2][6]==col[3][4] and col[3][6]==col[1][6]):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005


    if (col[3][6]=="white"):
        if ((col[2][6]==col[0][7] and col[3][5]==col[3][1]) or
        (col[2][6]==col[1][8] and col[3][5]==col[3][10])):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if(col[2][6]==col[2][7] and col[3][5]==col[3][7]):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[3][5] == col[3][4]) and (col[2][6] == col[1][6])):
            if col[1][6] == "red":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[2][6]==col[3][10] and col[3][5]==col[1][8]):
            if col[3][5]=="red":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[2][6]==col[3][1] and col[3][5]==col[0][7]) or
        (col[2][6]==col[3][4] and col[3][5]==col[1][6])):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[2][6]==col[3][7] and col[3][5]==col[2][7]):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005


    if (col[3][8]=="white"):
        if ((col[2][8]==col[0][7] and col[3][9]==col[3][1]) or
        (col[2][8]==col[1][6] and col[3][9]==col[3][4])):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if(col[2][8]==col[2][7] and col[3][9]==col[3][7]):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[3][9] == col[3][10]) and (col[2][8] == col[1][8])):
            if col[1][8] == "orange":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[2][8]==col[3][4] and col[3][9]==col[1][6]):
            if col[3][9]=="orange":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[2][8]==col[3][1] and col[3][9]==col[0][7]) or
        (col[2][8]==col[3][10] and col[3][9]==col[1][8])):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[2][8]==col[3][7] and col[3][9]==col[2][7]):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005

    if (col[3][9]=="white"):
        if ((col[2][8]==col[0][7] and col[3][8]==col[3][1]) or
        (col[2][8]==col[1][6] and col[3][8]==col[3][4])):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if(col[2][8]==col[1][8] and col[3][8]==col[3][10]):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[3][8] == col[3][7]) and (col[2][7] == col[2][8])):
            if col[2][7] == "green":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[2][8]==col[3][1] and col[3][8]==col[0][7]):
            if col[3][8]=="green":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[2][8]==col[3][4] and col[3][8]==col[1][6]) or
        (col[2][8]==col[3][7] and col[3][8]==col[2][7])):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[2][8]==col[3][10] and col[3][8]==col[1][8]):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005


    if (col[3][11]=="white"):
        if ((col[0][8]==col[1][6] and col[3][0]==col[3][4]) or
        (col[0][8]==col[2][7] and col[3][0]==col[3][7])):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter=meter+0.01
            else:
                meter=meter+0.05
        if(col[0][8]==col[1][8] and col[3][0]==col[3][10]):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005
        if ((col[3][0] == col[3][1]) and (col[0][7] == col[0][8])):
            if col[0][7] == "blue":
                meter = meter + 3
            else:
                meter = meter + 1
        if (col[0][8]==col[3][7] and col[3][0]==col[2][7]):
            if col[3][0]=="blue":
                meter = meter + 3
            else:
                meter = meter + 1
        if ((col[0][8]==col[3][4] and col[3][0]==col[1][6]) or
        (col[0][8]==col[3][1] and col[3][0]==col[0][7])):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter = meter + 0.01
            else:
                meter = meter + 0.05
        if (col[0][8]==col[3][10] and col[3][0]==col[1][8]):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter = meter + 0.0001
            else:
                meter = meter + 0.0005




    #white on top

    if col[0][6]=="white":
        if (((col[3][2]==col[2][7]) and (col[3][3]== col[3][7])) or ((col[3][2]==col[3][7]) and (col[3][3]==col[2][7]))):
            if col[3][7]=="green":
                meter = meter + 0.05
            else:
                meter = meter + 0.01
        if (((col[3][2]==col[1][8]) and (col[3][3]== col[3][10])) or ((col[3][2]==col[3][10]) and (col[3][3]==col[1][8]))):
            if col[3][10]=="orange":
                meter = meter + 0.05
            else:
                meter = meter + 0.01
        if ((((col[3][2]==col[1][6]) and (col[3][3]== col[3][4])) or ((col[3][2]==col[3][4]) and (col[3][3]==col[1][6]))) or
            (((col[3][2] == col[0][7]) and (col[3][3] == col[3][1])) or ((col[3][2] == col[3][1]) and (col[3][3] == col[0][7])))):
            if (col[8][6] == "white" and col[5][2] == "blue" and col[4][2] == "blue"
                and col[5][3] == "red" and col[4][2] == "red"):
                meter=meter+0.0005
            else:
                meter=meter+0.0001


    if col[2][6]=="white":
        if (((col[3][5]==col[0][7]) and (col[3][6]== col[3][1])) or ((col[3][5]==col[3][1]) and (col[3][6]==col[0][7]))):
            if col[3][1]=="blue":
                meter = meter + 0.05
            else:
                meter = meter + 0.01
        if (((col[3][5]==col[1][8]) and (col[3][6]== col[3][10])) or ((col[3][5]==col[3][10]) and (col[3][6]==col[1][8]))):
            if col[3][10]=="orange":
                meter = meter + 0.05
            else:
                meter = meter + 0.01
        if ((((col[3][5]==col[1][6]) and (col[3][6]== col[3][4])) or ((col[3][5]==col[3][4]) and (col[3][6]==col[1][6]))) or
            (((col[3][5] == col[2][7]) and (col[3][6] == col[3][7])) or ((col[3][5] == col[3][7]) and (col[3][6] == col[2][7])))):
            if (col[6][6] == "white" and col[5][5] == "red" and col[4][5] == "red"
                and col[4][6] == "green" and col[5][6] == "green"):
                meter=meter+0.0005
            else:
                meter=meter+0.0001


    if col[2][8]=="white":
        if (((col[3][8]==col[0][7]) and (col[3][9]== col[3][1])) or ((col[3][8]==col[3][1]) and (col[3][9]==col[0][7]))):
            if col[3][1]=="blue":
                meter=meter+0.05
            else:
                meter=meter+0.01
        if (((col[3][8]==col[1][6]) and (col[3][9]== col[3][4])) or ((col[3][8]==col[3][4]) and (col[3][9]==col[1][6]))):
            if col[3][4]=="red":
                meter=meter+0.05
            else:
                meter=meter+0.01
        if ((((col[3][8]==col[1][8]) and (col[3][9]== col[3][10])) or ((col[3][8]==col[3][10]) and (col[3][9]==col[1][8]))) or
            (((col[3][8] == col[2][7]) and (col[3][9] == col[3][7])) or ((col[3][8] == col[3][7]) and (col[3][9] == col[2][7])))):
            if (col[6][8] == "white" and col[5][8] == "green" and col[4][8] == "green"
                and col[5][9] == "orange" and col[4][9] == "orange"):
                meter=meter+0.0005
            else:
                meter=meter+0.0001

    if col[0][8]=="white":
        if (((col[3][0]==col[1][6]) and (col[3][11]== col[3][4])) or ((col[3][0]==col[3][4]) and (col[3][11]==col[1][6]))):
            if col[3][4]=="red":
                meter=meter+0.05
            else:
                meter=meter+0.01
        if (((col[3][0]==col[2][7]) and (col[3][11]== col[3][7])) or ((col[3][0]==col[3][7]) and (col[3][11]==col[2][7]))):
            if col[3][7]=="green":
                meter=meter+0.05
            else:
                meter=meter+0.01
        if ((((col[3][0]==col[1][8]) and (col[3][11]== col[3][10])) or ((col[3][0]==col[3][10]) and (col[3][11]==col[1][8]))) or
            (((col[3][0] == col[0][7]) and (col[3][11] == col[3][1])) or ((col[3][0] == col[3][1]) and (col[3][11] == col[0][7])))):
            if (col[8][8] == "white" and col[4][0] == "blue" and col[5][0] == "blue"
                and col[4][11] == "orange" and col[5][11] == "orange"):
                meter=meter+0.0005
            else:
                meter=meter+0.0001

    if len(scram.split(" "))==3:
        meter=meter+0.00004
    if len(scram.split(" "))==2:
        meter=meter+0.00007
    if len(scram.split(" "))==1:
        meter=meter+0.00009
    for i in scram.split(" "):
        if "2" in i:
            meter = meter - 0.00001
    return meter