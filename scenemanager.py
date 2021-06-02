from gamescene import *

class SceneManager():
    def __init__(self, screen):
        self.go_to(Game(screen))

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self