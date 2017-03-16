from  ev3dev.ev3 import *

from time import sleep


lA = LargeMotor('outA') #Mexe as rodas, desloca o papel
lB = LargeMotor('outB') #Sobe ou desce a caneta, para parar de escrever
mC = MediumMotor('outC') #Desloca a caneta lateralmente
positionC_max = -250
positionC_min = 70
positionB_min = 0
positionB_max = 80



#mC functions
def reset_position():
    mC.run_to_abs_pos(position_sp=positionC_min, speed_sp=400)
    mC.wait_while('running')

def go_to_max_position_vertical():
    mC.run_to_abs_pos(position_sp=positionC_max, speed_sp=400)
    mC.wait_while('running')

#lB functions
def drop_Pen():
    "Baixa a caneta"
    lB.run_to_abs_pos(position_sp=positionB_max, speed_sp=200)
    lB.wait_while('running')

def rise_Pen():
    "Levanta a caneta"
    lB.run_to_abs_pos(position_sp=positionB_max, speed_sp=200)
    lB.wait_while('running')

#lA functions
def roll_forward():
    lA.run_to_rel_pos(position_sp=45, speed_sp=300)

def roll_backwards():
    lA.run_to_rel_pos(position_sp=-45, speed_sp=300)

def space():
    lA.run_to_rel_pos(position_sp=90, speed_sp=300)
    

#mC.run_to_abs_pos(position_sp=100, speed_sp=400)
#mC.wait_while('running')
#reset_position()
#go_to_max_position_vertical()
#rise_Pen()
#drop_Pen()
