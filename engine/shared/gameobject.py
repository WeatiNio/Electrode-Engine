class GameObject:
    def __init__(self, x=0, y=0, width=100, height=100, colour="#ffffff", visible=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.visible = visible