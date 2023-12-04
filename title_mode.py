import game_framework
from pico2d import *

import play_mode
from gameover import Gameover


def init():
     global image
     image = load_image('image/titlem.png')

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
               game_framework.quit()
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
               game_framework.change_mode(play_mode)


def draw():
     clear_canvas()
     image.draw(640, 350)
     update_canvas()