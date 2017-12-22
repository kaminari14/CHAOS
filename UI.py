import urwid
import CubeClass

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
    if key in ('k','K'):
        cube.update_cube()


def on_submit(button,user_data):
    if(cube.chk_scan.get_state == True):
        cube.txt_scramble.set_edit_text("")
        #code for scanning goes here
    else:
        cube.footer1.set_text(cube.thescramble)

def on_quit(button,user_data):
    logs.write("-----cube array----")
    logs.write(str(cube.get_cube_array()))
    logs.write("----- end of cube array----")
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




cube.set_side("WRWOWBRYY", "U")
cube.set_side("OYWGOWYOR", "L")
cube.set_side("BYOGRWRYR", "R")
cube.set_side("GBBOBRYGG", "B")
cube.set_side("GGOBGWBRB", "F")
cube.set_side("YWWBYROOG", "D")
thescreen = cube.draw_cube()
urwid.connect_signal(cube.txt_scramble,'change',set_scramble)
urwid.connect_signal(cube.chk_scan,'change',clear_scramble)
urwid.connect_signal(cube.btn_quit,'click',on_quit,"")
urwid.connect_signal(cube.btn_submit,'click',on_submit,cube.thescramble)
ml = urwid.MainLoop(thescreen, palette, unhandled_input=onclick)
ml.screen.set_terminal_properties(colors=256)
ml.run()
