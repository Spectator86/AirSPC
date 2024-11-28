import pygame as pg
from settings import *
from player import Player
from plane import Plane
import random as rand

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("AirS")

player = Player(250, 700, "images/player/image.png", 10, 50, 75)

clock = pg.time.Clock()

planes = list()

failed = False

timer = 3
t = 0
l = 120

score = 0
best_score = 0

a = 10

fontsize = 20
font = pg.font.SysFont("Arial", fontsize)

deleted = list()

def update_save():
    global best_score
    if score > best_score:
        best_score = score
        with open("save.txt", "w", encoding="utf-8") as file:
            file.write(str(int(best_score)))

while True:
    try:
        with open("save.txt", "r", encoding="utf-8") as file:
            best_score = int(file.read())
    except ValueError:
        print("ValueError!")
        exit()
    except FileNotFoundError:
        print("File not found!")
        exit()

    sc.fill(WHITE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            update_save()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                PAUSED = not PAUSED

    score_text = font.render("SCORE", True, BLACK)
    score_text2 = font.render(str(int(score)), True, BLACK)
    best_score_text = font.render("BEST", True, BLACK)
    if score > best_score:
        best_score_text2 = font.render(str(int(score)), True, BLACK)
    else:
        best_score_text2 = font.render(str(int(best_score)), True, BLACK)

    player.draw(sc)
    if not PAUSED:
        score += 0.2
        player.move()

    for i in range(len(planes)):
        if planes[i][0].rect.y > HEIGHT + 100:
            deleted.append(i)

    for i in deleted:
        planes.pop(i)
    deleted.clear()

    for i in planes:
        i[0].draw(sc)
        i[1].draw(sc)

        if not PAUSED:
            i[0].move()
            i[1].move()

            if i[0].rect.colliderect(player.rect):
                failed = True
            if i[1].rect.colliderect(player.rect):
                failed = True
    
    if t >= timer*FPS and not PAUSED:
        x1 = rand.randint(-300, 0)
        x2 = x1 + l + 500
        planes.append([Plane(x1, -100, "images/plane.png", 500, 50), Plane(x2, -100, "images/plane.png", 500, 50)])
        
        t = 0
        if l > 100:
            l -= 0.01
        if timer > 1:
            timer -= 0.1
        if SPEED < 50:
            SPEED -= 0.1
    elif not PAUSED:
        t += 1

    if failed:
        #Lose screen
        update_save()
        exit()

    sc.blit(score_text, (a, 1*a))
    sc.blit(score_text2, (a, 2*a + fontsize))
    sc.blit(best_score_text, (a, 3*a + fontsize * 2))
    sc.blit(best_score_text2, (a, 4*a + fontsize * 3))

    pg.display.update()
    clock.tick(FPS)
