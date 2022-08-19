from likeprocessing.processing import *

def setup():
    createCanvas(610, 410)
    noStroke()
    frameRate(20)

def draw():
    background(255)
    fill((min(frameCount() % 510, 510 - frameCount() % 510), 0, 100))
    for i in range(1, width(), 20):
        for j in range(1, height(), 20):
            diametre = dist(mouseX(), mouseY(), i, j) // 6
            circle(i, j, diametre)
    if mouseIsPressed():
        noLoop()
run(globals())