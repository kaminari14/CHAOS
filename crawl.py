moveset=["R","R'","L","L'","F","F'","U","U'","B","B'","D","D'",'R2','D2','F2','U2','L2','B2']

tsol=""
i=""
crawl=[]
def whatnext(tsol,i):
    if i!="":
        tsol = tsol + " " + i
    crawl.append(tsol)
    for j in moveset:
        if len(tsol.split())!=0:
            if tsol.split()[len(tsol.split())-1][0] == j[0]:
                continue
        if len(tsol.split())>1:
            if ((tsol.split()[len(tsol.split())-2][0] =="R" and tsol.split()[len(tsol.split())-1][0]== "L" and j[0]=="R") or
            (tsol.split()[len(tsol.split())-2][0] =="L" and tsol.split()[len(tsol.split())-1][0]== "R" and j[0]=="L") or
            (tsol.split()[len(tsol.split())-2][0] =="F" and tsol.split()[len(tsol.split())-1][0]== "B" and j[0]=="F") or
            (tsol.split()[len(tsol.split())-2][0] =="B" and tsol.split()[len(tsol.split())-1][0]== "F" and j[0]=="B") or
            (tsol.split()[len(tsol.split())-2][0] =="U" and tsol.split()[len(tsol.split())-1][0]== "D" and j[0]=="U") or
            (tsol.split()[len(tsol.split())-2][0] =="D" and tsol.split()[len(tsol.split())-1][0]== "U" and j[0]=="D")):
                continue
        if len(tsol.split())>3:
            break
        whatnext(tsol,j,)

whatnext(tsol,i)