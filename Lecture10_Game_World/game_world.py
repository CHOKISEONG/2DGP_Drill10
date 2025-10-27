# layer 0 : Background object
# layer 1 : Foreground object
world = [[], []] # 게임내 객체들을 담는 리스트

def add_object(o, depth = 0):
    world[depth].append(o)
def add_objects(o, depth = 0):
    world[depth] += o

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise Exception('월드에 존재하지 않는 오브젝트를 삭제하려고 합니다.')


def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

