import random
import pygame as pg

from engine.gameobject import GameObject
from engine.input import Input

input("\033[33mYou have launched a test version of the engine, which may be unstable/broken. Engine Project & Game files (.eep, .eeg) can NOT be created/modified in this version. To continue, press 'ENTER'. To exit, hold 'CTRL+C' or simply close the terminal/window\033[0m")

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

    if engine_input.is_key_pressed("up"):
        player.y -= 200 * dt
    elif engine_input.is_key_pressed("down"):
        player.y += 200 * dt
    elif engine_input.is_key_pressed("left"):
        player.x -= 200 * dt
    elif engine_input.is_key_pressed("right"):
        player.x += 200 * dt

    if engine_input.input_began("return"):
        characters = "1234567890abcdef"
        new_colour = "#"
        for i in range(6):
            new_colour += characters[random.randint(1, len(characters)) - 1]

        player.colour = new_colour

    ## update ##
    player.update(dt)

    ## draw ##
    screen.fill("#1f1f1f") # fills the background - keep at top

    player.draw(screen)

    pg.display.flip() # draws to the screen - keep at the bottom

pg.quit()