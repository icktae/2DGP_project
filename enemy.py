from pico2d import *

import random
import math
import game_framework
import game_world
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
import play_mode

from gameover import Gameover

import server

# enemy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk', 'Idle']


class Enemy:
    images = None

    def load_images(self):
        if Enemy.images == None:
            Enemy.images = {}
            for name in animation_names:
                Enemy.images[name] = [load_image("./enemy/" + name + " (%d)" % i + ".png") for i in range(1, 11)]
    def __init__(self, x = None, y = None):
        self.x = x if x else random.randint(1200, 1900)
        self.y = y if y else random.randint(200, 1050)
        self.origin_x = self.x  # 원래 위치 x좌표 초기화
        self.origin_y = self.y
        self.size = clamp(1, random.random() * 2, 1.3)
        self.load_images()
        self.dir = 0.0  # radian 값으로 방향을 표시
        self.speed = random.randint(0, 1)
        self.frame = random.randint(0, 9)
        self.state = 'Idle'

        self.tx, self.ty = 0, 0
        self.build_behavior_tree()
        self.loc_no = 0

        self.reached_goal = False




    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if not self.reached_goal:  # Only run behavior tree if goal is not reached
            self.bt.run()


    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if math.cos(self.dir) < 0:
            Enemy.images[self.state][int(self.frame)].composite_draw(0, 'h', sx, sy, 100 * self.size, 100 * self.size)
        else:
            Enemy.images[self.state][int(self.frame)].draw(sx, sy, 100 * self.size, 100 * self.size)

        x1, y1, x2, y2 = self.get_bb()
        draw_rectangle(x1 - server.background.window_left, y1 - server.background.window_bottom,
                       x2 - server.background.window_left, y2 - server.background.window_bottom)


    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        if group == 'enemy:boy':
            gameover = Gameover()  # Create Gameover instance
            game_world.add_object(gameover, 1)
            game_world.remove_object(self)

    def set_target_location(self, x=None, y=None):
        if not x or not y:
            raise ValueError('Location should be given')
        self.tx, self.ty = x, y
        return BehaviorTree.SUCCESS

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2




    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        self.speed = RUN_SPEED_PPS * random.uniform(0, 3)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

    def move_to(self, r=0.5):
        self.state = 'Walk'
        self.move_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.tx, self.ty, self.x, self.y, r):
            self.set_patrol_location()
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def set_random_location(self):
        # select random location around boy
        self.tx = random.randint(int(server.boy.x) - 00, int(server.boy.x) + 00)
        self.ty = random.randint(int(server.boy.y) - 00, int(server.boy.y) + 00)
        return BehaviorTree.SUCCESS

    def is_boy_nearby(self, distance):
        if self.distance_less_than(server.boy.x, server.boy.y, self.x, self.y, distance):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_to_boy(self, r=0.5):
        self.state = 'Walk'
        self.move_slightly_to(server.boy.x, server.boy.y)
        if self.distance_less_than(server.boy.x * random.uniform(1,3), server.boy.y * random.uniform(1,3), self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def wait(self):
        self.state = 'Idle'
        self.frame = 0
        return BehaviorTree.SUCCESS

    def is_boy_far_away(self, distance):
        if self.distance_less_than(server.boy.x, server.boy.y, self.x, self.y, distance):
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS

    def move_to_origin(self):
        self.state = 'Walk'
        self.move_slightly_to(self.origin_x, self.origin_y)
        if self.distance_less_than(self.origin_x, self.origin_y, self.x, self.y, 1):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def is_boy_reached_goal(self):
        if server.boy.x > 2250:
            return BehaviorTree.SUCCESS

        else:
            return BehaviorTree.FAIL



    def stop(self):
        self.speed = 0
        self.reached_goal = True

    def set_patrol_location(self):
        self.tx = random.randint(int(self.x) - 100, int(self.x) + 100)
        self.ty = random.randint(int(self.y) - 100, int(self.y) + 100)
        return BehaviorTree.SUCCESS



    def build_behavior_tree(self):
        a1 = Action('대기', self.wait)
        c1 = Condition('소년이 20미터 이내에 있는가?', self.is_boy_nearby, 15)
        a2 = Action('접근', self.move_to_boy)
        SEQ_chase_boy = Sequence('소년을 추적', c1, a2)

        c2 = Condition('소년이 15미터 밖에 있는가?', self.is_boy_far_away, 15)
        a3 = Action('원래 위치로 돌아가기', self.move_to_origin)
        SEQ_return_origin = Sequence('원래 위치로 돌아가기', c2, a3)

        c3 = Condition('소년이 목표에 도달했는가?', self.is_boy_reached_goal)
        a4 = Action('멈춤', self.stop)
        SEQ_stop = Sequence('멈춤', c3, a4)

        root = SEL_chase_or_return_or_stop = Selector('추적 또는 복귀 또는 멈춤', SEQ_chase_boy, SEQ_return_origin, SEQ_stop)

        self.bt = BehaviorTree(root)