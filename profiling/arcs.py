from p5.core.primitives import arc
from p5.pmath.utils import QUARTER_PI, PI
from p5.sketch.userspace import run, size


def setup():
    size(720, 400)

def draw():
    offset = 0
    x = 0
    while x < 2 * PI:
        arc((50.0 + offset, 50.0), 50.0, 50.0, x, 2 * PI)
        arc((50.0 + offset, 100), 50, 50, x, 2 * PI, mode='OPEN')
        arc((50.0 + offset, 150), 50, 50, x, 2 * PI, mode='CHORD')
        arc((50.0 + offset, 200), 50, 50, x, 2 * PI, mode='PIE')
        x += QUARTER_PI
        offset += 50

if __name__ == '__main__':
    run()
