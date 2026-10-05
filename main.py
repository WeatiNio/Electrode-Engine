import random
import pygame as pg

from gameobject import GameObject
from input import Input

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Electrode Engine")

clock = pg.time.Clock()

input = Input()

player = GameObject()

running = True
while running:
    dt = clock.tick(180) / 1000

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    ## input ##
    input.keys = pg.key.get_pressed()

    if input.is_key_pressed("up"):
        player.y -= 200 * dt
    elif input.is_key_pressed("down"):
        player.y += 200 * dt
    elif input.is_key_pressed("left"):
        player.x -= 200 * dt
    elif input.is_key_pressed("right"):
        player.x += 200 * dt

    ## update ##
    player.update(dt)

    ## draw ##
    screen.fill("#1f1f1f") # fills the background - keep at top

    player.draw(screen)

    pg.display.flip() # draws to the screen - keep at the bottom

pg.quit()