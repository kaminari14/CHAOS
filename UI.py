import sys
import serial
import copy
import urwid
import threading
import CubeClass
import moves
import cross
import f2l
import oll
import pll


handle_check_serial = ""
handle_loading = ""
loadcount=0
logs = CubeClass.logs
# look_file = tempfile.TemporaryFile()

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


ardtopy={"a":moves.right,"b":moves.rightd,"c":moves.right2,
         "d":moves.left,"e":moves.leftd,"f":moves.left2,
         "g":moves.up,"h":moves.upd,"i":moves.up2,
         "j":moves.down,"k":moves.downd,"l":moves.down2,
         "m":moves.front,"n":moves.frontd,"o":moves.front2,
         "p":moves.back,"q":moves.backd,"r":moves.back2,
         "R":"a","R'":"b","R2":"c","L":"d","L'":"e","L2":"f","U":"g","U'":"h","U2":"i","D":"j","D'":"k","D2":"l","F":"m","F'":"n","F2":"o","B":"p","B'":"q","B2":"r"}

def _py_to_ard(itterable):
    ans=""
    for i in itterable:
        if i in ardtopy:
            ans+=ardtopy[i]
    ans+="z\n"
    return ans


cube = CubeClass.cube()

def onclick(key):  # {
    if key in ('s', 'S'):
        # logs.write(str(cube_left))
        cube.set_side("WRWOWBRYY", "L")
        # logs.write(str(_left))
        # logs.write("kdfj\n")
    if key in ('u', 'U'):
        moves.up(cube.cubearray)
        cube.get_side_from_array(cube.cubearray)
        cube.update_cube()
    if key in ('k', 'K'):
        pass


def on_submit(button, user_data):
    if (cube.chk_scan.get_state == True):
        cube.txt_scramble.set_edit_text("")
        # code for scanning goes here
    else:
        moves.breakscram(cube.thescramble, cube.cubearray)
        logs.write(str(cube.cubearray))
        cube.get_side_from_array(cube.cubearray)
        cube.update_cube()
        cube.footer1.set_text(["Finding Solution for : ", ("R", cube.thescramble)])
        #logicthread.start()
        ml.draw_screen()
        do_logic()# sets solution

def on_quit(button, user_data):
    raise urwid.ExitMainLoop()


def set_scramble(et, thenew):
    cube.thescramble = thenew


def clear_scramble(et, thenew):
    if (cube.chk_scan.get_state() == False):
        cube.txt_scramble_attr.set_attr_map({None: 'hidebg'})

        cube.footer1.set_text('false')
    else:
        cube.txt_scramble_attr.set_attr_map({'hidebg': None})
        cube.footer1.set_text('true')


def get_full_sol(fullsol):
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
    return fullsol


def do_logic():
    cubearraycopy=copy.deepcopy(cube.cubearray)
    cr = cross.makecross(cubearraycopy)
    f2 = f2l.dof2l(cubearraycopy)
    ol = oll.solveoll(cubearraycopy)
    pl = pll.solvepll(cubearraycopy)
    cube.set_solution(get_full_sol(cr + " " + f2 + " " + ol + " " + pl))
    kellogs.write(_py_to_ard(cube.thesolution.split(" ")).encode())
    global handle_check_serial
    handle_check_serial=ml.set_alarm_in(1,check_serial,"")
    handle_loading=ml.set_alarm_in(0.5,loadingstatus,"")



def check_serial(theml ,data):
    global  handle_check_serial
    currentover = kellogs.read().decode()
    if currentover in ardtopy:
        ardtopy[currentover](cube.cubearray) # move virtualcube
        cube.get_side_from_array(cube.cubearray)
        cube.update_cube()
        cube.position=cube.position+1
    if currentover == 'z':
        theml.remove_alarm(handle_loading)
        cube.footer1.set_text("finito")
        theml.remove_alarm(handle_check_serial)
    else:
        handle_check_serial=theml.set_alarm_in(1,check_serial,"")


def loadingstatus(theml,data):
    global loadcount
    if loadcount>2:
        loadcount=0
    loadcount=loadcount+1
    cube.loading(loadcount)
    theml.draw_screen()
    handle_loading=theml.set_alarm_in(0.5,loadingstatus,"")

def testpopup(data):
    logs.write("VSAUCE::"+data)
    cube.open_pop_up()


if len(sys.argv)!=2:
    valid=False
else:
    valid=True
    port=sys.argv[1]
    kellogs=serial.Serial(port=port,timeout=1)

if valid:
    thescreen = cube.draw_cube()
    #logicthread = threading.Thread(target=do_logic)
    urwid.connect_signal(cube.txt_scramble, 'change', set_scramble)
    urwid.connect_signal(cube.chk_scan, 'change', clear_scramble)
    urwid.connect_signal(cube.btn_quit, 'click', on_quit, "")
    urwid.connect_signal(cube.btn_submit, 'click', on_submit, cube.thescramble)
    #urwid.connect_signal(cube.gf1.contents[1][0],'',testpopup,"michael here")
    ml = urwid.MainLoop(thescreen, palette, unhandled_input=onclick,pop_ups=True)
    ml.screen.set_terminal_properties(colors=256)
    urwid.set_encoding("utf-8")
    ml.run()
else:
    print("::usage::\n"+sys.argv[0]+" [com device]\nWhere:\n[com device] -> Arduino Serial Communication Port\n\n")
    print("example:\n\n"+sys.argv[0]+" COM3\n"+sys.argv[0]+" /dev/ttyAM0")
