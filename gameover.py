from pico2d import *


class Gameover:
    active = False
    game_over_sound = None
    def __init__(self):
        self.image = load_image('image/Gameover.png')
        Gameover.active = True
        self.is_sound_playing = False

        if not Gameover.game_over_sound:
            Gameover.game_over_sound = load_wav('sound/gameover_sound.mp3')
            Gameover.game_over_sound.set_volume(32)
            Gameover.game_over_sound.play(1)



    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 350)
