import random
import time

from engine.shared.gameobject import GameObject

class Scene:
    def __init__(self):
        self.objects = {}

    def create_object(self):
        game_object = GameObject()
        object_id = self._generate_object_id()

        while object_id in self.objects:
            object_id = self._generate_object_id()

        self.objects[object_id] = game_object

        return game_object

    def delete_object(self, object_id):
        if not object_id in self.objects:
            return -1

        self.objects.pop(object_id)

    def _generate_object_id(self):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
        object_id = ""
        for i in range(20):
            object_id += random.choice(characters)

        return object_id