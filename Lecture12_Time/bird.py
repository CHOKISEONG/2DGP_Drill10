from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)  # 1pixel = 3cm, 1m = 33.33 pixel
GRAVITY = 9.8  # 중력 가속도 (m/s²)

class Bird:
    image = None

    def __init__(self, x = 400, y = 300):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.face_dir = 1
        self.x, self.y = x, y
        self.width, self.height = 183,169
        self.my_width, self.my_height = 50, 50
        #self.xv = throwing_speed * math.cos(math.radians(throwing_angle))
        #self.yv = abs(throwing_speed * math.sin(math.radians(throwing_angle)))

    def draw(self):
        if self.face_dir == 1: #오른쪽 방향
            print('right dir')
            self.image.clip_composite_draw(0,0, 183, 169,0,'not flip',self.x, self.y, self.my_width, self.my_height)
        else:
            self.image.clip_composite_draw(0, 0, 183, 169, 0, 'v', self.x, self.y, self.my_width, self.my_height)

    def update(self):
        #self.yv -= GRAVITY * game_framework.frame_time  # m/s
        #self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        #self.y += self.yv * game_framework.frame_time * PIXEL_PER_METER

        if self.y < 60:
            game_world.remove_object(self)

