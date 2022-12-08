from likeprocessing.processing import *

damier = []
joueur = 0
dx, dy = 10, 10
largeur_case = 30
rayon_pion = 20
f =loadImage("fantomme_jaune.png")

def init_damier():
    global damier
    damier = [[0 for j in range(10)] for i in range(10)]
    for i in range(4):
        for j in range(5):
            damier[i][j * 2 + i % 2] = 2
            damier[i + 6][j * 2 + i % 2] = 1


def draw_damier():
    blanc = True
    for y in range(10):
        for x in range(10):
            if blanc:
                fill("white")
                blanc = not blanc
                i=None
            else:
                fill("brown")
                blanc = not blanc
                i=f
            rect(dx + (x * largeur_case), dy + (y * largeur_case), largeur_case, largeur_case)
        blanc = not blanc


def xy_to_ij(x, y) -> tuple:
    return (y - dy) // largeur_case, (x - dx) // largeur_case


def avance_droite(i, j):
    global damier
    if joueur == 0:
        damier[i][j], damier[i - 1][j + 1] = damier[i - 1][j + 1], damier[i][j]
    else:
        damier[i][j], damier[i + 1][j + 1] = damier[i + 1][j + 1], damier[i][j]


def avance_gauche(i, j):
    global damier
    if joueur == 0:
        damier[i][j], damier[i - 1][j - 1] = damier[i - 1][j - 1], damier[i][j]
    else:
        damier[i][j], damier[i + 1][j - 1] = damier[i + 1][j - 1], damier[i][j]


def draw_points():
    blanc = True
    for y in range(10):
        for x in range(10):
            if damier[y][x] == 1:
                fill("white")
                circle(dx + largeur_case // 2 + (x * largeur_case), dx + largeur_case // 2 + (y * largeur_case),
                       rayon_pion)
            elif damier[y][x] == 2:
                fill("black")
                circle(dx + largeur_case // 2 + (x * largeur_case), dx + largeur_case // 2 + (y * largeur_case),
                       rayon_pion)


def test_deplacement_gauche(x, y):
    i, j = xy_to_ij(x, y)
    if 0 <= i-1 and i+1<= 9 and 0 <= j-1 and j <= 9:
        if (joueur == 0 and damier[i][j] == 1 and damier[i - 1][j - 1] == 0) or (
                joueur == 1 and damier[i][j] == 2 and damier[i + 1][j - 1] == 0):
            return True
    return False


def test_deplacement_droite(x, y):
    i, j = xy_to_ij(x, y)
    if 0 <= i-1 and i+1<= 9 and 0 <= j and j+1 <= 9:
        if (joueur == 0 and damier[i][j] == 1 and damier[i - 1][j + 1] == 0) or (
                joueur == 1 and damier[i][j] == 2 and damier[i + 1][j + 1] == 0):
            return True
    return False


def retourne_damier():
    global damier
    for i in range(5):
        for j in range(10):
            damier[i][j], damier[9 - i][9 - j] = damier[9 - i][9 - j], damier[i][j]


def setup():
    createCanvas(largeur_case*10+2*dx, largeur_case*10+2*dy)
    title("Jeu de dame")
    background("grey")
    init_damier()
    ellipseMode("center")

def draw_joueur():
    if joueur == 0:
        title(f"jeu de dame : joueur blanc")
    else:
        title(f"jeu de dame : joueur noir")

def compute():
    global joueur
    if mouseIsPressed():
        if mouse_button_pressed() == 0:
            if test_deplacement_gauche(mouseX(), mouseY()):
                avance_gauche(*xy_to_ij(mouseX(), mouseY()))
                joueur = (joueur + 1) % 2
        elif mouse_button_pressed() == 2:
            if test_deplacement_droite(mouseX(), mouseY()):
                avance_droite(*xy_to_ij(mouseX(), mouseY()))
                joueur = (joueur + 1) % 2


def draw():
    draw_joueur()
    draw_damier()
    draw_points()


run(globals())
