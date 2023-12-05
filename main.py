# from pico2d import open_canvas, delay, close_canvas
# import game_framework
#
# import play_mode as start_mode
#
# open_canvas(1700, 700)
# game_framework.run(start_mode)
# close_canvas()

from pico2d import open_canvas, delay, close_canvas
import game_framework

import title_mode as start_mode

open_canvas(1280, 700)
game_framework.run(start_mode)
close_canvas()