import math

from pico2d import *
from sdl2 import SDLK_UP, SDLK_DOWN, SDLK_q, SDLK_w

from speed_up_effect import SpeedUpEffect
from back_step_effect import Back_stepEffect

import game_world
import game_framework


import server

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def q_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_q


def q_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_q


def w_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w


def w_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w



def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:

    @staticmethod
    def enter(boy, e):
        print("stay")
        if boy.action == 0:
            boy.action = 2
        elif boy.action == 1:
            boy.action = 3
        boy.speed = 0
        boy.dir = 0
        boy.wait_time = get_time()
        if get_time() - boy.wait_time > 2:
            boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunRight:
    @staticmethod
    def enter(boy, e):
        print("run right")
        boy.action = 1
        boy.speed = RUN_SPEED_PPS
        boy.dir = 0

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunRightUp:
    @staticmethod
    def enter(boy, e):
        print("run right up")
        boy.action = 1
        boy.speed = RUN_SPEED_PPS
        boy.dir = math.pi / 4.0

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunRightDown:
    @staticmethod
    def enter(boy, e):
        print("run right down")
        boy.action = 1
        boy.speed = RUN_SPEED_PPS
        boy.dir = -math.pi / 4.0

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunLeft:
    @staticmethod
    def enter(boy, e):
        print("run left")
        boy.action = 0
        boy.speed = RUN_SPEED_PPS
        boy.dir = math.pi

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunLeftUp:
    @staticmethod
    def enter(boy, e):
        print("run left up")
        boy.action = 0
        boy.speed = RUN_SPEED_PPS
        boy.dir = math.pi * 3.0 / 4.0

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunLeftDown:
    @staticmethod
    def enter(boy, e):
        print("run left down")
        boy.action = 0
        boy.speed = RUN_SPEED_PPS
        boy.dir = - math.pi * 3.0 / 4.0

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunUp:
    @staticmethod
    def enter(boy, e):
        print("run up")
        if boy.action == 2:
            boy.action = 0
        elif boy.action == 3:
            boy.action = 1
        boy.speed = RUN_SPEED_PPS
        boy.dir = math.pi / 2.0

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass


class RunDown:
    @staticmethod
    def enter(boy, e):
        print("run down")
        if boy.action == 2:
            boy.action = 0
        elif boy.action == 3:
            boy.action = 1
        boy.speed = RUN_SPEED_PPS
        boy.dir = - math.pi / 2.0
        pass

    @staticmethod
    def exit(boy, e):
        if q_down(e):
            boy.q_effect()

        if w_down(e):
            boy.w_effect()

    @staticmethod
    def do(boy):
        pass
def draw_touch_down_text():
    pass




class Speedup:
    @staticmethod
    def enter(boy, e):
        print("speed up")
        boy.speedup_time = get_time() + 0.3
        boy.original_speed = boy.speed  # 원래 속도 저장
        boy.speed = boy.speed * 2.5

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if get_time() >= boy.speedup_time:
            boy.speed = boy.original_speed
            if boy.previous_state:
                boy.state_machine.cur_state = boy.previous_state
                boy.previous_state = None
            else:
                boy.state_machine.cur_state = boy.previous_state
                boy.previous_state = None


class Backstep:
    @staticmethod
    def enter(boy, e):
        print('backstep')
        boy.action = 1
        boy.speed = RUN_SPEED_PPS * 4
        boy.dir = math.pi
        boy.initial_x = boy.x
        boy.backstep_time = get_time() + 0.06

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.x -= boy.speed * game_framework.frame_time

        if get_time() >= boy.backstep_time :
            boy.state_machine.handle_event(('TIME_OUT', 0))

            if boy.previous_state:
                boy.state_machine.cur_state = boy.previous_state
                boy.previous_state = None
            else:
                boy.state_machine.handle_event(('TIME_OUT', 0))


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: RunRight,  right_up: RunLeft, left_down: RunLeft, left_up: RunRight, up_down: RunUp, up_up: RunDown, down_down: RunDown, down_up: RunUp,
                   w_down: Backstep, q_down: Speedup},

            RunRight: {right_up: Idle, left_down: Idle, up_down: RunRightUp, up_up: RunRightDown, down_down: RunRightDown, down_up: RunRightUp
                       ,w_down: Backstep, q_down: Speedup},
            RunRightUp: {right_up: RunUp, left_down: RunUp, down_down: RunRight, up_up: RunRight
                         ,w_down: Backstep, q_down: Speedup},
            RunRightDown: {right_up: RunDown, left_down: RunDown, down_up: RunRight, up_down: RunRight
                           ,w_down: Backstep, q_down: Speedup},

            RunLeft: {left_up: Idle, right_down: Idle, up_down: RunLeftUp,  up_up: RunLeftDown, down_down: RunLeftDown, down_up: RunLeftUp
                      ,w_down: Backstep, q_down: Speedup},
            RunLeftUp: {left_up: RunUp, right_down: RunUp, down_down: RunLeft,  up_up: RunLeft
                        ,w_down: Backstep, q_down: Speedup},
            RunLeftDown: {left_up: RunDown, right_down: RunDown, down_up: RunLeft, up_down: RunLeft
                         ,w_down: Backstep, q_down: Speedup},

            RunDown: {down_up: Idle, left_down: RunLeftDown, up_down: Idle, right_down: RunRightDown,
                      left_up: RunRightDown, right_up: RunLeftDown
                      ,w_down: Backstep, q_down: Speedup},
            RunUp: {up_up: Idle, left_down: RunLeftUp, down_down: Idle, right_down: RunRightUp, left_up: RunRightUp,
                    right_up: RunLeftUp
                   ,w_down: Backstep, q_down: Speedup},
            #
            Backstep: {right_down: RunRight, right_up: Idle, left_down: RunLeft, left_up: Idle, up_down: RunUp,
                       up_up: Idle, down_down: RunDown, down_up: Idle,
                       w_up: Idle, time_out: Idle},
            Speedup: {right_down: RunRight,  right_up: RunLeft, left_down: RunLeft, left_up: RunRight, up_down: RunUp, up_up: RunDown, down_down: RunDown, down_up: RunUp,
                      time_out: Idle, up_up: Idle, down_up: Idle},



             }





    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)
        self.boy.frame = (self.boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.boy.x += math.cos(self.boy.dir) * self.boy.speed * game_framework.frame_time
        self.boy.y += math.sin(self.boy.dir) * self.boy.speed * game_framework.frame_time

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)

                return True

        return False

class Boy:
    def __init__(self):
        self.x, self.y = 600, 620
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.size = 75
        self.dir_y = 0
        self.image = load_image('image/PLAYER.png')
        # self.font = load_font('ENCR10B.TTF', 128)
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        self.speed_up_effect = 'SpeedUpEffect'
        self.back_step_effect = "Back_stepEffect"

        self.previous_state = None



    def update(self):
        self.state_machine.update()
        self.x = clamp(50.0, self.x, server.background.w - 50.0)
        self.y = clamp(50.0, self.y, server.background.h - 50.0)


    def q_effect(self):
        if self.speed_up_effect == 'SpeedUpEffect':
            speed_up_effect = SpeedUpEffect(self.x, self.y)
            game_world.add_object(speed_up_effect)

    def w_effect(self):
        if self.back_step_effect == 'Back_stepEffect':
            back_step_effect = Back_stepEffect(self.x, self.y)
            game_world.add_object(back_step_effect)

    def handle_event(self, event):
        if (event.type == SDL_KEYDOWN and event.key == SDLK_q) or (event.type == SDL_KEYDOWN and event.key == SDLK_w):
            self.previous_state = self.state_machine.cur_state  # Store the previous state before q or w is pressed

        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, sx, sy)


        x1,y1,x2,y2 = self.get_bb()
        draw_rectangle(x1-server.background.window_left,y1-server.background.window_bottom,
                       x2-server.background.window_left,y2-server.background.window_bottom)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 30

    def handle_collision(self, group, other):

        if group == 'boy:enemy':
            game_framework.quit()