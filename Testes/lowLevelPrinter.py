#!/usr/bin/env python3
from ev3dev.ev3 import *

lA = LargeMotor('outA') #Mexe as rodas, desloca o papel
lB = LargeMotor('outB') #Sobe ou desce a caneta, para parar de escrever
mC = MediumMotor('outC') #Desloca a caneta lateralmente

#vars globais para os movimentos porque tem de ser ajustado
origemCaneta = 30
limiteCaneta = -400
canetaBaixo = -30
canetaCima = 120

#Para o motor A pode-se usar run_to_rel_pos(position_sp=<posicao relativ em graus>, speed_sp=<speed>)
#um speed que me parecia bom e não rápido demais foi por volta de 400 a 600, a posição relativa de rotação tem de se ver com o papel e a caneta
#Recomendo pensar em duas utilizações principais, fazer linha horizontal e puxar para o próximo carater (em que temos de dar um certo espaço).

#Para o motor B, ver vars globais acima como para o motor C.
#Como a roda é pequena a precisão é muito baixa portanto há que usar velocidade baixa (<=200) e posições testadas
#O problema da baixa precisão é que movendo para um lado duas vezes seguidas fica numa posição desconhecida intermédia, às vezes até a oposta.

#Safe interval para o motor C : tem de ser testado e mudado nas vars acima

#Para fazer pausas para esperar que o movimento do motor pare pode-se fazer motor.wait_while('running')

#Startup
#Baixar o levantador de caneta aka baixar a caneta
lB.run_to_abs_pos(position_sp = canetaBaixo, speed_sp = 200)

#Por a caneta do lado do motor
mC.run_to_abs_pos(position_sp = origemCaneta, speed_sp = 800)

#Teste de definicao de funcoes
#Nota: Devido a restrições físicas, levantar a caneta duas vezes seguidas baixa-a ligeiramente.
#O mesmo não acontece quando se baixa a caneta, vá-se lá saber porquê...
def baixarCaneta():
	"Baixa a caneta"
	lB.run_to_abs_pos(position_sp = canetaBaixo, speed_sp=200)
	lB.wait_while('running')

def levantarCaneta():
	"Levanta a caneta"
	lB.run_to_abs_pos(position_sp= canetaCima, speed_sp=200)
	lB.wait_while('running')

#esta está a funcionar bem
def fazerLinhaVerticalCompleta():
	"Leva a caneta de um lado ao outro da folha"
	if mC.position < 0:
		mC.run_to_abs_pos(position_sp = origemCaneta, speed_sp=800)
		mC.wait_while('running')
	else:
		mC.run_to_abs_pos(position_sp = limiteCaneta, speed_sp=800)
		mC.wait_while('running')

