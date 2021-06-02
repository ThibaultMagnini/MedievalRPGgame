from utils.spritesheet import SpriteSheet
from os import path
import pygame as pg
from config import *

def load_character(path1, player_walkup, player_walkdown, player_walk_right, player_walk_left, 
        player_idleup, player_idledown, player_idle_right, player_idle_left, player_attack_right):

    sprites_character_folder = path1

    spritesheet_walk_up = SpriteSheet(path.join(sprites_character_folder, 'upwalk.png'))
    spritesheet_walk_down = SpriteSheet(path.join(sprites_character_folder, 'downwalk.png'))
    spritesheet_walk_side = SpriteSheet(path.join(sprites_character_folder, 'sidewalk.png'))
    spritesheet_idle_down = SpriteSheet(path.join(sprites_character_folder, '_down idle.png'))
    spritesheet_idle_up = SpriteSheet(path.join(sprites_character_folder, '_up idle.png'))
    spritesheet_idle_side = SpriteSheet(path.join(sprites_character_folder, '_side idle.png'))
    spritesheet_attack = SpriteSheet(path.join(sprites_character_folder, '_side attack.png'))

    player_walkup.append(spritesheet_walk_up.get_sprite(0, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(64, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(128, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(192, 0, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(0, 64, 64, 64))
    player_walkup.append(spritesheet_walk_up.get_sprite(64, 64, 64, 64))

    player_walkdown.append(spritesheet_walk_down.get_sprite(0, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(64, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(128, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(192, 0, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(0, 64, 64, 64))
    player_walkdown.append(spritesheet_walk_down.get_sprite(64, 64, 64, 64))

    player_walk_left.append(spritesheet_walk_side.get_sprite(0, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(64, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(128, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(192, 0, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(0, 64, 64, 64))
    player_walk_left.append(spritesheet_walk_side.get_sprite(64, 64, 64, 64))

    player_idledown.append(spritesheet_idle_down.get_sprite(0,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(64,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(128,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(192,0,64,64))
    player_idledown.append(spritesheet_idle_down.get_sprite(0,64,64,64))

    player_idleup.append(spritesheet_idle_up.get_sprite(0,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(64,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(128,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(192,0,64,64))
    player_idleup.append(spritesheet_idle_up.get_sprite(0,64,64,64))

    player_idle_left.append(spritesheet_idle_side.get_sprite(0,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(64,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(128,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(192,0,64,64))
    player_idle_left.append(spritesheet_idle_side.get_sprite(0,64,64,64))

    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(0, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(64, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(128, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(192, 0, 64, 64), True, False))
    player_idle_right.append(pg.transform.flip(spritesheet_idle_side.get_sprite(0, 64, 64, 64), True, False))

    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(0, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(64, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(128, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(192, 0, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(0, 64, 64, 64), True, False))
    player_walk_right.append(pg.transform.flip(spritesheet_walk_side.get_sprite(64, 64, 64, 64), True, False))

    player_attack_right.append(pg.transform.flip(spritesheet_attack.get_sprite(0, 0, 64, 64), True, False))
    player_attack_right.append(pg.transform.flip(spritesheet_attack.get_sprite(64, 0, 64, 64), True, False))
    player_attack_right.append(pg.transform.flip(spritesheet_attack.get_sprite(0, 64, 64, 64), True, False))

    return player_walkup, player_walkdown, player_walk_right, player_walk_left, player_idleup, player_idledown, player_idle_right, player_idle_left, player_attack_right


def load_combat(pathimg):
    background = pg.image.load(path.join(pathimg, 'battlebackground.png')).convert_alpha()
    panel = pg.image.load(path.join(pathimg, 'panel.png')).convert_alpha()
    return background, panel

def load_enemy_idle(pathimg, enemy_name):
    spritesheet = SpriteSheet(path.join(pathimg, f'{enemy_name}.png'))
    sprites = []
    sprites.append(spritesheet.get_sprite(0, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(80, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(160, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(240, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(320, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(400, 0, 80, 80))

    for frame in sprites:
            frame.set_colorkey(GRAY)
    
    return sprites


def load_enemy_attack(pathimg, enemy_name):
    spritesheet = SpriteSheet(path.join(pathimg, f'{enemy_name}_attack.png'))
    sprites = []
    sprites.append(spritesheet.get_sprite(0, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(80, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(160, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(240, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(320, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(400, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(480, 0, 80, 80))
    sprites.append(spritesheet.get_sprite(560, 0, 80, 80))

    for frame in sprites:
            frame.set_colorkey(BLACK)
    
    return sprites