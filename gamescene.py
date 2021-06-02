from sprites.enemy import Enemy
from scene import Scene
from sprites.items import HealingPotion, StaminaPotion
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
from combat import *

class Game(Scene):
    def __init__(self, screen, player=None, gamestate={}):
        super(Game, self).__init__()
        self.screen = screen
        self.myfont = pg.font.Font("sprites\character\Livingst.ttf", 32)
        self.myfontbutton = pg.font.SysFont("Comic Sans MS", 15)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.hud = Hud(WIDTH, HEIGHT, self)
        self.gamestate = gamestate
        self.player = player
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
        self.player_attack_right = []

        self.player_walkup,self.player_walkdown, self.player_walk_right, self.player_walk_left, self.player_idleup, self.player_idledown, self.player_idle_right, self.player_idle_left, self.player_attack_right = load_character(sprites_character_folder, self.player_walkup,self.player_walkdown, self.player_walk_right, self.player_walk_left, self.player_idleup, self.player_idledown, self.player_idle_right, self.player_idle_left, self.player_attack_right)

        for frame in self.player_attack_right:
            frame.set_colorkey(BLACK) 

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
        self.enemies = pg.sprite.Group()
        

        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
            if tile_object.name == "player":
                if self.player is None:
                    self.player = Player(self, obj_center.x, obj_center.y)
                else:
                    self.player = Player(self, self.player.pos.x, self.player.pos.y, health=self.player.health, stamina=self.player.stamina, inventory=self.player.inventory )
            elif tile_object.name == "wall":
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            elif tile_object.name == "healingpot1":
                HealingPotion(self, obj_center)
                self.gamestate["heallingpot1"] = True
            elif tile_object.name == "staminapot1":
                StaminaPotion(self, obj_center)
                self.gamestate["staminapot1"] = True
            elif tile_object.name == "blob_enemy1":
                if "blob_enemy1" in self.gamestate:
                    if not self.gamestate["blob_enemy1"]:
                        print("skip dan")
                    else: 
                        Enemy(self, obj_center, 'blob_enemy', number=1)
                        self.gamestate["blob_enemy1"] = True              
                else:
                    Enemy(self, obj_center, 'blob_enemy', number=1)
                    self.gamestate["blob_enemy1"] = True

        self.camera = Camera(self.map.width, self.map.height)
        self.night = False


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # print(self.clock.get_fps())
            self.events()
            self.update()
            self.draw(self.screen)
            

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

        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        for hit in hits:
            self.playing = False
            hit.kill()
            self.manager.go_to(CombatScene(player=self.player, enemy=hit, gamestate=self.gamestate, screen=self.screen))
    


    def render_fog(self, screen):
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)


    def draw(self, screen):  
        screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        
        for sprite in self.all_sprites:
            screen.blit(sprite.image, self.camera.apply(sprite))
        
        if self.night:
            self.render_fog(screen)

        self.hud.draw(screen)

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
                

