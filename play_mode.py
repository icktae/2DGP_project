import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from clear import Clear
from ball import Ball
from enemy import Enemy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global grass
    global boy
    global enemy

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    enemys = [Enemy() for _ in range(10)]
    game_world.add_objects(enemys, 1)
    game_world.add_collision_pair('boy:enemy', boy, None)
    for enemy in enemys:
       game_world.add_collision_pair('boy:enemy', None, enemy)
       game_world.add_collision_pair('enemy:ball', enemy, None)

    # fill here
    # global balls
    # balls = [Ball(random.randint(100, 1600 - 100), 60, 0) for _ in range(30)]
    # game_world.add_objects(balls, 1)
    #
    #
    #
    # game_world.add_collision_pair('boy:ball', boy, None)
    # for ball in balls:
    #     game_world.add_collision_pair('boy:ball', None, ball)




def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
