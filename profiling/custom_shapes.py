# Adapted from
import cProfile, random
import numpy as np

from p5.core.transforms import push_matrix, rotate, translate
from p5.core.vertex import begin_shape, vertex, end_shape
from p5.pmath.rand import random_uniform
from p5.pmath.utils import PI
from p5.sketch.userspace import size, run

FRAME_MAX = 1000

def setup():
    # Sets the screen to be 720 pixels wide and 400 pixels high
    size(720, 400)


def draw():
    if frame_count >= FRAME_MAX:
        exit()

    transform = lambda p, a, b: p * a + b
    # Points adapted from https://github.com/processing/p5.js/issues/3672
    points = np.asarray(((0, 0), (4, 0), (4, 1), (1, 1), (1, 2), (4, 2), (4, 3), (0, 3)))
    shapes_to_draw = 10
    for _ in range(shapes_to_draw):
        with push_matrix():
            begin_shape()
            rotate(random_uniform(0, 2 * PI))
            translate(random.randint(-200, 200), random.randint(-20, 20))
            transformed_pts = transform(points, np.asarray((20, 20)), np.asarray((width / 2, height / 2)))
            for p in transformed_pts:
                vertex(*p)
            end_shape("CLOSE")


if __name__ == '__main__':
    random.seed(42)
    pr = cProfile.Profile()
    pr.enable()
    try:
        run()
    except:
        pass
    pr.disable()
    pr.dump_stats("custom_shapes.prof")
