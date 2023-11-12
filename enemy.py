import random
import game_framework
from pico2d import *

import game_world

# enemy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# enemy Action Speed
TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

class Enemy:
    image = None

    def load_image(self):
        if Enemy.image is None:
            Enemy.image = load_image('enemy.png')

    def __init__(self):
        self.x, self.y = random.randint(1700-800, 1500), random.randint(125, 625)
        self.frame = random.randint(0, 7)
        self.load_image()
        self.dir = random.choice([-1, 1])
        # self.size = 75

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        if self.y > 625:
            self.dir = -1
        elif self.y < 125:
            self.dir = 1

        self.x = clamp(800, self.x, 1600)
        self.y = clamp(125, self.y, 625)

    def draw(self):
        if self.dir < 0:
            Enemy.image.clip_draw(int(self.frame) * 100, 200, 100, 100, self.x, self.y)
        else:
            Enemy.image.clip_draw(int(self.frame) * 100, 200, 100, 100, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        if group == 'enemy:ball':
            self.size -= 100
            self.y = 100
            if self.size == 0:
                game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40