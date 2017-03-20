from lib import *

def draw_letter(letter='A'):
	print("draw letter A")
	drop_pen()
	print_vertical_up_line()
	print_horizontal_line()
	print_vertical_down_line()
	go_to_half_max_position_vertical()
	roll_backwards()
	print_horizontal_line()

def draw_letter(letter='B'):
	print("draw letter B")

draw_letter('A')
