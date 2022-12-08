from likeprocessing.processing import *
from time import sleep
def setup():
    createCanvas(500,200)
    background("grey")
    textAlign("center","center")

def draw():
    redraw()
    sleep(0.5)
    for i in range(10,440,40):
        fill(color(i//2))
        rect(i,10,40,40)
        fill("white")
        text(str(i),i,50,41,40)
        redraw()
        sleep(0.5)


run(globals())