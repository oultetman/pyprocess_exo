import likeprocessing.processing
from likeprocessing.processing import *

plateau = [[0 for j in range(6)] for i in range(6)]
taille_case = 50
dx, dy = 35, 35


def draw_fixe(i, j):
    fill("white")
    circle(j * taille_case + dx, i * taille_case + dy, 60)
    circle(j * taille_case + dx, i * taille_case + dy, 52)


def draw_2_vert(x, y, angle: int):
    """Angle peut prendre deux valeurs 0 ou 270"""
    if angle not in [0, 270]: raise ValueError
    fill("green")
    diametre = (14 * taille_case) // 10
    if angle == 0:

        circle_arc(x, y, diametre, PI / 4, 7 * PI / 4)
        circle_arc(x + taille_case, y - taille_case, diametre, 5 * PI / 4, 7 * PI / 4)
        circle_arc(x + taille_case, y + taille_case, diametre, PI / 4, 3 * PI / 4)
        circle_arc(x + 2 * taille_case, y, diametre, 5 * PI / 4, 3 * PI / 4)
        circle(x, y, 60)
        circle(x + 2 * taille_case, y, 60)
    else:
        circle_arc(x, y, diametre, 7 * PI / 4, 5 * PI / 4)
        circle_arc(x + taille_case, y + taille_case, diametre, 3 * PI / 4, 5 * PI / 4)
        circle_arc(x - taille_case, y + taille_case, diametre, 7 * PI / 4, PI / 4)
        circle_arc(x, y + 2 * taille_case, diametre, 3 * PI / 4, PI / 4)
        circle(x, y, 60)
        circle(x, y + 2 * taille_case, 60)


def draw_3_bleu(x, y, angle: int):
    """Angle peut prendre deux valeurs 0 ou 270"""
    if angle not in [0, 270]: raise ValueError
    noFill()
    strokWeight(1)
    diametre = (14 * taille_case) // 10
    rotate(-likeprocessing.processing.PI/2,(x,y))
    fill("grey")
    pts = arc_points(x, y, diametre, diametre, PI / 4, 7 * PI / 4)
    pts += arc_points(x + taille_case, y + taille_case, diametre, diametre, 3 * PI / 4, PI / 4, False)
    pts += arc_points(x + 2 * taille_case, y, diametre, diametre, 5 * PI / 4, 7 * PI / 4)
    pts += arc_points(x + 3 * taille_case, y + taille_case, diametre, diametre, 3 * PI / 4, PI / 4, False)
    pts += arc_points(x + 4 * taille_case, y, diametre, diametre, 5 * PI / 4, 3 * PI / 4)
    pts+=arc_points(x + 3 * taille_case, y - taille_case, diametre,diametre, 7 * PI / 4, 5 * PI / 4,False)
    pts+=arc_points(x + 2 * taille_case, y, diametre,diametre, PI / 4, 3 * PI / 4)
    pts += arc_points(x + taille_case, y - taille_case, diametre, diametre, 7 * PI / 4, 5 * PI / 4,False)
    polygone(pts)
    fill("blue")
    noStroke()
    circle(x, y, 60)
    circle(x + 2 * taille_case, y, 60)
    circle(x + 4 * taille_case, y, 60)
    rotate(0)


def draw_angle_violet(x, y, angle: int):
    """Angle peut prendre quatre valeurs 0 , 90, 180 ou 270"""
    if angle not in [0, 90, 180, 270]: raise ValueError
    fill("purple")
    diametre = (14 * taille_case) // 10
    if angle == 0:
        circle_arc(x, y, diametre, PI / 4, 7 * PI / 4)
        circle_arc(x + taille_case, y - taille_case, diametre, 5 * PI / 4, 7 * PI / 4)
        circle_arc(x + taille_case, y + taille_case, diametre, PI / 4, 3 * PI / 4)
        circle_arc(x + 3 * taille_case, y - taille_case, diametre, 5 * PI / 4, 7 * PI / 4)
        circle_arc(x + 3 * taille_case, y + taille_case, diametre, PI / 4, 3 * PI / 4)
        circle_arc(x + 2 * taille_case, y, diametre, PI / 4, 3 * PI / 4)
        circle_arc(x + 2 * taille_case, y, diametre, 5 * PI / 4, 7 * PI / 4)
        circle_arc(x + 4 * taille_case, y, diametre, 5 * PI / 4, 3 * PI / 4)
        circle(x, y, 60)
        circle(x + 2 * taille_case, y, 60)
        circle(x + 4 * taille_case, y, 60)


def draw_2_rouge(x, y, angle: str):
    if angle not in [225, 315]: raise ValueError
    diametre = (14 * taille_case) // 10
    fill("red")
    if angle == 315:
        circle_arc(x, y, diametre, 0, 6 * PI / 4)
        circle_arc(x + diametre, y, diametre, 4 * PI / 4, 6 * PI / 4)
        circle_arc(x, y + diametre, diametre, 0, 2 * PI / 4)
        circle_arc(x + diametre, y + diametre, diametre, 4 * PI / 4, 2 * PI / 4)
        circle(x, y, 60)
        circle(x + diametre, y + diametre, 60)
    else:
        circle_arc(x, y, diametre, 6 * PI / 4, 4 * PI / 4)
        circle_arc(x, y + diametre, diametre, 2 * PI / 4, 4 * PI / 4)
        circle_arc(x - diametre, y, diametre, 6 * PI / 4, 0)
        circle_arc(x - diametre, y + diametre, diametre, 2 * PI / 4, 0)
        circle(x, y, 60)
        circle(x - diametre, y + diametre, 60)


def draw_plateau():
    ellipseMode("center")
    fill("black")
    for i in range(0, 7, 2):
        line(dx + i * taille_case, dy, 6 * taille_case + dx, 6 * taille_case - i * taille_case + dy)
        line(dx, dy + i * taille_case, 6 * taille_case - i * taille_case + dx, 6 * taille_case + dy)
    for i in range(0, 7, 2):
        line(dx, 6 * taille_case - i * taille_case + dy, 6 * taille_case - i * taille_case + dx, dy)
        line(dx + i * taille_case, 6 * taille_case + dy, 6 * taille_case + dx, dy + i * taille_case)

    for i in range(7):
        if i % 2 == 0:
            for j in range(7):
                if j % 2 == 0:
                    fill("black")
                    circle(i * taille_case + dx, j * taille_case + dy, 10)
                    noFill()
                    circle(i * taille_case + dx, j * taille_case + dy, 50)
                else:
                    circle(i * taille_case + dx, j * taille_case + dy, 10)
        else:
            for j in range(7):
                if j % 2 == 1:
                    fill("black")
                    circle(i * taille_case + dx, j * taille_case + dy, 10)
                    noFill()
                    circle(i * taille_case + dx, j * taille_case + dy, 50)
                else:
                    circle(i * taille_case + dx, j * taille_case + dy, 10)


def setup():
    createCanvas(400, 400)
    background("white")
    ellipseMode("center")
    rectMode("center")


def draw():
    draw_plateau()
    # draw_fixe(0,2)
    fill("green")
    x, y = 30, 30
    # for i in range(3):
    #     square(100+i*taille_case,100,taille_case)
    draw_3_bleu(dx, dy, 0)
    line(100, 0, 100, 400)
    line(0, 100, 400, 100)


run(globals())
