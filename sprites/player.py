from sprites.inventory import Inventory
import pygame as pg
from config import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.player_sprites = game.player_sprites
        self.image = self.player_sprites[0]
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.changesprite = 0
        self.rightdirection = False

        self.health = 100
        self.stamina = 100 

        self.inventory = Inventory(self)

        for i in range(len(self.player_sprites)):
            self.player_sprites.append(pg.transform.flip(self.player_sprites[i], True, False)) 


    # TODO optimize and clean player animation when walking 
    def get_keys(self):
        self.changesprite += 1
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] or keys[pg.K_a]:

            if self.rightdirection == True:
                self.image = self.player_sprites[0]
                self.rightdirection = False

            self.vel.x = -PLAYER_SPEED
            if self.changesprite >= 3:
                if self.image == self.player_sprites[0]:
                    self.image = self.player_sprites[1]
                elif self.image == self.player_sprites[1]:
                    self.image = self.player_sprites[2]
                elif self.image == self.player_sprites[2]:
                    self.image = self.player_sprites[3]
                elif self.image == self.player_sprites[3]:
                    self.image = self.player_sprites[4]
                elif self.image == self.player_sprites[4]:
                    self.image = self.player_sprites[5]
                elif self.image == self.player_sprites[5]:
                    self.image = self.player_sprites[6]
                elif self.image == self.player_sprites[6]:
                    self.image = self.player_sprites[7]
                elif self.image == self.player_sprites[7]:
                    self.image = self.player_sprites[8]
                elif self.image == self.player_sprites[8]:
                    self.image = self.player_sprites[0]
                self.changesprite = 0

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            
            self.vel.x = PLAYER_SPEED

            if self.rightdirection == False:
                self.image = self.player_sprites[9]
                self.rightdirection = True

            if self.changesprite >= 3:
                if self.image == self.player_sprites[9]:
                    self.image = self.player_sprites[10]
                elif self.image == self.player_sprites[10]:
                    self.image = self.player_sprites[11]
                elif self.image == self.player_sprites[11]:
                    self.image = self.player_sprites[12]
                elif self.image == self.player_sprites[12]:
                    self.image = self.player_sprites[13]
                elif self.image == self.player_sprites[13]:
                    self.image = self.player_sprites[14]
                elif self.image == self.player_sprites[14]:
                    self.image = self.player_sprites[15]
                elif self.image == self.player_sprites[15]:
                    self.image = self.player_sprites[16]
                elif self.image == self.player_sprites[16]:
                    self.image = self.player_sprites[17]
                elif self.image == self.player_sprites[17]:
                    self.image = self.player_sprites[9]
                self.changesprite = 0
                
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
            if self.changesprite >= 3:
                if self.image == self.player_sprites[0]:
                    self.image = self.player_sprites[1]
                elif self.image == self.player_sprites[1]:
                    self.image = self.player_sprites[2]
                elif self.image == self.player_sprites[2]:
                    self.image = self.player_sprites[3]
                elif self.image == self.player_sprites[3]:
                    self.image = self.player_sprites[4]
                elif self.image == self.player_sprites[4]:
                    self.image = self.player_sprites[5]
                elif self.image == self.player_sprites[5]:
                    self.image = self.player_sprites[6]
                elif self.image == self.player_sprites[6]:
                    self.image = self.player_sprites[7]
                elif self.image == self.player_sprites[7]:
                    self.image = self.player_sprites[8]
                elif self.image == self.player_sprites[8]:
                    self.image = self.player_sprites[0]
                self.changesprite = 0
        
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            if self.changesprite >= 3:
                if self.image == self.player_sprites[0]:
                    self.image = self.player_sprites[1]
                elif self.image == self.player_sprites[1]:
                    self.image = self.player_sprites[2]
                elif self.image == self.player_sprites[2]:
                    self.image = self.player_sprites[3]
                elif self.image == self.player_sprites[3]:
                    self.image = self.player_sprites[4]
                elif self.image == self.player_sprites[4]:
                    self.image = self.player_sprites[5]
                elif self.image == self.player_sprites[5]:
                    self.image = self.player_sprites[6]
                elif self.image == self.player_sprites[6]:
                    self.image = self.player_sprites[7]
                elif self.image == self.player_sprites[7]:
                    self.image = self.player_sprites[8]
                elif self.image == self.player_sprites[8]:
                    self.image = self.player_sprites[0]
                self.changesprite = 0
        
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

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
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls_x()
        self.rect.y = self.pos.y
        self.collide_with_walls_y()
        