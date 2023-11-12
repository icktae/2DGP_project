from pico2d import *
from sdl2 import SDLK_UP, SDLK_DOWN, SDLK_q, SDLK_w

from ball import Ball
import game_world
import game_framework


# state event check
# ( state event type, event value )

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
        if boy.face_dir == -1:
            boy.action = 2
        elif boy.face_dir == 1:
            boy.action = 3
        boy.dir = 0
        boy.dir_y = 0
        boy.frame = 0
        boy.wait_time = get_time()
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if get_time() - boy.wait_time > 2:
            boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)


def draw_touch_down_text():
    pass


class Run:

    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 128)

    @staticmethod
    def enter(boy, e):
        print("run")
        boy.dir_y = 0
        if right_down(e) or right_up(e):  # 오른쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = 1, 1, 1
        elif left_down(e) or left_up(e):  # 왼쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = -1, 0, -1
        elif up_down(e):  # 위쪽으로 RUN
            boy.dir_y, boy.action, boy.face_dir = 1, 1, boy.face_dir
        elif down_down(e):  # 아래쪽으로 RUN
            boy.dir_y, boy.action, boy.face_dir = -1, 1, boy.face_dir

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.y += boy.dir_y * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1700)
        boy.y = clamp(125, boy.y, 625)
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if boy.dir == 1:
            boy.action = 1
        elif boy.dir == -1:
            boy.action = 0
        elif boy.dir_y == 1:
            boy.action = 1
        elif boy.dir_y == -1:
            boy.action = 1

        # boy.x -> over  game clear
        if boy.x >= 1600 :
            print("Touch Down")


        # boy.y -> under 25, over 625 game over
        if boy.y <= 125 or boy.y >= 625:
            print('Game Over')



    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class Speedup:
    @staticmethod
    def enter(boy, e):
        print("speed up")
        boy.speedup_time = get_time() + 0.4

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        speed_multiplier = 2

        boy.x += boy.dir * RUN_SPEED_PPS * speed_multiplier * game_framework.frame_time
        boy.y += boy.dir_y * RUN_SPEED_PPS * speed_multiplier * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1700)
        boy.y = clamp(125, boy.y, 625)
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if boy.dir == -1:
            boy.action = 0

        # boy.x -> over  game clear
        if boy.x >= 1600 :
            print("Touch Down")


        # boy.y -> under 25, over 625 game over
        if boy.y <= 125 or boy.y >= 625:
            print('Game Over')

        if get_time() >= boy.speedup_time :
            boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)



class Backstep:
    @staticmethod
    def enter(boy, e):
        print("backstep")
        boy.speedup_time = get_time() + 0.04


    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        speed_multiplier = 10

        boy.x -= boy.dir * RUN_SPEED_PPS * speed_multiplier * game_framework.frame_time

        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8


        if get_time() >= boy.speedup_time:
            boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)






class Dash :
    pass


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, up_down: Run, down_down: Run, q_down: Speedup, w_down: Backstep,
                   left_up: Idle, right_up: Idle, up_up: Idle, down_up: Idle, space_down: Idle, q_up : Speedup, time_out : Run},
            Run: {right_down: Run, left_down: Run, up_down: Run, down_down: Run, q_down: Speedup, w_down: Backstep,
                  right_up: Idle, left_up: Idle, up_up: Idle, down_up: Idle, space_down: Run, q_up: Speedup, time_out : Run},
            Speedup: {right_down: Run, left_down: Run, up_down: Run, down_down: Run, w_down: Backstep,
                   right_up: Idle, left_up: Idle, up_up: Idle, down_up: Idle, space_down: Idle, time_out : Run},
            Backstep: {right_down: Run, left_down: Run, up_down: Run, down_down: Run,
                   right_up: Idle, left_up: Idle, up_up: Idle, down_up: Idle, space_down: Idle, time_out : Run}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)


    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)

class Boy:
    def __init__(self):
        self.x, self.y = 600, 350
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.dir_y = 0
        self.image = load_image('sonic_animation.png')
        self.font = load_font('ENCR10B.TTF', 128)
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.ball_count = 10

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def clear_draw(self):
        if self.x >= 1600:
            self.font.draw(500, 350, 'TouchDown!', (255, 255, 255))
            draw_rectangle(*self.get_bb())

    def over_draw(self):
        if self.y <= 125 or self.y >= 625:
            self.font.draw(500, 350, 'GameOver', (255, 255, 255))
            draw_rectangle(*self.get_bb())


    # fill here
    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 50

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            self.ball_count += 1

        if group == 'boy:zombie':
            game_framework.quit()