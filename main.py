import random
import pygame as pg

from engine.gameobject import GameObject
from engine.input import Input

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Electrode Engine")

engine_clock = pg.time.Clock()
engine_input = Input()

player = GameObject()

running = True
while running:
    dt = engine_clock.tick(180) / 1000

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    ## input ##
    engine_input.update_keys()

    ## update ##
    player.update(dt)

    ## draw ##
    screen.fill("#1f1f1f") # fills the background - keep at top

    player.draw(screen)

    pg.display.flip() # draws to the screen - keep at the bottom

pg.quit()