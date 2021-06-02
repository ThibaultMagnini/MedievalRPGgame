from sprites.inventory import Inventory
import pygame as pg
from config import *
import random
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, health=100, stamina=100, inventory=None):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = 'Player'
        self.alive = True
        self.player_walkup = game.player_walkup
        self.player_walkdown = game.player_walkdown
        self.player_walk_left = game.player_walk_left
        self.player_walk_right = game.player_walk_right
        self.player_idle_right_combat = [pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3)) for img in game.player_idle_right]
        self.player_idleup = game.player_idleup
        self.player_idledown = game.player_idledown
        self.player_idle_left = game.player_idle_left
        self.player_idle_right = game.player_idle_right
        self.player_attack_right = [pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3)) for img in game.player_attack_right]

        self.right = False
        self.up = False
        self.down = True
        self.walking = False
        self.in_combat=False
        self.attacking = False
        
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

        if not self.in_combat:
            self.image = self.player_walkdown[0]
        else:
            self.image = self.player_idle_right_combat[0]
            
        self.rect = self.image.get_rect()

        self.changesprite = 0
        self.currentframe = 1

        self.health = health
        self.stamina = stamina

        if inventory is None:
            self.inventory = Inventory(self)
        else:
            self.inventory = inventory

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.walking = True
            self.vel.x = -PLAYER_SPEED
            if self.changesprite >= 10:
                self.currentframe = (self.currentframe + 1) % len(self.player_walkdown)
                self.changesprite = 0
            self.image = self.player_walk_left[self.currentframe]
            self.changesprite += 1
            self.right = False
            self.up = False
            self.down = False

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.walking = True
            self.vel.x = PLAYER_SPEED
            if self.changesprite >= 10:
                self.currentframe = (self.currentframe + 1) % len(self.player_walkdown)
                self.changesprite = 0
            self.image = self.player_walk_right[self.currentframe]
            self.changesprite += 1
            self.right = True
            self.up = False
            self.down = False

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.walking = True
            self.vel.y = -PLAYER_SPEED
            if self.changesprite >= 6:
                self.currentframe = (self.currentframe + 1) % len(self.player_walkdown)
                self.changesprite = 0
            self.image = self.player_walkup[self.currentframe]
            self.changesprite += 1
            self.right = False
            self.up = True
            self.down = False

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.walking = True
            self.vel.y = PLAYER_SPEED
            if self.changesprite >= 6:
                self.currentframe = (self.currentframe + 1) % len(self.player_walkdown)
                self.changesprite = 0
            self.image = self.player_walkdown[self.currentframe]
            self.changesprite += 1
            self.right = False
            self.up = False
            self.down = True
        
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
        
        self.walking = False
        

    def collide_with_walls_x(self):
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.vel.x > 0:
                self.pos.x = hits[0].rect.left - self.rect.width
            if self.vel.x < 0:
                self.pos.x = hits[0].rect.right
            self.vel.x = 0
            self.rect.x = self.pos.x
        
    def collide_with_walls_y(self):
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.vel.y > 0:
                self.pos.y = hits[0].rect.top - self.rect.height
            if self.vel.y < 0:
                self.pos.y = hits[0].rect.bottom
            self.vel.y = 0
            self.rect.y = self.pos.y

    def attack(self, target):
        rand = random.randint(-5, 7)
        damadge = self.inventory.getWeaponDamadge() + rand
        stamina_drain = self.inventory.getWeaponStaminaUsage() + rand
        if self.stamina > stamina_drain:
            self.attacking = True
            self.currentframe = 0
            target.health -= damadge
            self.stamina -= stamina_drain
            if target.health <= 0:
                target.alive = False
        else:
            if self.stamina + 30 < 100:
                self.stamina += 30
            else:
                self.stamina += 100 - self.stamina

    def update(self):
        self.changesprite += 1
        if not self.in_combat:
            if not self.walking:
                if self.changesprite >= 10:
                    if self.down:
                        self.currentframe = (self.currentframe + 1) % len(self.player_idle_left)
                        self.image = self.player_idledown[self.currentframe]
                        self.changesprite = 0
                    elif self.right:
                        self.currentframe = (self.currentframe + 1) % len(self.player_idle_left)
                        self.image = self.player_idle_right[self.currentframe]
                        self.changesprite = 0
                    elif self.up:
                        self.currentframe = (self.currentframe + 1) % len(self.player_idle_left)
                        self.image = self.player_idleup[self.currentframe]
                        self.changesprite = 0
                    else:
                        self.currentframe = (self.currentframe + 1) % len(self.player_idle_left)
                        self.image = self.player_idle_left[self.currentframe]
                        self.changesprite = 0
        
        elif self.in_combat:
            if not self.walking:
                if not self.attacking:
                    if self.changesprite >= 10:
                        self.currentframe = (self.currentframe + 1) % len(self.player_idle_left)
                        self.image = self.player_idle_right_combat[self.currentframe]
                        self.changesprite = 0
                else:
                    if self.changesprite >= 10:
                        self.currentframe = (self.currentframe + 1) % len(self.player_attack_right)
                        if self.currentframe == 2:
                            self.attacking = False
                        self.image = self.player_attack_right[self.currentframe]
                        self.changesprite = 0

        
        if not self.in_combat:
            self.get_keys()
            self.pos += self.vel * self.game.dt
            self.rect.x = self.pos.x
            self.collide_with_walls_x()
            self.rect.y = self.pos.y
            self.collide_with_walls_y()
        