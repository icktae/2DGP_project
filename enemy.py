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
            Enemy.image = load_image('image/SINRUZI.png')

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




    # def build_behavior_tree(self):
    #     a1 = Action('Set target location', self.set_target_location, 500, 50)
    #
    #     a2 = Action('Move to', self.move_to)
    #
    #     root = SEQ_move_to_target_location = Sequence('Move to target location', a1, a2)
    #
    #     a3 = Action('Set random location', self.set_random_location)
    #     root = SEQ_wander = Sequence('Wander', a3, a2)
    #
    #     c1 = Condition('소년이 근처에 있는가?', self.is_boy_nearby, 7)
    #     c2 = Condition('소년보다 공이 많은가?', self.more_ball_than_boy)
    #     a4 = Action('접근', self.move_to_boy)
    #     root = SEQ_chase_boy = Sequence('소년을 추적', c1, c2, a4)
    #
    #     c3 = Condition('소년보다 공이 적은가?', self.less_ball_than_boy)
    #     a5 = Action('run away', self.run_away_boy)
    #     root = SEQ_runaway_boy = Sequence('소년을 추적', c1, c3, a5)
    #     root = SEL_chase_or_flee = Selector('추적 또는 배회', SEQ_chase_boy, SEQ_runaway_boy, SEQ_wander)
    #
