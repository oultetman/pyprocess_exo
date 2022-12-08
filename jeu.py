from likeprocessing.processing import *
x = 0
y = 0

temporisation = Tempo(1000)
score=0
coeur =  loadImage("fantomme_jaune.png")
nbre_vie = 5

def draw_life(x,y):
    for i in range(nbre_vie):
        image(coeur,x + i * 40,y)

def on_rect():
    return x<=mouseX()<=x+50 and y<=mouseY()<=y+30

def setup():
    createCanvas(400,400)
    background("#8400FE")
    fill_mouse_on("orange")

def compute():
    global x,y, score,nbre_vie
    if nbre_vie > 0:
        if temporisation.fin():
            nbre_vie -= 1
            x = random(0, 300)
            y = random(0,350)
        if mouse_click_down():
            if mouse_button_pressed() == 0:
                if on_rect():
                    score += 50
                    x = random(0,300)
                    y = random(0,300)
                    temporisation.reset()
                else:
                    score -= 10
    else:
        if in_polygone(*mouseXY(),[(20,200),(300,200),(300,250),(20,250)]):
            if mouse_click_down():
                if mouse_button_pressed() == 0:
                    nbre_vie = 5
                    score = 0
def draw():
    if nbre_vie>0:
        rect(x,y,50,30)
    else:
        text("cheh tu as perdue",20,200,360,font_size=48,fill="red",allign_h="center")
    text(str(score),10,10,110,allign_h="right",allign_v="center",size = 30,noFill=True,no_stroke=True)
    rect(x, y,50,30)
    draw_life(190,10)

run(globals())