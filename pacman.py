from likeprocessing.processing import *

def setup():
    createCanvas(400,200)
    background("grey")
    ellipseMode("center")
    rectMode("center")
    angleMode("deg")

def draw():
    line(200,0,200,200)
    translate(50,0)
    fill("yellow")
    rotate(-45,(250,100))
    flip_h(100)
    line(200,100,400,100)
    circle(200,100,50)
    fill("white")
    circle(200,90,15)
    fill("black")
    circle(202, 90, 5)
    arc(200,100,50,50,350,370)
    rect(300,100,50,26)

run(globals())