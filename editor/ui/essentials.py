import pygame as pg

def ui():
    font = pg.Font(None, 24)

    toolbar = (pg.Rect(0, 0, 640, 50), "#3f3f3f")
    add_game_object = (pg.Rect(480, 10, 150, 30), "#6f6f6f", "+ New GameObject")

    return {
        "toolbar": toolbar,
        "add_game_object": add_game_object
    }