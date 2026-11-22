import math

import pygame as pg

class Editor:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((640, 480))
        self.running = True
        self.clock = pg.time.Clock()
        pg.display.set_caption("Electrode Editor | Loading...")

    def process_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

    def update(self, dt):
        pass

    def render(self):
        self.screen.fill("#1f1f1f")

        pg.display.flip()

    def start(self):
        while self.running:
            dt = self.clock.tick(180) / 1000
            fps = math.floor(1 / dt)

            pg.display.set_caption(f"Electrode Editor | {fps}FPS")

            self.process_events()
            self.update(dt)
            self.render()

        pg.quit()