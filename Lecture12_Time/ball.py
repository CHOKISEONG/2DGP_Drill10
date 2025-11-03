from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)  # 1pixel = 3cm, 1m = 33.33 pixel
GRAVITY = 9.8  # 중력 가속도 (m/s²)

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, throwing_speed = 15, throwing_angle = 45):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = throwing_speed * math.cos(math.radians(throwing_angle))
        self.yv = abs(throwing_speed * math.sin(math.radians(throwing_angle)))

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.yv -= GRAVITY * game_framework.frame_time  # m/s
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        self.y += self.yv * game_framework.frame_time * PIXEL_PER_METER

        if self.y < 60:
            game_world.remove_object(self)

