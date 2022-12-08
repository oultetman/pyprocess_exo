from likeprocessing.processing import *
from random import shuffle

nb_rondelles = 1
ecran = 0
tour = loadImage("tour.jpg")
tour = resize_image(tour, (800, 600))
rondelle = None
piquet_depart = None

piquets = [[i for i in range(nb_rondelles * 2 + 1, 1, -2)], [], []]

couleurs = []


def pose_rondelle(rondelle, piquet):
    if len(piquets[piquet]) == 0 or rondelle < piquets[piquet][-1]:
        piquets[piquet].append(rondelle)
        return True
    else:
        return False


def gagne() -> bool:
    return len(piquets[2]) == nb_rondelles


def click_rondelle(name):
    global rondelle, piquet_depart
    piquet_depart, rondelle = eval(name)
    piquets[piquet_depart].pop()


def click_piquet(name):
    global rondelle, piquet_depart
    if rondelle is not None:
        if not pose_rondelle(rondelle, name):
            piquets[piquet_depart].append(rondelle)
        piquet_depart = None
        rondelle = None


def start():
    global ecran, piquets, couleurs
    ihm.delObjet("bouton_start")
    piquets = [[i for i in range(nb_rondelles * 2 + 1, 1, -2)], [], []]
    couleurs = base_colors_name()
    shuffle(couleurs)
    couleurs = {piquets[0][i]: couleurs[i] for i in range(nb_rondelles)}
    ecran = 1


ihm = IhmScreen()
ihm.addObjet(Bouton(None, (10, 100, 100, 50), "Nouvelle partie", command=start, size=78), "bouton_start")


def setup():
    createCanvas(800, 600)
    ihm.init()
    ihm.pack(["bouton_start"])
    background("grey")
    title("La tour de Hanoï")


def draw_ecran0():
    image(tour, 0, 0)
    textStyle("bold")
    text("La tour de Hanoï", 0, 100, 800, allign_h="center", allign_v="center", font_size=78, font_color="darkred",
         no_fill=True, no_stroke=True)


def draw_rondelles():
    mode = rectMode('center')
    for p, piquet in enumerate(piquets):
        for i, r in enumerate(piquet):
            if i == len(piquet) - 1:
                rect(200 + p * 200, 435 - 30 * i, r * 15, 30, fill=couleurs[r], fill_mouse_on="blue4",
                     name=f"{p},{r}", command=click_rondelle)
            else:
                rect(200 + p * 200, 435 - 30 * i, r * 15, 30, fill=couleurs[r])
    if rondelle is not None:
        rect(mouseX(), mouseY(), rondelle * 15, 30, fill=couleurs[rondelle])
    rectMode(mode)


def draw_ecran_jeu():
    fill("brown")
    rect(50, 450, 700, 30)
    for i in range(3):
        rect(190 + i * 200, 200, 20, 250, no_stroke=True, command=click_piquet, name=i, fill_mouse_on="red",
             click_up=True)
        triangle(190 + i * 200, 200, 210 + i * 200, 200, 200 + i * 200, 180, no_stroke=True)


def compute():
    global ecran
    if gagne() and ecran == 1:
        ihm.addObjet(Bouton(None, (10, 100, 100, 50), "Rejouer ?", command=start, size=78), "bouton_start")
        ihm.pack("bouton_start")
        ecran = 2
    ihm.scan_events()


def draw():
    if ecran == 0:
        draw_ecran0()
    elif ecran == 1:
        draw_ecran_jeu()
        draw_rondelles()
    elif ecran == 2:
        draw_ecran_jeu()
        draw_rondelles()
        text("Bravo!\nVous avez gagné!", 0, 5, 800, 200, allign_h="center", font_size=78, no_fill=True, no_stroke=True,
             font_color="darkred", style="bolditalic")

    ihm.draw()


run(globals())
