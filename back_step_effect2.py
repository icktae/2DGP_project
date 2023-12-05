from pico2d import *

import game_world
import game_framework


class Back_stepEffect2:
    image = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Back_stepEffect2.image == None:
            Back_stepEffect2.image = load_image('image/backstep_eff.png')
        self.x, self.y, self.velocity = x, y, velocity

        self.timer = get_time() + 0.2

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * 300 * game_framework.frame_time

        if get_time() >= self.timer:
            game_world.remove_object(self)

