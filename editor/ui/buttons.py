import pygame as pg

def add_game_object(scene):
    object = scene.create_object()
    print(object)

def get_buttons():
    return {
        "add_game_object": (
            pg.Rect(480, 10, 150, 30),
            "#6f6f6f",
            "+ New GameObject",
            add_game_object
        )
    }