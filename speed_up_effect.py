from pico2d import *

import game_world


class SpeedUpEffect:
    image = None
    def __init__(self, x = 175, y = 130, velocity = 1):
        if SpeedUpEffect.image == None:
            SpeedUpEffect.image = load_image('image/cut1_1.png')
        self.x, self.y, self.velocity = 640, 350, velocity
        self.timer = get_time() + 0.5


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if get_time() >= self.timer:
            game_world.remove_object(self)

