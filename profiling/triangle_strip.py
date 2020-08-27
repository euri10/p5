from math import cos, radians, sin

from p5.core.attribs import background
from p5.core.constants import TRIANGLE_STRIP
from p5.core.vertex import begin_shape, vertex, end_shape
from p5.sketch.userspace import size, run

x = 0
y = 0
outsideRadius = 150
insideRadius = 100

def setup():
        size(720, 400)
        background(204)

        global x, y
        x = width / 2
        y = height / 2

def draw():
        global x, y, outsideRadius, insideRadius
        background(204)

        numPoints = 60
        angle = 0
        angleStep = 180.0 / numPoints

        begin_shape(TRIANGLE_STRIP)

        for i in range(numPoints + 1):
                px = x + cos(radians(angle)) * outsideRadius
                py = y + sin(radians(angle)) * outsideRadius
                angle += angleStep
                vertex(px, py)

                px = x + cos(radians(angle)) * insideRadius
                py = y + sin(radians(angle)) * insideRadius
                vertex(px, py)

                angle += angleStep

        end_shape()

if __name__ == '__main__':
        run()
