from random import randint
from likeprocessing.processing import *

bouge = False
coordonnees = [300, 150]


def setup():
    createCanvas(600, 200)
    noStroke()
    ellipseMode("center")


def draw():
    etape1(mouseX(), mouseY())
    etape2(mouseX(), mouseY())
    etape3(mouseX(), mouseY())
    etape4()


# ---------------------------------------------------------------------
def etape1(x, y):
    background(220)
    if survole_zone(x, y):
        dessine_boutons_vides()
        dessine_motifs_boutons()
    else:
        dessine_boutons_vides()


def etape2(x, y):
    if survole_play(x, y):
        dessine_play_couleur()
    elif survole_pause(x, y):
        dessine_pause_couleur()
    elif survole_stop(x, y):
        dessine_stop_couleur()


def etape3(x, y):
    global bouge
    if mouseIsPressed() and survole_play(x, y):
        dessine_play_couleur_click()
        bouge = True
    elif mouseIsPressed() and survole_pause(x, y):
        dessine_pause_couleur_click()
        bouge = False
    elif mouseIsPressed() and survole_stop(x, y):
        dessine_stop_couleur_click()
        bouge = False
        noLoop()


def etape4():
    if bouge:
        coordonnees[0] = coordonnees[0] + randint(-3, 3)
    fill('red')
    circle(coordonnees[0], coordonnees[1], 15)


# -----------------------------------------------------------------------
def survole_zone(x, y):
    if 0 <= x <= 300 and 0 <= y <= 100:
        fill('lightgray')
        rect(0, 0, 300, 100)
        return True


def dessine_boutons_vides():
    fill(150)
    circle(75, 50, 50)
    circle(150, 50, 50)
    circle(225, 50, 50)


def dessine_motifs_boutons():
    fill("black")
    triangle(70, 40, 70, 60, 85, 50)
    rect(143, 40, 5, 20)
    rect(152, 40, 5, 20)
    square(215, 40, 20)


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def survole_play(x, y):
    return distance(x, y, 75, 50) < 25


def survole_pause(x, y):
    return distance(x, y, 150, 50) < 25


def survole_stop(x, y):
    return distance(x, y, 225, 50) < 25


def dessine_play_couleur():
    fill('green')
    circle(75, 50, 50)
    fill('white')
    triangle(70, 40, 70, 60, 85, 50)


def dessine_play_couleur_click():
    fill('green')
    circle(75, 50, 55)
    fill('lightgreen')
    triangle(70, 40, 70, 60, 85, 50)


def dessine_pause_couleur():
    fill('orange')
    circle(150, 50, 50)
    fill('White')
    rect(143, 40, 5, 20)
    rect(152, 40, 5, 20)


def dessine_pause_couleur_click():
    fill('orange')
    circle(150, 50, 55)
    fill('orangeRed')
    rect(143, 40, 5, 20)
    rect(152, 40, 5, 20)


def dessine_stop_couleur():
    fill('red')
    circle(225, 50, 50)
    fill('White')
    square(215, 40, 20)


def dessine_stop_couleur_click():
    fill('red')
    circle(225, 50, 55)
    fill('FireBrick')
    square(215, 40, 20)


# ---------------------------------------------------------------------------

run(globals())
