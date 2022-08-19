from likeprocessing.processing import *

def setup():
    createCanvas(1000, 200)
    background('gold')
    noFill()

def draw():
    for i in range(60, 160, 20):
        circle(100, 100, i)

    translate(200, 0)
    line(0, 0, 0, 200)

    # Programme 2

    for i in range(60, 160, 20):
        circle(i, 100, 80)

    translate(200, 0)
    line(0, 0, 0, 200)

    # Programme 3

    for i in range(60, 160, 20):
        circle(i, i, 80)

    translate(200, 0)
    line(0, 0, 0, 200)

    # Programme 4

    for i in range(60, 160, 20):
        circle(100, i, 160 - i)

    translate(200, 0)
    line(0, 0, 0, 200)

    # Programme 5

    for i in range(60, 160, 20):
        circle(i - 20, 100, i)

run(globals())