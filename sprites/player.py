from sprites.inventory import Inventory
import pygame as pg
from config import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
       
        self.player_walkup = game.player_walkup
        self.player_walkdown = game.player_walkdown
        self.player_walk_left = game.player_walk_left
        self.player_walk_right = game.player_walk_right
        self.player_idleup = game.player_idleup
        self.player_idledown = game.player_idledown
        self.player_idle_left = game.player_idle_left
        self.player_idle_right = game.player_idle_right

        self.right = False
        self.up = False
        self.down = True
        self.walking = False
        
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

        self.image = self.player_walkdown[0]
        self.rect = self.image.get_rect()

        self.changesprite = 0
        self.currentframe = 1

        self.health = 100
        self.stamina = 100 

        self.inventory = Inventory(self)

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


    def update(self):
        self.changesprite += 1
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

        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls_x()
        self.rect.y = self.pos.y
        self.collide_with_walls_y()
        