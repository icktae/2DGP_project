from pico2d import *

class Skill:
    def __init__(self):
        self.image = load_image('image/SKILL_IMAGE.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1150, 75)


