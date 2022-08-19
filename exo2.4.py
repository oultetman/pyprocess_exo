from likeprocessing.processing import *

def setup():
    createCanvas(200, 200)
    background('darkblue')
    stroke('white')
    noLoop()

def draw():
    for i in range(20, 200 , 20 ):
        line(i , 20, i , 180)

run(globals())