import pygame as pg

from engine.shared.scene import Scene

class Runtime:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((640, 480))
        self.running = True
        self.clock = pg.time.Clock()

        self.active_scene = Scene()

    def process_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

    def update(self, dt):
        pass

    def render(self):
        self.screen.fill("#1f1f1f")

        for game_object in self.active_scene.objects.values():
            if game_object.visible:
                pg.draw.rect(self.screen, game_object.colour, pg.Rect(game_object.x, game_object.y, game_object.width, game_object.height))

        pg.display.flip()

    def start(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            self.process_events()
            self.update(dt)
            self.render()

        pg.quit()