import urwid
import threading
import queue
import CubeClass
import moves
import cross
import f2l
import oll
import pll


logs = CubeClass.logs
palette = [
    ("O", "", "", "", "h16", "h166"),
    ("G", "", "", "", "h16", "h02"),
    ("B", "", "", "", "h16", "h04"),
    ("R", "", "", "", "h16", "h01"),
    ("W", "", "", "", "h16", "h15"),
    ("Y", "", "", "", "h16", "h226"),
    ("bg", "", "", "", "h00", "h07"),
    ("hidebg", "", "", "", "h07", "h07"),
    ("header", "", "", "", "h16", "h15"),
    ("logo", "", "", "", "h46", "h00"),
    ("form", "", "", "", "h52", "h39"),
    ("btn_quit", "", "", "", "h15", "h01")

]
cube = CubeClass.cube()

def onclick(key):  # {
    if key in ('s', 'S'):
        #logs.write(str(cube_left))
        cube.set_side("WRWOWBRYY", "L")
        #logs.write(str(_left))
        #logs.write("kdfj\n")
    if key in ('u','U'):
        moves.up(cube.cubearray)
        cube.get_side_from_array(cube.cubearray)
        cube.update_cube()
    if key in ('k','K'):
        pass


def on_submit(button,user_data):
    global semaphorefinally,semaphorepll,semaphoreoll,semaphoref2,semaphorecross
    if(cube.chk_scan.get_state == True):
        cube.txt_scramble.set_edit_text("")
        #code for scanning goes here
    else:
        moves.breakscram(cube.thescramble,cube.cubearray)
        logs.write("----HERE KITTY----\n")
        logs.write(str(cube.cubearray))
        cube.get_side_from_array(cube.cubearray)
        cube.update_cube()
        cube.footer1.set_text(["Finding Solution for : ",("R",cube.thescramble)])
        logicthread.start()


def on_quit(button,user_data):
    raise urwid.ExitMainLoop()

def set_scramble(et,thenew):
    cube.thescramble=thenew

def clear_scramble(et,thenew):
    if(cube.chk_scan.get_state() == False):
        cube.txt_scramble_attr.set_attr_map({None:'hidebg'})

        cube.footer1.set_text('false')
    else:
        cube.txt_scramble_attr.set_attr_map({'hidebg':None})
        cube.footer1.set_text('true')

def get_full_sol(fullsol):

    fullsol=fullsol.replace("R R'", "")
    fullsol=fullsol.replace("L L'", "")
    fullsol=fullsol.replace("F F'", "")
    fullsol=fullsol.replace("D D'", "")
    fullsol=fullsol.replace("B B'", "")
    fullsol=fullsol.replace("U U'", "")
    fullsol=fullsol.replace("U U", "U2")
    fullsol=fullsol.replace("F F", "F2")
    fullsol=fullsol.replace("D D", "D2")
    fullsol=fullsol.replace("B B", "B2")
    fullsol=fullsol.replace("L L", "L2")
    fullsol=fullsol.replace("R R", "R2")
    fullsol=fullsol.replace("U2 U", "U'")
    fullsol=fullsol.replace("F2 F", "F'")
    fullsol=fullsol.replace("D2 D", "D'")
    fullsol=fullsol.replace("B2 B", "B'")
    fullsol=fullsol.replace("L2 L", "L'")
    fullsol=fullsol.replace("R2 R", "R'")
    fullsol=fullsol.replace("U2 U'", "U")
    fullsol=fullsol.replace("F2 F'", "F")
    fullsol=fullsol.replace("D2 D'", "D")
    fullsol=fullsol.replace("B2 B'", "B")
    fullsol=fullsol.replace("L2 L'", "L")
    fullsol=fullsol.replace("R2 R'", "R")
    return fullsol

def do_logic():
    cr=cross.makecross(cube.cubearray)
    f2=f2l.dof2l(cube.cubearray)
    ol=oll.solveoll(cube.cubearray)
    pl=pll.solvepll(cube.cubearray)
    cube.thesolution=get_full_sol(cr+" "+f2+" "+ol+" "+pl)
    cube.update_cube(cube.thesolution)

thescreen = cube.draw_cube()
logicthread=threading.Thread(target=do_logic)
urwid.connect_signal(cube.txt_scramble,'change',set_scramble)
urwid.connect_signal(cube.chk_scan,'change',clear_scramble)
urwid.connect_signal(cube.btn_quit,'click',on_quit,"")
urwid.connect_signal(cube.btn_submit,'click',on_submit,cube.thescramble)
ml = urwid.MainLoop(thescreen, palette, unhandled_input=onclick)
ml.screen.set_terminal_properties(colors=256)
ml.run()
