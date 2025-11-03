from pico2d import *
import game_world
import game_framework
from random import randint

PIXEL_PER_METER = (1.0 / 0.03)  # 1pixel = 3cm, 1m = 33.33 pixel
ACTION_PER_TIME = 1
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self, x = randint(50,200), y = randint(200,400)):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.face_dir = 1
        self.x, self.y = x, y
        self.width, self.height = 183,169
        self.my_width, self.my_height = 50, 50
        self.speed = 10 # 새의 속도는 1초에 10
        self.frame = 0
        self.theta = 0

    def draw(self):
        if self.face_dir == 1: #오른쪽 방향
            print(int(self.frame) // 5)
            self.image.clip_composite_draw((int(self.frame) % 5) * 183 ,(2 - int(self.frame) // 5) * 169, 183, 169
                                           ,0,'not flip',self.x, self.y, self.my_width, self.my_height)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 183 ,(2 - int(self.frame) // 5) * 169, 183, 169
                                           ,0,'h',self.x, self.y, self.my_width, self.my_height)

    def update(self):
        #self.yv -= GRAVITY * game_framework.frame_time  # m/s
        #self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        #self.y += self.yv * game_framework.frame_time * PIXEL_PER_METER
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.speed * game_framework.frame_time * PIXEL_PER_METER
        if self.x > 1500 or self.x < 30:
            self.speed = -self.speed
            self.face_dir = -self.face_dir



