from likeprocessing.processing import *


def setup():
    createCanvas(200, 200)
    background('darkorange')
    stroke('white')  # couleur des tracés
    noLoop()


def draw():
    for i in range(20, 200, 20):
        line(20, 20, i, 180)
        line(100, 100, 180, i)


run(globals())
