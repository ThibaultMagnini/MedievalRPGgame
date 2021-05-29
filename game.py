from sprites.items import HealingPotion, StaminaPotion
from sprites.grass import Grass
from utils.spritesheet import SpriteSheet
from utils.camera import Camera
import pygame as pg
import sys
from config import *
from os import path 
from sprites.player import *
from sprites.wall import *
from utils.map import * 
from utils.hud import *
from utils.setup import *

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.myfont = pg.font.Font("sprites\character\Livingst.ttf", 32)
        self.myfontbutton = pg.font.SysFont("Comic Sans MS", 15)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.hud = Hud(WIDTH, HEIGHT, self)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        sprites_character_folder = path.join(game_folder,'sprites/character')
        sprites_tree_folder = path.join(game_folder,'sprites/environment')
        map_folder = path.join(sprites_tree_folder, 'maps')

        self.map = TiledMap(path.join(map_folder, 'map2.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.player_walkup = []
        self.player_walkdown = []
        self.player_walk_right = []
        self.player_walk_left = []
        self.player_idleup = []
        self.player_idledown = []
        self.player_idle_right = []
        self.player_idle_left = []
        self.tree_sprites = []
        self.grass_sprites = []

        self.player_walkup,self.player_walkdown, self.player_walk_right, self.player_walk_left, self.player_idleup, self.player_idledown, self.player_idle_right, self.player_idle_left= load_character(sprites_character_folder, self.player_walkup,self.player_walkdown, self.player_walk_right, self.player_walk_left, self.player_idleup, self.player_idledown, self.player_idle_right, self.player_idle_left)

        for frame in self.player_idleup:
            frame.set_colorkey(BLACK)    
        
        for frame in self.player_idledown:
            frame.set_colorkey(BLACK)  
        
        for frame in self.player_idle_right:
            frame.set_colorkey(BLACK)    
        
        for frame in self.player_idle_left:
            frame.set_colorkey(BLACK) 

        for frame in self.player_walkup:
            frame.set_colorkey(BLACK)    
        
        for frame in self.player_walkdown:
            frame.set_colorkey(BLACK)  
        
        for frame in self.player_walk_right:
            frame.set_colorkey(BLACK)    
        
        for frame in self.player_walk_left:
            frame.set_colorkey(BLACK)  


        self.healingpot_image = pg.image.load(path.join(sprites_tree_folder, 'POTION 6.png')).convert_alpha()
        self.staminapot_image = pg.image.load(path.join(sprites_tree_folder, 'POTION 3.png')).convert_alpha()

        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.image.load(path.join(sprites_tree_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grass = pg.sprite.Group()
        self.healingpotions = pg.sprite.Group()
        self.staminapotions = pg.sprite.Group()
        

        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
            if tile_object.name == "player":
                self.player = Player(self, obj_center.x, obj_center.y)
            elif tile_object.name == "wall":
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            elif tile_object.name == "healingpot":
                HealingPotion(self, obj_center)
            elif tile_object.name == "staminapot":
                StaminaPotion(self, obj_center)

        self.camera = Camera(self.map.width, self.map.height)
        self.night = False


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        
        hits = pg.sprite.spritecollide(self.player, self.healingpotions, False)
        for hit in hits:
            if self.player.inventory.inventory_slots["healingpot"] < 20:
                hit.kill()
                self.player.inventory.addHealingPot(1)

        hits = pg.sprite.spritecollide(self.player, self.staminapotions, False)
        for hit in hits:
            if self.player.inventory.inventory_slots["staminapot"] < 20:
                hit.kill()
                self.player.inventory.addStaminaPot(1)  


    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    def render_fog(self):
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)

    def draw(self):  
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        
        if self.night:
            self.render_fog()

        self.hud.draw(self.screen)

        pg.display.flip()



    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_n:
                    self.night = not self.night
                if event.key == pg.K_1:
                    self.player.inventory.consumeHealing()
                if event.key == pg.K_2:
                    self.player.inventory.consumeStamina()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
