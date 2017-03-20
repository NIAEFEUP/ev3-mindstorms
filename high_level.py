from lib import *
import sys

'''
Este código vai ser depois responsavel por imprimir o nome da pessoa
passado como argumento na linha de  comandos para 1 só nome basta escrever
[python high_level.py ze] para mais do que um é preciso o seguinte
[python high_level.py ze tone] quando for para testar no robot descomenta-se
este codigo

name = sys.argv[1].upper()

for letter in name:
	draw_letter(letter)
'''

def draw_letter(letter='A'):
	print("draw letter A")
	drop_pen()
	print_vertical_up_line()
	print_horizontal_line()
	print_vertical_down_line()
	go_to_half_max_position_vertical()
	roll_backwards()
	print_horizontal_line()

def draw_letter(letter="B"):
	drop_pen()
	go_to_max_position_vertical()
	roll_forward()
	reset_position()
	roll_backwards()
	rise_pen()
	go_to_half_max_position_vertical()
	drop_pen()
	roll_forward()
	rise_pen()
	reset_position()
	white_space()

def draw_letter(letter="C"):
	roll_forward()
	drop_pen()
	roll_backwards()
	go_to_max_position_vertical()
	roll_forward()
	rise_pen()
	reset_position()
	white_space()

def draw_letter(letter="D"):
	drop_pen()
	go_to_max_position_vertical()
	roll_forward()
	reset_position()
	roll_backwards()
	rise_pen()
	roll_forward()
	white_space()

def draw_letter(letter="E"):
	roll_forward()
	drop_pen()
	roll_backwards()
	go_to_max_position_vertical()
	roll_forward()
	rise_pen()
	roll_backwards()
	go_to_half_max_position_vertical()
	drop_pen()
	roll_forward()
	rise_pen()
	reset_position()
	white_space()

def draw_letter(letter="F"):
	drop_pen()
	go_to_max_position_vertical()
	roll_forward()
	rise_pen()
	roll_backwards()
	go_to_half_max_position_vertical()
	drop_pen()
	roll_forward()
	rise_pen()
	reset_position()
	white_space()

def draw_letter(letter="G"):
	go_to_half_max_position_vertical()
	roll_half_forward()
	drop_pen()
	roll_half_forward()
	reset_position()
	roll_backwards()
	go_to_max_position_vertical()
	roll_forward()
	rise_pen()
	reset_position()
	white_space()

def draw_letter(letter="H"):
	drop_pen()
	go_to_max_position_vertical()
	rise_pen()
	go_to_half_max_position_vertical()
	drop_pen()
	roll_forward()
	rise_pen()
	go_to_max_position_vertical()
	drop_pen()
	reset_position()
	rise_pen()
	white_space()


draw_letter('A')
