import pygame as pg

from editor.ui.essentials import ui
from editor.ui.buttons import get_buttons
from editor.ui.text import draw_text

from engine.shared.scene import Scene

class Editor:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((640, 480))
        self.running = True
        self.clock = pg.time.Clock()
        self.ui = ui()
        self.buttons = get_buttons()
        self.font = pg.font.Font(None, 24)
        self.active_scene = Scene()
        self.selected_object = None
        pg.display.set_caption("Electrode Engine")
        pg.display.set_icon(pg.image.load(r"assets/icon.ico"))

    def process_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()

                for button in self.buttons.values():
                    if button[0].collidepoint(mouse_pos):
                        button[3](self.active_scene)

    def update(self, dt):
        pass

    def render(self):
        self.screen.fill("#1f1f1f")

        """
        GAMEOBJECT RENDERING HERE
        """
        for object in self.active_scene.objects.items():
            game_object = object[1]
            rect = pg.rect.Rect(game_object.x, game_object.y, game_object.width, game_object.height)

            if game_object.visible:
                pg.draw.rect(surface=self.screen, rect=rect, color=game_object.colour)

        """
        IMPORTANT UI OVERLAYS HERE
        e.g. TOOLBAR, HIERARCHY
        """
        for _, ui_obj in self.ui.items():
            rect = ui_obj[0]
            text = ui_obj[2] if len(ui_obj) > 2 else None

            pg.draw.rect(surface=self.screen, rect=rect, color=ui_obj[1])

            if text: draw_text(self.screen, self.font, text, (rect.x + (rect.width / 2), rect.y + (rect.height / 2)), "#dfdfdf")

        for _, ui_obj in self.buttons.items():
            rect = ui_obj[0]
            text = ui_obj[2] if len(ui_obj) > 2 else None

            pg.draw.rect(surface=self.screen, rect=rect, color=ui_obj[1])

            if text: draw_text(self.screen, self.font, text, (rect.x + (rect.width / 2), rect.y + (rect.height / 2)), "#dfdfdf")

        pg.display.flip()

    def start(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            fps = self.clock.get_fps()

            pg.display.set_caption(f"Electrode Engine | {fps:.0f}fps")

            self.process_events()
            self.update(dt)
            self.render()

        pg.quit()