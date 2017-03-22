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


Código para se testar o alfabeto todo
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].upper()
for char in alfabeto:
	draw_letter(char)
'''


def draw_letter(letter='A'):
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


def draw_letter(letter="I"):
    drop_pen()
    go_to_max_position_vertical()
    rise_pen()
    reset_position()
    white_space()


def draw_letter(letter="J"):
    go_to_half_max_position_vertical()
    drop_pen()
    reset_position()
    roll_half_forward()
    go_to_max_position_vertical()
    roll_half_backwards()
    rise_pen()
    reset_position()
    roll_half_forward()
    white_space()


def draw_letter(letter="K"):
    drop_pen()
    go_to_max_position_vertical()
    rise_pen()
    reset_position()
    go_to_half_max_position_vertical()
    #meia diagonal para cima
    roll_half_backwards()
    reset_position()
    go_to_half_max_position_vertical()
    #meia digonal para baixo
    rise_pen()
    white_space()


def draw_letter(letter="L"):
    go_to_max_position_vertical()
    drop_pen()
    reset_position()
    roll_half_forward()
    rise_pen()
    white_space()


def draw_letter(letter="M"):
    drop_pen()
    go_to_max_position_vertical()
    #meia diagonal para baixo
    #meia diagonal para cima
    reset_position()
    rise_pen()
    white_space()


def draw_letter(letter="N"):
    drop_pen()
    go_to_max_position_vertical()
    print_diagonal_forward_line()
    go_to_max_position_vertical()
    rise_pen()
    reset_position()
    white_space()


def draw_letter(letter="O"):
    go_to_half_max_position_vertical()
    drop_pen()
    #meia diagonal para cima
    #meia diagonal para baixo
    #meia diagonal para tras para baixo
    #meia diagonal para tras para cima
    rise_pen()
    reset_position()
    roll_forward()
    white_space()