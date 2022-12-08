from likeprocessing.processing import *

ihm = IhmScreen()


def essai(valeur):
    print(valeur)


def setup():
    createCanvas(400, 260)
    background("grey")
    ihm.init()
    touche = ["1","2","3","*",
              "4","5","6","/",
              "7","8","9","+",
              "0",".","²","-",
              "\x1a6","=","<-","AC"]
    for j in range(len(touche)):
        ihm.addObjet(Bouton(None, (10+(j%4)*40, 50+(j//4)*40, 40, 40), touche[j], command=lambda v=touche[j]: essai(v)))


def compute():
    ihm.scan_events()


def draw():
    ihm.draw()


run(globals())
