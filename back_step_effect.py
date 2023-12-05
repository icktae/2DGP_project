from pico2d import *

import game_framework
import game_world


class Back_stepEffect:
    image = None
    def __init__(self, x = 50, y = 0, velocity = 1):
        if Back_stepEffect.image == None:
            Back_stepEffect.image = load_image('image/cut2.png')

        self.x, self.y, self.velocity = 150, 550, velocity
        self.timer = get_time() + 0.5


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if get_time() >= self.timer:
            game_world.remove_object(self)


class Back_stepEffect2:
    image = None

    def __init__(self, x=50, y=500, velocity=1):
        if Back_stepEffect2.image == None:
            Back_stepEffect2.image = load_image('image/backstep_eff.png')

        self.x, self.y, self.velocity = x, y, velocity
        self.timer = get_time() + 0.3

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time
        if get_time() >= self.timer:
            game_world.remove_object(self)


