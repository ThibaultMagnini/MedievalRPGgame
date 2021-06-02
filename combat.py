from random import randint
from utils.hud import HealthBar, StaminaBar
from sprites.enemy import Enemy
from config import *
from utils.setup import load_combat
from scene import Scene
import pygame as pg
import gamescene as game
from os import path
import sys

class CombatScene(Scene):
    def __init__(self, player, enemy, gamestate, screen):
        super(CombatScene, self).__init__()
        self.screen = screen
        self.player = player
        self.gamestate = gamestate
        self.enemy = enemy
        self.player.in_combat = True
        self.enemy.in_combat = True
        self.text = "Combat Scene"
        self.myfont = pg.font.Font("sprites\character\Livingst.ttf", 32)
        self.clock = pg.time.Clock()
        self.player_health_bar = HealthBar(130, COMBATBACKGROUNDHEIGHT + 65, self.player.health, 100, self.screen)
        self.player_stamina_bar = StaminaBar(130, COMBATBACKGROUNDHEIGHT + 130, self.player.stamina, 100, self.screen)

        self.enemy_health_bar = HealthBar(630, COMBATBACKGROUNDHEIGHT + 65, self.enemy.health, self.enemy.max_health, self.screen)
        
        # self.cursor_sword = pg.image.load("sprites\environment\enemies\sword.png").convert_alpha()
        self.first_attack = True
        self.attack = False

        self.current_fighter = 1
        self.total_fighters = 2
        self.action_cooldown = 0
        self.action_wait_time = 120

        self.load_data()

    def run(self):
        self.fighting = True
        while self.fighting:
            self.dt = self.clock.tick(FPS) / 1000
            # print(self.clock.get_fps())
            self.events()
            self.update()
            self.draw()
    
    def draw_text(self, text, text_col, x, y, screen):
        img = self.myfont.render(text, True, text_col)
        screen.blit(img, (x, y))

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.panel, (0, COMBATBACKGROUNDHEIGHT))
        self.screen.blit(self.player.image, (50, 280))
        self.screen.blit(self.enemy.image, (550, 225))
        if self.first_attack == True:
            self.draw_text('Press \'E\' to attack the enemy!', WHITE, 300, 250, self.screen)
        self.draw_text(f'{self.player.name} HP: {self.player.health}', WHITE, 127, COMBATBACKGROUNDHEIGHT + 22, self.screen)
        self.draw_text(f'{self.player.name} Stamina: {self.player.stamina}', WHITE, 127, COMBATBACKGROUNDHEIGHT + 90, self.screen)
        self.draw_text(f'{self.enemy.enemy_name} HP: {self.enemy.health}', RED, 627, COMBATBACKGROUNDHEIGHT + 22, self.screen)
        self.player_health_bar.draw(self.player.health)
        self.player_stamina_bar.draw(self.player.stamina)
        self.enemy_health_bar.draw(self.enemy.health)
        pg.display.flip()


    def update(self):
        self.player.update()
        self.enemy.update()

        potion = False

        if self.player.alive:
            if self.attack:
                if self.current_fighter == 1:
                    self.player.attack(self.enemy)
                    self.attack = False
                    self.current_fighter = 2
                    self.action_cooldown = 0

        if self.enemy.alive:
            if self.current_fighter == 2:
                self.action_cooldown += 1
                if self.action_cooldown >= self.action_wait_time:
                    self.enemy.attack(self.player)
                    self.current_fighter = 1
                    self.action_cooldown = 0
                    rand = randint(5, 15)
                    if self.player.stamina + rand < 100:
                        self.player.stamina += rand
                    else: 
                        self.player.stamina += 100 - self.player.stamina



    def events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.quit()
                if e.key == pg.K_e:
                    self.attack = True
                    self.first_attack = False
                if e.key == pg.K_h:
                    self.fighting = False
                    self.gamestate[f"{self.enemy.enemy_name}{self.enemy.number}"] = False
                    self.manager.go_to(game.Game(self.screen, player=self.player, gamestate=self.gamestate))

    def new(self):
        pass

    def load_data(self):
        game_folder = path.dirname(__file__)
        sprites_tree_folder = path.join(game_folder,'sprites/environment')
        self.background, self.panel = load_combat(sprites_tree_folder)


    def quit(self):
        pg.quit()
        sys.exit()
