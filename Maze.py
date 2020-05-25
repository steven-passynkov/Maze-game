import pygame as pg
from sys import path
from sys import exit
import os
import random

#my_path = os.path.dirname(os.path.realpath(__file__))
#os.chdir(my_path)
#path.append(my_path)

#Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#Setup
pg.init()
screen = pg.display.set_mode((800,600)) #set your window size, (x,y)
pg.display.set_caption("Game Title")
clock = pg.time.Clock()#you can just use import time and time.sleep()
font = pg.font.Font('freesansbold.ttf', 32)
state = 1
num = 0
t = 0
g = 0
time_coin = 0
health = 15
maze = []
walls = 1
ran1 = random.uniform(0.5,1.5)
ran2 = random.uniform(0.2,1.9)
ran3 = random.uniform(0.6,2.3)
ran4 = random.uniform(0.3,2.5)
player = pg.Rect(10,10,50,50)
coin_1 = pg.Rect(700,510,50,50)
coin_2 = 0
coin_3 = 0
side = pg.Rect(0,80,10,600)
end = pg.Rect(225,120,50,50)

wall_1 = pg.Rect(0,75,700,10)
maze.append(wall_1)
wall_2 = pg.Rect(700,75,10,100)
maze.append(wall_2)
wall_3 = pg.Rect(630,260,200,10)
maze.append(wall_3)
wall_4 = pg.Rect(630,170,10,90)
maze.append(wall_4)
wall_5 = pg.Rect(520,170,120,10)
maze.append(wall_5)
wall_6 = pg.Rect(450,75,10,400)
maze.append(wall_6)
wall_7 = pg.Rect(450,260,180,10)
maze.append(wall_7)
wall_8 = pg.Rect(450,370,270,10)
maze.append(wall_8)
wall_9 = pg.Rect(450,460,10,140)
maze.append(wall_9)
wall_10 = pg.Rect(460,460,180,10)
maze.append(wall_10)
wall_11 = pg.Rect(635,460,10,140)
maze.append(wall_11)
wall_12 = pg.Rect(645,460,270,10)
maze.append(wall_12)

move_1 = pg.Rect(300,500,150,10)
maze.append(move_1)
move_2 = pg.Rect(300,400,150,10)
maze.append(move_2)
move_3 = pg.Rect(300,300,150,10)
maze.append(move_3)
move_4 = pg.Rect(300,200,150,10)
maze.append(move_4)

top = pg.Rect(0,0,800,0)
maze.append(top)
bottom = pg.Rect(0,600,800,0)
maze.append(bottom)
side_r = pg.Rect(0,0,0,600)
maze.append(side_r)
side_l = pg.Rect(800,0,0,800)
maze.append(side_l)

def move(which,num):
    keys = pg.key.get_pressed()
    if which == 0:
        player[num] -= 1
        if keys[pg.K_LSHIFT]:
            player[num] -= 2
    if which == 1:
        player[num] += 1
        if keys[pg.K_LSHIFT]:
            player[num] += 2

def move_wall(wall,speed):
    global walls
    if wall.colliderect(wall_6):
        walls = 1
    if wall.colliderect(side):
        walls = 2

    if walls == 1:
        wall[0] -= speed
    if walls == 2:
        wall[0] -= speed
    pg.draw.rect(screen,white,wall)

while True:
    while state == 0:
        pg.event.pump()
        screen.fill(black)
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            move(0,1)
        if keys[pg.K_s]:
            move(1,1)
        if keys[pg.K_a]:
            move(0,0)
        if keys[pg.K_d]:
            move(1,0)
            
        if player.colliderect(top):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(bottom):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_r):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_l):
            player = pg.Rect(10,10,50,50)
            
        pg.draw.rect(screen,white,player)
        pg.display.flip()
        clock.tick(50)

    while state == 1:
        pg.event.pump()
        keys = pg.key.get_pressed()
        screen.fill(black)
        
        move_wall(move_1,ran1)
        move_wall(move_2,ran2)
        move_wall(move_3,ran3)
        move_wall(move_4,ran4)

        if keys[pg.K_w]:
            move(0,1)
        if keys[pg.K_s]:
            move(1,1)
        if keys[pg.K_a]:
            move(0,0)
        if keys[pg.K_d]:
            move(1,0)
        if player.colliderect(end):
            state = 2
        if player.colliderect(wall_7):
            player = pg.Rect(500,300,50,50)
        if player.colliderect(coin_1):
            coin = pg.Rect(999,999,50,50)
        if player.colliderect(wall_10):
            player = pg.Rect(530,500,50,50)
            time_coin = 1
        if time_coin == 1:
            g += 1
            if g == 90:
                player = pg.Rect(400,530,50,50)
        if player.colliderect(wall_11):

            if t == 0:
                player = pg.Rect(700,510,50,50)
                t += 1
            if t == 10:
                player = pg.Rect(530,500,50,50)
                t -= 1

        for wall in maze:
            pg.draw.rect(screen,white,wall)
            if player.colliderect(wall):
                health -= 1
                if health == 0:
                    player = pg.Rect(10,10,50,50)
                    health = 15

        pg.draw.rect(screen,white,coin_1)
        pg.draw.rect(screen,white,player)
        pg.draw.rect(screen,white,side)
        pg.draw.rect(screen,white,end)

        num = num+1
        num_text = font.render(str(num), True, white)
        num_textRect = num_text.get_rect()
        num_textRect.center = (400, 300)
        screen.blit(num_text,num_textRect)
        
        h_text = font.render(str(health), True, white)
        h_textRect = h_text.get_rect()
        h_textRect.center = (300, 300)
        screen.blit(h_text,h_textRect)


        pg.display.flip()
        clock.tick(50)
        
    while state == 2:
        pg.event.pump()
        screen.fill(black)
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            move(0,1)
        if keys[pg.K_s]:
            move(1,1)
        if keys[pg.K_a]:
            move(0,0)
        if keys[pg.K_d]:
            move(1,0)
            
        if player.colliderect(top):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(bottom):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_r):
            player = pg.Rect(10,10,50,50)
        if player.colliderect(side_l):
            player = pg.Rect(10,10,50,50)
            
        pg.draw.rect(screen,white,player)
        pg.display.flip()
        clock.tick(50)
