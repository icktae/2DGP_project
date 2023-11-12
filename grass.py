from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('field_test2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(850, 350)


    def get_bb(self):
        return 0, 0, 1600 - 1, 50


