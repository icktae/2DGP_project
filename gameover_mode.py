import game_framework
from pico2d import *

import play_mode
import title_mode
from gameover import Gameover


def init():
     global image
     image = load_image('image/gameoverm.png')


def finish():
     global image
     del image
def update():
     pass


def handle_events():
     events = get_events()
     for event in events:
          if event.type == SDL_QUIT:
               game_framework.quit()
          elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
               game_framework.change_mode(title_mode)

def draw():
     clear_canvas()
     image.draw(640, 350)
     update_canvas()