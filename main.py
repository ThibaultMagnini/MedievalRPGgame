from scenemanager import SceneManager
import pygame as pg
from config import *

pg.init()
pg.font.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
manager = SceneManager(screen)

while True:
    manager.scene.new()
    manager.scene.run()
    