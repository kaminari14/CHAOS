import urwid

logs = open("/tmp/log.txt", "a")

class _SideLayout(urwid.TextLayout):
    def layout(self, text, width, align, wrap):
        return [[(18, 0, 18)], [(18, 18, 36)], [(18, 36, 54)], [(18, 54, 72)], [(18, 72, 90)], [(18, 90, 108)],
                [(18, 108, 126)], [(18, 126, 144)], [(18, 144, 162)]]

class _LogoLayout(urwid.TextLayout):
    def layout(self, text, width, align, wrap):
        self.align='right'
        return [[(37, 0, 37)], [(37, 37, 74)], [(37, 74, 111)], [(37, 111, 148)], [(37, 148, 185)], [(37, 185, 222)],
                [(37, 222, 259)], [(37, 259, 296)], [(37, 296, 333)], [(37, 333, 370)], [(37, 370, 407)], [(37, 407, 444)]
            , [(37, 444, 481)], [(37, 481, 518)], [(37, 518, 555)], [(37, 555, 592)]]


'''
class _StatusLayout(urwid.TextLayout):
    def layout(self, text, width, align, wrap ):
        ll=len(text)
        if ll>width:
           diff=ll-width
        isless=True
        while isless:
            if diff/width==
'''

class cube:
    def __init__(self):
        self._up = []
        self._down = []
        self._left = []
        self._right = []
        self._back = []
        self._front = []
        self.up = []
        self.down = []
        self.left = []
        self.right = []
        self.back = []
        self.front = []
        self.cubearray = [["" for i in range(12)] for j in range(9)]
        self.footer1 = urwid.Text("")
        self.txt_scramble=urwid.Edit("Enter Scramble: \n","",align='left')
        self.txt_scramble_attr = urwid.AttrMap(self.txt_scramble,'bg',focus_map="form")
        self.chk_scan = urwid.CheckBox("Scan the CUBE")
        self.thescramble=""
        self.set_side("Y"*9, "U")
        self.set_side("R"*9, "L")
        self.set_side("O"*9, "R")
        self.set_side("B"*9, "B")
        self.set_side("G"*9, "F")
        self.set_side("W"*9, "D")
        self.set_cube_array()
        self.thesolution=""

    def _draw_boxes(self,itteration,colorofside):
        thetext=""
        temp=[]
        if(itteration==0):
            thetext="▛"+"▔"*4+"▜"
        if(itteration==1):
            thetext="▌"+" "*4+"▐"
        if(itteration==2):
            thetext="▙"+"▁"*4+"▟"

        temp += [(colorofside, thetext)]

        return temp

    def set_side(self,sequence, side):
        totaltemp = []
        threepair=[]
        for k in sequence:
            logs.write("sequence no: "+k+"\n")
            threepair+=k
            if len(threepair) >= 3:
                logs.write(str(threepair)+"\n")
                for i in range(0,3):
                    for j in threepair:
                        totaltemp+=self._draw_boxes(i,j)
                threepair=[]

        logs.write("^ for side : "+side+"\n")

        if side == "U":
            self._up = totaltemp
        elif side == "D":
            self._down = totaltemp
        elif side == "L":
            self._left = totaltemp
        elif side == "R":
            self._right = totaltemp
        elif side == "B":
            self._back = totaltemp
        elif side == "F":
            self._front = totaltemp
        else:
            pass

    def get_side_from_array(self,thearray):
        forup=""
        fordown=""
        forfront=""
        forback=""
        forleft=""
        forright=""
        for i in range(0, 9):
            for j in range(0, 12):
                if j > 5 and j < 9 and i < 3:
                    forup+=self._vtofarray(thearray[i][j])
                if i > 2 and i < 6:
                    if j < 3:
                        forback+=self._vtofarray(thearray[i][j])
                    if j > 2 and j < 6:
                        forleft+=self._vtofarray(thearray[i][j])
                    if j > 5 and j < 9:
                        forfront+=self._vtofarray(thearray[i][j])
                    if j > 8 and j < 12:
                        forright+=self._vtofarray(thearray[i][j])
                if j > 5 and j < 9 and i > 5:
                    fordown+=self._vtofarray(thearray[i][j])
        self.set_side(forup,"U")
        self.set_side(fordown,"D")
        self.set_side(forfront,"F")
        self.set_side(forback,"B")
        self.set_side(forleft,"L")
        self.set_side(forright,"R")

    def get_side(self,side):
        tside=""
        if(side == "U"):
           for i in self._up:
               if(i[1]=="▛▔▔▔▔▜"):
                   tside+=i[0]
        if(side == "D"):
            for i in self._down:
                if(i[1]=="▛▔▔▔▔▜"):
                    tside+=i[0]
        if(side == "L"):
            for i in self._left:
                if(i[1]=="▛▔▔▔▔▜"):
                    tside+=i[0]
        if(side == "R"):
            for i in self._right:
                if(i[1]=="▛▔▔▔▔▜"):
                    tside+=i[0]
        if(side == "F"):
            for i in self._front:
                if(i[1]=="▛▔▔▔▔▜"):
                    tside+=i[0]
        if(side == "B"):
            for i in self._back:
                if(i[1]=="▛▔▔▔▔▜"):
                    tside+=i[0]
        return tside

    def set_cube_array(self):
        up=self.get_side("U")
        down=self.get_side("D")
        front=self.get_side("F")
        back=self.get_side("B")
        left=self.get_side("L")
        right=self.get_side("R")
        uptemp=0
        downtemp=0
        lefttemp=0
        backtemp=0
        righttemp=0
        fronttemp=0
        for i in range(0, 9):
            for j in range(0, 12):
                if j > 5 and j < 9 and i < 3:
                    self.cubearray[i][j] = self._vtofarray(up[uptemp])
                    uptemp=uptemp+1
                if i > 2 and i < 6:
                    if j < 3:
                        self.cubearray[i][j] = self._vtofarray(back[backtemp])
                        backtemp=backtemp+1
                    if j > 2 and j < 6:
                        self.cubearray[i][j] = self._vtofarray(left[lefttemp])
                        lefttemp=lefttemp+1
                    if j > 5 and j < 9:
                        self.cubearray[i][j] = self._vtofarray(front[fronttemp])
                        fronttemp=fronttemp+1
                    if j > 8 and j < 12:
                        self.cubearray[i][j] = self._vtofarray(right[righttemp])
                        righttemp=righttemp+1
                if j > 5 and j < 9 and i > 5:
                    self.cubearray[i][j] = self._vtofarray(down[downtemp])
                    downtemp=downtemp+1
        return self.cubearray

    def _vtofarray(self,vtofstring):
        if vtofstring=="R":
            return "red"
        if vtofstring=="W":
            return "white"
        if vtofstring=="O":
            return "orange"
        if vtofstring=="B":
            return "blue"
        if vtofstring=="G":
            return "green"
        if vtofstring=="Y":
            return "yellow"


        if vtofstring=="red":
            return "R"
        if vtofstring=="white":
            return "W"
        if vtofstring=="orange":
            return "O"
        if vtofstring=="blue":
            return "B"
        if vtofstring=="green":
            return "G"
        if vtofstring=="yellow":
            return "Y"

    def draw_cube(self):
        blank = urwid.Text(" "*162, layout=_SideLayout())
        try:
            self.up = urwid.Text(self._up, layout=_SideLayout())
        except IndexError:
            self.up = urwid.Text(" "*162, layout=_SideLayout())

        try:
            self.down = urwid.Text(self._down, layout=_SideLayout())
        except IndexError:
            self.down = urwid.Text(" "*162, layout=_SideLayout())

        try:
            self.left = urwid.Text(self._left, layout=_SideLayout())
        except IndexError:
            self.left = urwid.Text(" "*162, layout=_SideLayout())

        try:
            self.right = urwid.Text(self._right, layout=_SideLayout())
        except IndexError:
            self.right = urwid.Text(" "*162, layout=_SideLayout())

        try:
            self.front = urwid.Text(self._front, layout=_SideLayout())
        except IndexError:
            self.front = urwid.Text(" "*162, layout=_SideLayout())

        try:
            self.back = urwid.Text(self._back, layout=_SideLayout())
        except IndexError:
            self.back = urwid.Text(" "*162, layout=_SideLayout())

        #CUBE LAYOUT
        gf1 = urwid.GridFlow([blank, self.up, blank, blank, self.left, self.front, self.right, self.back, blank, self.down, blank, blank],
                             cell_width=18, h_sep=1, v_sep=1, align="center")
        #CUBE LAYOUT ENDS

        #RIGHT FORM
        txt_logo = urwid.Text("█████████████████████████████████████"+
                              "████ ▄▄▄▄▄ █▀▀ ██▄  █▄ ▄▀█ ▄▄▄▄▄ ████"+
                              "████ █   █ █▄▀██▀█▀▄█▄ ▀ █ █   █ ████"+
                              "████ █▄▄▄█ █ ▄ █ ▄▄  █ ▀▀█ █▄▄▄█ ████"+
                              "████▄▄▄▄▄▄▄█ █ ▀▄█ █ ▀▄█▄█▄▄▄▄▄▄▄████"+
                              "████▄ ▀ ██▄ █▀█   ▄█▀▀█▄▀█ ▄▄▀▄▄▀████"+
                              "██████▀▀▀▄▄█▀▀▀   ██ █▀ ▄▄██ ▄  █████"+
                              "████▀▀ ▀█▄▄▀▀█▄ █ █▄  ▀█▀ ▄██▄█▄▄████"+
                              "████▄▀▄▄█ ▄ ▀▀█ █ ▄█▄▀▄█ ▀ ▄▄ ▄ ▄████"+
                              "████▄▄▄█▄▄▄▀▄█▀█ ▀▄█ ███ ▀▀ █▀█▄▀████"+
                              "████▄██ ▄ ▄▄▀▄▄▄ ██▀█  █▀ █  ██  ████"+
                              "████▄█▄██▄▄█ █▄▀█▄▄█ ██  ▄▄▄ █ ▀▀████"+
                              "████ ▄▄▄▄▄ █▄▀▄██▀▄▀████ █▄█ ▀▀▄▀████"+
                              "████ █   █ █▀ ▄▀ ▀▄██ █▀ ▄   ▀▀▀█████"+
                              "████ █▄▄▄█ █▀ ▀█  █▀▄    ▀██ ▄▄▀▄████"+
                              "████▄▄▄▄▄▄▄█▄█▄▄▄▄▄█▄▄██▄▄▄▄▄▄█▄█████",layout=_LogoLayout())

        txt_logo_attr = urwid.AttrMap(txt_logo,'bg','form')


        txt_OR = urwid.Text("OR",align="center")
        txt_OR_attr = urwid.AttrMap(txt_OR,'bg',focus_map='form')

        chk_scan_attr = urwid.AttrMap(self.chk_scan,'bg','form')

        self.btn_submit = urwid.Button("  BEGIN  ",user_data=self.thescramble)
        btn_submit_attr = urwid.AttrMap(self.btn_submit,'bg','form')

        self.btn_quit = urwid.Button("  EXIT  ",user_data=" ")
        btn_quit_attr = urwid.AttrMap(self.btn_quit,'btn_quit','form')

        right_form = urwid.GridFlow([txt_logo_attr,self.txt_scramble_attr,txt_OR_attr,chk_scan_attr,btn_submit_attr,btn_quit_attr],cell_width=88,v_sep=1,align='center',h_sep=0)
        right_form.set_focus(1)

        #RIGHT FORM ENDS

        #FULL BODY
        body1 = urwid.Columns([(2,urwid.Text(" ")),(76,gf1),right_form])
        body1.set_focus(2)
        right_form.set_focus(1)
        body1 = urwid.Filler(body1)
        body1=urwid.AttrMap(body1,"bg")
        #FULL BODY ENDS

        header1 = urwid.Text(("header", "Yet Another Cube Solver"), align="center")
        header1 = urwid.AttrMap(header1,"header")
        self.footer1 = urwid.Text(("header","statusline is here"))
        footer1attr = urwid.AttrMap(self.footer1,"header")

        #THEFRAME
        frame1 = urwid.Frame(body=body1, header=header1, footer=footer1attr)
        frame1.focus_position='body'
        #~THEFRAME
        return frame1

    def update_cube(self):
        logs.write("start update\n")
        self.left.set_text(self._left)
        self.right.set_text(self._right)
        self.up.set_text(self._up)
        self.down.set_text(self._down)
        self.front.set_text(self._front)
        self.back.set_text(self._back)
        logs.write("end update\n")

    def set_solution(self,soluchan):
        self.thesolution=soluchan
        temp=["The Solution is : "]
        for i,j in enumerate(soluchan.split()):
            temp+=[('G',j)]
        self.footer1.set_text(temp)

    def loading(self,loadcount,position):
        if loadcount == 0:
            tmp="-"
        if loadcount == 1:
            tmp="|"
        if loadcount == 2:
            tmp="/"

        temp=["  "+tmp+"  Solving : "]
        for i,j in enumerate(self.thesolution.split()):
            if i==position:
                temp+=[('header',j)]
            else:
                temp+=[('G',j)]
            self.footer1.set_text(temp)
