from pico2d import *

class Touchdown:
    touch_down_sound = None

    def __init__(self):
        self.image = load_image('image/TouchDown.png')

        if not Touchdown.touch_down_sound:
            Touchdown.touch_down_sound = load_wav('sound/touchdown_sound.mp3')
            Touchdown.touch_down_sound.set_volume(32)
            Touchdown.touch_down_sound.play(1)

        # self.bgm = load_music('sound/touchdown_sound.mp3')
        # self.bgm.set_volume(32)
        # self.bgm.play(1)

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 350)