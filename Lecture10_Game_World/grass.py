from pico2d import load_image


class Grass:
    def __init__(self, dx = 0, dy = 0):
        self.image = load_image('grass.png')
        self. x = 400 + dx
        self. y = 30 + dy

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
