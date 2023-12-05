from pico2d import *
import game_framework

import game_world
import play_mode4
import title_mode

from boy import Boy
from enemy import Enemy
from speed_up_effect import SpeedUpEffect
from skill_icon import Skill
from stage3_image import Stage3
from touchdown import Touchdown
from gameover import Gameover

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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode4)


        else:
            server.boy.handle_event(event)


def init():
    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)
    game_world.add_collision_pair('boy:enemy', server.boy, None)

    server.stage3_image = Stage3()
    game_world.add_object(server.stage3_image, 1)

    server.skill_icon = Skill()
    game_world.add_object(server.skill_icon, 1)

    for _ in range(8):
        enemy = Enemy()
        game_world.add_object(enemy)
        game_world.add_collision_pair('boy:enemy', None, enemy)




def finish():
    game_world.clear()

    pass


def update():
    game_world.update()
    game_world.handle_collisions()

    # Check if boy's x value exceeds 2250
    if server.boy.x > 2250:
        server.touchdown = Touchdown()  # Create Skill instance
        game_world.add_object(server.touchdown, 1)
        Touchdown.touch_down_sound.play()

        for obj in game_world.all_objects():  # Get all objects in the game world
            if isinstance(obj, Enemy):
                obj.stop()

    if server.boy.y > 1098 or server.boy.y < 170 :
        server.gameover = Gameover()  # Create Skill instance
        game_world.add_object(server.gameover, 1)
        Gameover.game_over_sound.play()




def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
