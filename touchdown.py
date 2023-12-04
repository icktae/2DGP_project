from pico2d import *

class Touchdown:
    def __init__(self):
        self.image = load_image('image/TouchDown.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 350)