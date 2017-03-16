from  ev3dev.ev3 import *

from time import sleep


lA = LargeMotor('outA') #Mexe as rodas, desloca o papel
lB = LargeMotor('outB') #Sobe ou desce a caneta, para parar de escrever
mC = MediumMotor('outC') #Desloca a caneta lateralmente

def reset_position():
    lB.run_to_abs_pos(position_sp=70, speed_sp=200)

reset_position()
