from lib import *
import sys

'''
Este codigo vai ser depois responsavel por imprimir o nome da pessoa
passado como argumento na linha de  comandos para 1 so nome basta escrever
[python high_level.py ze] para mais do que um e preciso o seguinte
[python high_level.py ze tone] quando for para testar no robot descomenta-se
este codigo

name = sys.argv[1].upper()

for letter in name:
	draw_letter(letter)


Codigo para se testar o alfabeto todo
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].upper()
for char in alfabeto:
	draw_letter(char)
'''

reset_position()
drop_pen()
go_to_max_position_vertical()

def draw_letter(letter="A"):
    drop_pen()
    print_vertical_up_line()
    print_horizontal_line()
    print_vertical_down_line()
    go_to_half_max_position_vertical()
    roll_backwards()
    print_horizontal_line()

#draw_letter("A")

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

def draw_letter(letter="P"):
    drop_pen()
    go_to_half_max_position_vertical()
    roll_half_forward()
    go_to_max_position_vertical()
    roll_half_backwards()
    reset_position()
    rise_pen()
    roll_half_forward()
    white_space()

def draw_letter(letter="Q"):
    drop_pen()
    go_to_max_position_vertical()
    roll_forward()
    go_to_half_max_position_vertical()
    #meia diagonal para baixo para tras
    roll_half_backwards()
    rise_pen()
    go_to_half_max_position_vertical()
    roll_half_forward()
    drop_pen()
    #meia diagonal para frente para baixo
    rise_pen()
    white_space()

def draw_letter(letter="R"):
    drop_pen()
    go_to_max_position_vertical()
    roll_half_forward()
    go_to_half_max_position_vertical()
    roll_half_backwards()
    #meia diagonal para frente para baixo
    rise_pen()
    white_space()

def draw_letter(letter="S"):
    drop_pen()
    roll_half_forward()
    go_to_half_max_position_vertical()
    roll_half_backwards()
    go_to_max_position_vertical()
    roll_half_forward()
    rise_pen()
    reset_position()
    white_space()

def draw_letter(letter="T"):
    roll_half_forward()
    drop_pen()
    go_to_max_position_vertical()
    roll_half_backwards()
    roll_forward()
    rise_pen()
    reset_position()
    white_space()

def draw_letter(letter="U"):
    go_to_max_position_vertical()
    drop_pen()
    reset_position()
    roll_half_forward()
    go_to_max_position_vertical()
    rise_pen()
    reset_position()
    white_space()

def draw_letter(letter="V"):
    go_to_max_position_vertical()
    drop_pen()
    #diagonal 2:1 para baixo frente
    #diagonal 2:1 para cima frente
    rise_pen()
    reset_position()
    white_space()

def draw_letter(letter="W"):
    go_to_max_position_vertical()
    drop_pen()
    reset_position()
    rise_pen()
    go_to_half_max_position_vertical()
    roll_half_forward()
    drop_pen()
    #print_half_diagonal_backwards()    #/
    rise_pen()
    go_to_half_max_position_vertical()
    roll_half_forward()
    drop_pen()
    #print_half_diagonal_forward()      #\
    go_to_max_position_vertical()
    rise_pen()
    reset_position()
    white_space()


def draw_letter(letter="X"):
    go_to_max_position_vertical()
    drop_pen()
    print_diagonal_forward_line()
    rise_pen()
    go_to_max_position_vertical()
    drop_pen()
    print_diagonal_backwards_line()
    rise_pen()
    roll_forward()
    reset_position()
    white_space()


def draw_letter(letter="Y"):
    go_to_max_position_vertical()
    drop_pen()
    #print_half_diagonal_forward()      #\
    reset_position()
    rise_pen()
    roll_half_forward()
    go_to_max_position_vertical()
    drop_pen()
    #print_half_diagonal_backwards()    #/
    rise_pen()
    roll_half_forward()
    reset_position()
    white_space()

def draw_letter(letter="Z"):
    go_to_max_position_vertical()
    drop_pen()
    roll_forward()
    print_diagonal_backwards_line()
    roll_forward()
    rise_pen()
    reset_position()
    white_space()