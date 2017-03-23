from  ev3dev.ev3 import *

lA = LargeMotor('outA') #Mexe as rodas, desloca o papel
lB = LargeMotor('outB') #Sobe ou desce a caneta, para parar de escrever
mC = MediumMotor('outC') #Desloca a caneta lateralmente
positionC_max = -250
positionC_min = 70
positionB_min = 0
positionB_max = 80
defaultC_speed = 400
defaultB_speed = 200
defaultA_speed = 300

pen_raised = True

#mC functions
def reset_position():
    mC.run_to_abs_pos(position_sp=positionC_min, speed_sp=defaultC_speed)
    mC.wait_while('running')

def go_to_max_position_vertical():
    mC.run_to_abs_pos(position_sp=positionC_max, speed_sp=defaultC_speed)
    #mC.wait_while('running')

def go_to_half_max_position_vertical():
    mC.run_to_abs_pos(position_sp=positionC_max/2, speed_sp=defaultC_speed)


#lB functions
def drop_pen():
    "Baixa a caneta"
    global pen_raised
    if not pen_raised:
        return
    lB.run_to_abs_pos(position_sp=positionB_max, speed_sp=defaultB_speed)
    lB.wait_while('running')
    pen_raised = False

def rise_pen():
    "Levanta a caneta"
    global pen_raised
    if pen_raised:
        return
    lB.run_to_abs_pos(position_sp=positionB_max, speed_sp=defaultB_speed)
    lB.wait_while('running')
    pen_raised = True

#lA functions
def roll_forward():
    lA.run_to_rel_pos(position_sp=45, speed_sp=defaultA_speed)

def roll_half_forward():
    lA.run_to_rel_pos(position_sp=45/2, speed_sp=defaultA_speed)

def roll_backwards():
    lA.run_to_rel_pos(position_sp=-45, speed_sp=defaultA_speed)

def roll_half_backwards():
    lA.run_to_rel_pos(position_sp=-45/2, speed_sp=defaultA_speed)

def space():
    lA.run_to_rel_pos(position_sp=90, speed_sp=defaultA_speed)

def white_space():
    lA.run_to_rel_pos(position_sp=20, speed_sp=defaultA_speed)


#Prints
def print_vertical_up_line():
    drop_pen()
    go_to_max_position_vertical()
    rise_pen()


def print_vertical_down_line():
    drop_pen()
    reset_position()
    rise_pen()

def print_horizontal_line():
    drop_pen()
    roll_forward()
    rise_pen()

def print_diagonal_forward_line():#\
    go_to_max_position_vertical()
    roll_forward()
    mC.wait_while('running')
    lA.wait_while('running')

def print_diagonal_backwards_line():#/
    go_to_max_position_vertical()
    roll_backwards()
    mC.wait_while('running')
    lA.wait_while('running')


#mC.run_to_abs_pos(position_sp=-100, speed_sp=400)
#mC.wait_while('running')
reset_position()
#rise_pen()
#go_to_max_position_vertical()
#print_vertical_up_line()
print_diagonal_forward_line()
reset_position()
print_diagonal_backwards_line()
#reset_position()
#rise_pen()
#print_diagonal_backwards_line
#reset_position()
#rise_pen()
