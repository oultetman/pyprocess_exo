from likeprocessing.processing import *


def setup():
    createCanvas(600, 200)
    background('SeaGreen')
    stroke("black")  # couleur des tracés



def draw():
    noFill()
    for i in range(25, 175, 25):
        square(25, 25, i)
    translate(200, 0)
    line(0, 0, 0, 200)

    rectMode("CENTER")
    for i in range(1, 7):
        square(100, 100, 25 * i)
    translate(200, 0)
    line(0, 0, 0, 200)

    rectMode("Corners")
    fill("#ff000000")
    for i in range(25, 175,25):
        square(i, i, 25)
    translate(200, 0)
    line(0, 0, 0, 200)

run(globals())
