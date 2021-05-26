
import pygame as pg
import pytweening as tween
from config import *
vec = pg.math.Vector2

class Weapon:
    def __init__(self, damadge, stamina_drain, image):
        self.damadge = damadge
        self.stamina_drain = stamina_drain
        self.image = image

class Armor:
    def __init__(self, armor_amount, image):
        self.armor_amount = armor_amount
        self.image = image

class HealingPotion(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.healingpotions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.healingpot_image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def update(self):
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.pos.y + offset * self.dir
        self.step += BOB_SPEED

        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1 

class StaminaPotion(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.staminapotions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.staminapot_image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def update(self):
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.pos.y + offset * self.dir
        self.step += BOB_SPEED

        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1 