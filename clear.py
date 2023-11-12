from pico2d import *

import boy


class Clear:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 128)

    def update(self):
        pass

    def draw(self):
        if boy.x >= 1600:
            self.state_machine.draw()
            self.font.draw(500, 350, 'TouchDown!', (255, 255, 255))
        elif boy.y <= 125 or boy.y >= 625:
            self.state_machine.draw()
            self.font.draw(500, 350, 'GameOver', (255, 255, 255))


    def get_bb(self):
        pass