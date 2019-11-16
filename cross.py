import time
#from line_profiler import LineProfiler
import crawl
import moves




def makecross(col):
    t=time.time()
    max=0
    csol=""
    while(max<100):
        max=0
        maxi = ""
        for i in crawl.crawl:
            tcol=[x[:] for x in col]
            moves.breakscram(i,tcol)
            hap=happiness(tcol, i)
            if hap>= max:
                max=hap
                maxi=i
        csol=csol+ maxi
        print(maxi)
        moves.breakscram(maxi, col)
    u=time.time()
    #print(u-t)
    return csol



def happiness(col, scram):
    meter=0
    if col[6][7]=="white" and col[5][7]=="green":
        meter=meter+25
    if col[7][6]=="white" and col[5][4]=="red":
        meter=meter+25
    if col[7][8]=="white" and col[5][10]=="orange":
        meter=meter+25
    if col[8][7] == "white" and col[5][1] == "blue":
        meter=meter+25
    if col[4][0] == "white":
        meter = meter + 2
    if col[4][2] == "white":
        meter = meter + 2
    if col[4][3] == "white":
        meter = meter + 2
    if col[4][5] == "white":
        meter = meter + 2
    if col[4][6] == "white":
        meter = meter + 2
    if col[4][8] == "white":
        meter = meter + 2
    if col[4][9] == "white":
        meter = meter + 2
    if col[4][11] == "white":
        meter = meter + 2
    if len(scram.split(" "))==3:
        meter=meter+0.04
    if len(scram.split(" "))==2:
        meter=meter+0.07
    if len(scram.split(" "))==1:
        meter=meter+0.09
    for i in scram.split(" "):
        if "2" in i:
            meter = meter - 0.01
    return meter



#lp=LineProfiler()
#aa=lp(makecross)
#aa([['', '', '', '', '', '', 'yellow', 'yellow', 'green', '', '', ''],
#['', '', '', '', '', '', 'white', 'yellow', 'yellow', '', '', ''],
#['', '', '', '', '', '', 'orange', 'orange', 'white', '', '', ''],
#['orange', 'blue', 'blue', 'red', 'green', 'white', 'blue', 'white', 'red', 'blue', 'green', 'white'],
#['blue', 'blue', 'blue', 'white', 'red', 'green', 'orange', 'green', 'red', 'green', 'orange', 'red'],
#['orange', 'red', 'green', 'white', 'red', 'yellow', 'orange', 'orange', 'red', 'yellow', 'orange', 'blue'],
#['', '', '', '', '', '', 'green', 'yellow', 'green', '', '', ''],
#['', '', '', '', '', '', 'yellow', 'white', 'blue', '', '', ''],
#['', '', '', '', '', '', 'red', 'white', 'yellow', '', '', '']]
#)
#lp.print_stats()
