from pico2d import *
import game_framework

import game_world

from boy import Boy
from enemy import Enemy
from speed_up_effect import SpeedUpEffect
from skill_icon import Skill

# boy = None

from background import FixedBackground as Background

import server

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)


def init():
    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)
    game_world.add_collision_pair('boy:enemy', server.boy, None)


    # server.speed_up_effect = SpeedUpEffect()
    # game_world.add_object(server.speed_up_effect, 1)

    server.skill_icon = Skill()
    game_world.add_object(server.skill_icon, 1)

    for _ in range(11):
        enemy = Enemy()
        game_world.add_object(enemy)
        # game_world.add_collision_pair('enemy:ball', enemy, None)
        game_world.add_collision_pair('boy:enemy', None, enemy)




def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
