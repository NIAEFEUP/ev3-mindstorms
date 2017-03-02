
from  ev3dev.ev3 import *

from time import sleep

dict = {0: 'No Color' , 1: 'Black', 2:'Blue', 3:'Green',4:'Yellow',5:'Red',6:'White',7:'Brown'} 

i = 0

while(True):
	motor1=LargeMotor('outA')
	motor2=LargeMotor('outB')
	sensor=TouchSensor('in1')
	irsensor=InfraredSensor('in2')
	#colorsensor=ColorSensor('in3')
	if(i%100 == 0):
		print("WAITING FOR INPUT")
	
	while((sensor.value(0) == 1) ):
		#color=colorsensor.value(0)
		#print('Color is :', dict[color])
		distance = irsensor.value(0)
		#print(distance)
		motor1.run_timed(time_sp=100,speed_sp= distance*10.5%1051)
		motor2.run_timed(time_sp=100,speed_sp= distance*10.5%1051)
		i = i -1
	i = i + 1

