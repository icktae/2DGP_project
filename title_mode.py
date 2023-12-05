import game_framework
from pico2d import *

import play_mode
import play_mode2
import play_mode3
import play_mode4
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


          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
               game_framework.change_mode(play_mode)
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
               game_framework.change_mode(play_mode2)
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
               game_framework.change_mode(play_mode3)
          elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_4):
               game_framework.change_mode(play_mode4)


          # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
          #      game_framework.change_mode(play_mode)


def draw():
     clear_canvas()
     image.draw(640, 350)
     update_canvas()