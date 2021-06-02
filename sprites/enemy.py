import pygame as pg
from config import *
from utils.setup import *
vec = pg.math.Vector2
import random

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, pos, enemy_name, number, strenght=6, health=150):
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        game_folder = path.dirname(__file__)
        sprites_enemy = path.join(game_folder,'environment\enemies')
        self.enemy_name = enemy_name
        self.enemy_idle_anim = load_enemy_idle(sprites_enemy, enemy_name)
        self.enemy_attack_anim = load_enemy_attack(sprites_enemy, enemy_name)

        self.enemy_idle_anim_scaled = [pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3)) for img in self.enemy_idle_anim]
        self.enemy_attack_anim_scaled = [pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3)) for img in self.enemy_attack_anim]
        
        self.pos = pos

        self.number = number
        self.in_combat = False
        if not self.in_combat:
            self.image = self.enemy_idle_anim[0]
        else:
            self.image = self.enemy_idle_anim_scaled[0]

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.changesprite = 0
        self.currentframe = 1
        self.health = health
        self.max_health = health
        self.strength = strenght
        self.alive = True
        self.attacking = False


    def attack(self, target):
        rand = random.randint(-5, 7)
        damadge = self.strength + rand
        self.attacking = True
        self.currentframe = 0
        target.health -= damadge
        if target.health <= 0:
            target.alive = False


    def update(self):
        self.changesprite += 1
        if not self.in_combat:
            if self.changesprite >= 10:
                self.currentframe = (self.currentframe + 1) % len(self.enemy_idle_anim)
                self.image = self.enemy_idle_anim[self.currentframe]
                self.changesprite = 0
        elif self.in_combat: 
            if not self.attacking:
                if self.changesprite >= 10:
                    self.currentframe = (self.currentframe + 1) % len(self.enemy_idle_anim)
                    self.image = self.enemy_idle_anim_scaled[self.currentframe]
                    self.changesprite = 0
            else: 
                if self.changesprite >= 10:
                    self.currentframe = (self.currentframe + 1) % len(self.enemy_attack_anim)
                    if self.currentframe == 7:
                        self.attacking = False
                    self.image = self.enemy_attack_anim_scaled[self.currentframe]
                    self.changesprite = 0