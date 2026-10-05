import pygame as pg
from gameobject import GameObject

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Electrode Engine")

clock = pg.time.Clock()

player = GameObject()

running = True
while running:
    dt = clock.tick(180) / 1000

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    ## input (TODO) ##

    ## update ##
    player.update(dt)

    ## draw ##
    screen.fill("#1f1f1f") # fills the background - keep at top

    player.draw(screen)

    pg.display.flip() # draws to the screen - keep at the bottom

pg.quit()