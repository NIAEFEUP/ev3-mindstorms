#!/usr/bin/env python3
from ev3dev.ev3 import *

lA = LargeMotor('outA') #Mexe as rodas, desloca o papel
lB = LargeMotor('outB') #Sobe ou desce a caneta, para parar de escrever
mC = MediumMotor('outC') #Desloca a caneta lateralmente

#Para o motor A pode-se usar run_to_rel_pos(position_sp=<posicao relativ em graus>, speed_sp=<speed>)
#um speed que me parecia bom e não rápido demais foi por volta de 400 a 600, a posição relativa de rotação tem de se ver com o papel e a caneta
#Recomendo pensar em duas utilizações principais, fazer linha horizontal e puxar para o próximo carater (em que temos de dar um certo espaço).

#Para o motor B, -20 é em baixo e 80 em cima. Como a roda é pequena a precisão é muito baixa mas estes dois comandos funcionam +- bem:
#Para levantar a caneta: lB.run_to_abs_pos(position_sp=80, speed_sp=200)
#Para descer a caneta: lB.run_to_abs_pos(position_sp=-20, speed_sp=200)
#O problema da baixa precisão é que correndo qualquer um destes duas vezes seguidas fica numa posição desconhecida intermédia, às vezes até a oposta.

#Safe interval para o motor C : de 230 (lado do motor) a -200 (lado oposto) ish
#usar mC.run_to_abs_pos(position_sp=<pos>, speed_sp=<speed>), sendo que speed não deve ser mais de 200 senão perde precisão
#porém, como sao movimentos longos de ponta a ponta nao haveria muitos problemas
#consegue-se aceder a posição com motor.position, mas tem uma margem de erro de quase 20 em velocidade baixa (< 300)
#em velocidade mais alta, a mover ponta a ponta (como 800) chegou a ter mais de 40 de erro
#talvez seja mais facil ver apenas se a posicao e negativa ou nao, mas isso tem bastante margem de erro... Porem isso permite movimentos muito mais rapidos

#Para fazer pausas para esperar que o movimento do motor pare pode-se fazer motor.wait_while('running')

#Startup
#Baixar o levantador de caneta aka baixar a caneta
lB.run_to_abs_pos(position_sp=-20, speed_sp=200)

#Por a caneta do lado do motor
mC.run_to_abs_pos(position_sp=230, speed_sp=800)

#Teste de definicao de funcoes
#Nota: Devido a restrições físicas, levantar a caneta duas vezes seguidas baixa-a ligeiramente.
#O mesmo não acontece quando se baixa a caneta, vá-se lá saber porquê...
def baixarCaneta():
	"Baixa a caneta"
	lB.run_to_abs_pos(position_sp=-20, speed_sp=200)
	lB.wait_while('running')

def levantarCaneta():
	"Levanta a caneta"
	lB.run_to_abs_pos(position_sp=80, speed_sp=200)
	lB.wait_while('running')

#esta está a funcionar bem, os problemas de precisão parecem ser mínimos mas é preciso testar com papel e caneta
def fazerLinhaVerticalCompleta():
	"Leva a caneta de um lado ao outro da folha"
	if mC.position < 0:
		mC.run_to_abs_pos(position_sp=230, speed_sp=900)
	else:
		mC.run_to_abs_pos(position_sp=-200, speed_sp=900)
